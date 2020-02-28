# Lendo os números como entrada

# A função input sempre retorna o valor digitado como uma cadeia de caracteres (texto).
# Isso faz sentido, porque o usuário pode inserir qualquer valor que desejar.

x = input("Digite um número: ")
print(type(x))

x = int(input("Digite um número: "))
print(x)