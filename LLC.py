# Para a regra de produção da linguagem de palíndromos sem repetição consecutiva de a e b
# 1.	S → §bS | a
# 1.	S → §bS | a
# 3.    S → []

# V = {S, §, a, b}
# sigma = {a, b}
# P =
def LLC(string: str, limite = 1):
    #limite = condição de parada, tamanho da string de saída, tamanho da pilha de memória

	#Aplicando a regra da máquina sobre cada caractere
    for char in string:
        #S → §bS | a
        if char == "S":
            #Condição para a decisão de §bS | a é o limite de tamanho da pilha de memória
            # +3, pois, +2 p/ o tamanho de "S" → "§bS" e +1 p/ tamanho = índice, sendo índice [0...n] e tamanho [1...n]
            if (string.find(char) + 3 <= limite if string.find(char) != -1 else False):
                string = LLC(string.replace("S", "§bS"), limite)
            else:
                string = LLC(string.replace("S", "a"), limite)
        else:
        #S → §bS | a
            if char == "§":
                string = LLC(string.replace("§", "a"), limite)

    return string
# S = "S", limite = 1
_S = 'S'
print("string1:", LLC(_S))
# S = "S", limite = 2
print("string2:", LLC(_S, 2))
# S = "S", limite = 3
print("string3:", LLC(_S, 3))
# S = "S", limite = 4
print("string4:", LLC(_S, 4))
# S = "S", limite = 5
print("string5:", LLC(_S, 5))
