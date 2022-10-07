palabras_censuradas=["racismo", "terrorista", "peligro", "miedo", "odio"]

tweet = input("Ingrese el tweet: ")
caracter = input("Ingrese un caracter para reemplazar las palabras censuradas: ")

for palabra in palabras_censuradas: # recorro cada palabra de la lista de palabras que tengo que quitar del tweet
    tweet = tweet.replace(palabra, caracter * len(palabra)) # actualizo el tweet reemplazando la palabra con el caracter elegido repetido tantas veces como letras tenga la palabra (len me dice la longitud de la palabra, o sea, cuántas letras tiene. y el * lo uso para repetir el caracter)

print(tweet)