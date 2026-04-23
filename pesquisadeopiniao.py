# Pesquisa de Opinião da Tudo Web
# Autor: Inês Martinelli
print("\n             TUDO WEB") # Início do programa
print("Pesquisa de Atendimento ao Cliente:")
print("===================================")
# Declaração das variávies
total_entrevistados = 50
qtd_excelente = 0
qtd_ruim = 0

# Processamento
for i in range(1, 49 + 1):
     nome = input("\nPor favor, digite o seu nome: ")
     idade = int(input("Qual a sua idade? "))
     pesquisa = int(input("Qual a sua opinião sobre o nosso atendimento? Insira: 1 para EXCELENTE | 2 para BOM | 3 para RUIM: "))
     print("\nAtendimento:", pesquisa)
     print("=================================")
     
     if pesquisa == 1:
        qtd_excelente += 1 
     elif pesquisa == 3:
          qtd_ruim += 1 
# Saída
print("\nAVALIAÇÕES: ")
print("Quantidade de respostas EXCELENTE: ", qtd_excelente)
print("Quantidade de respostas RUIM: ", qtd_ruim) #Fim do programa 
