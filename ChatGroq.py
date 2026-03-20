from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

# Configuração do modelo
chat = ChatGroq(
    api_key="chave**",
    model='llama-3.3-70b-versatile'
)

# Prompt com propósito claro
template = ChatPromptTemplate.from_messages([
    ("system", 
     "Você é um assistente que organiza a rotina diária do usuário. "
     "Com base nas tarefas informadas, crie um cronograma organizado em formato de tabela com horários. "
     "Use horários realistas e organize de forma lógica e produtiva. "
     "Responda em português e de forma clara."),
    
    ("user", "{tarefas}")
])

chain = template | chat

print("Chatbot Organizador de Dia")
print("Digite suas tarefas (ou 'x' para sair)\n")

while True:
    tarefas = input("Quais são suas tarefas hoje? ")

    if tarefas.lower() == "x":
        print("Encerrando...")
        break

    resposta = chain.invoke({"tarefas": tarefas})

    print("\nSeu planejamento:")
    print(resposta.content)
    print("\n" + "-"*40 + "\n")
