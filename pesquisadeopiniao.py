# Pesquisa de Opinião da Tudo Web
# Autor: Inês Martinelli
print("             TUDO WEB") # Início
print("Pesquisa de Atendimento ao Cliente:")
print("===================================")
nome = input("Por favor, digite o seu nome: ") # Entrada de dados
idade = int(input("Qual a sua idade? "))
pesquisa = int(input("Qual a sua opinião sobre o nosso atendimento? Insira: 1 para EXCELENTE | 2 para BOM | 3 para RUIM: "))
# Declaração das variávies
excelente = 0
bom = 0
ruim = 0
# Processamento
for i in range(1, 4, 50):
    print("\nAtendimento:", pesquisa)
    if pesquisa == 1:
        excelente += 1 
    elif pesquisa == 2:
          bom += 1 
    elif pesquisa == 3:
          ruim += 1 
# Saída
print("\nAVALIAÇÕES")
print("Quantidade de respostas EXCELENTE: ", excelente)
print("Quantidade de respostas RUIM: ", ruim) # Fim