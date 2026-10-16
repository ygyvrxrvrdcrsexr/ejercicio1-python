meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "PAPEAR": "es ganar a una persona en una discusion",
            "momos": "es una forma de llamar un chiste o una broma",
            "prime": "es el mejor momento de una persona",
            "funar": "denunciar o exponer a una persona en redes sociales",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("revisa tu palabra")

    
