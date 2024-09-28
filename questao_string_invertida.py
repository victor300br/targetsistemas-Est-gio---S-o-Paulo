entrada = "Exemplo de string"
string_invertida = ""

for i in range(len(entrada) - 1, -1, -1):
    string_invertida += entrada[i]

print(string_invertida)
