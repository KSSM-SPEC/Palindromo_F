def es_palindromo(texto):
    # Normalizamos el texto: quitamos espacios y pasamos a minúsculas
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]

# Programa principal
palabra = input("Ingresa una palabra o frase: ")
if es_palindromo(palabra):
    print("✅ Es un palíndromo")
else:
    print("❌ No es un palíndromo")