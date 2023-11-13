from Person import Artista

class Genero:
   ROCK = "ROCK"
   CLASICA = "CLASICA"
   TROPICAL = "TROPICAL"

class Cancion:
    def __init__(self,nombre:str, artista:"Artista",genero:str) -> None:
        self.__nombre = nombre
        self.__artista = artista
        self.__genero = genero
    
    def get_artista(self)->"Artista":
        return self.__artista

        