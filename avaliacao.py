qt_excelente = 0
qt_ruim = 0

for i in range(50):  # O range é responsável até onde o laço se repetirá
    print(f"\nEntrevistado {i+1}")
    
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    print("Feedback sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    
    opiniao = int(input("Digite de 1 a 3 com base em sua opinião: "))
    
    if opiniao == 1: #Opinião excelente
        qt_excelente += 1
    elif opiniao == 3: #Opinião ruim
        qt_ruim += 1

# Ao finalizar o range, o programa irá demonstrar os resultados da pesquisa
print("\nResultados da Pesquisa")
print("Quantidade de EXCELENTE:", qt_excelente)
print("Quantidade de RUIM:", qt_ruim)
