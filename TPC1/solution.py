from math import floor
import sys
modalidades = []
total = 0
aptos = 0
inaptos = 0 
escaloes = [0, # 21 - 25
            0, # 26 - 30
            0] # 31 - 35

sys.stdin.readline() # ler o cabeçalho do csv

for linha in sys.stdin:
    # TODO ignore frist line 
    linha = linha.strip("\n") # remover "\n" do fim da linha
    total += 1

    valores = linha.split(',')

    # guardar modalidade se ela n existe
    modalidade = valores[8]
    if modalidade not in modalidades:
        modalidades.append(modalidade)

    # verificar se é apto ou inapto
    teste_aptidao = valores[12]
    if teste_aptidao == "true":
        aptos += 1
    else:   
        inaptos += 1

    # ver range da idade e aumentar escalão de acordo
    idade = int(valores[5])
    if (20 < idade <= 25):
        escaloes[0] += 1
    elif (25 < idade <= 30):
        escaloes[1] += 1
    elif (30 < idade <= 35):
        escaloes[2] += 1
    else:
        print("Error: Idade out of range")
    


print("Lista de modalidades:")
for mod in modalidades:
    print(f"* {mod}")
print()


pAptos = aptos/total*100
pInaptos = inaptos/total*100
print(f"Aptos e Inaptos:\n- Percentagem Aptos: {pAptos:.2f}%\n- Percentagem Inaptos: {pInaptos:.2f}%")
print()

print(f"Distribuição de Idades: \n\t [21 - 25]: {escaloes[0]}\n\t [26 - 30]: {escaloes[1]}\n\t [30 - 35]: {escaloes[2]}")