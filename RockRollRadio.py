from typing import List,Any,Optional

class RockRollRadio:
    def __init__(self) -> None:
        self.__artistas: List["Artista"] = []
        self.__canciones: List["Cancion"] = []
        self.__invitados: List["Invitado"] = []
        self.__locutores: List["Locutor"] = []
        self.__programas: List["Programa"] = []
    
    @property
    def locutores(self)-> List["Locutor"]:
        return self.__locutores
    
    @property
    def artistas(self)-> List["Artistas"]:
        return self.__artistas
    
    @property
    def programas(self)-> List["Programa"]:
        return self.__programas
    
    @property
    def canciones(self)-> List["Cancion"]:
        return self.__canciones
    
    def add_locutor(self,locutor:"Locutor")->None:
        self.__locutores.append(locutor)
    
    def add_programa(self, programa:"Programa")->None:
        self.__programas.append(programa)
    
    def add_artista(self,artista:"Artista")->None:
        self.__artistas.append(artista)
    
    def add_cancion(self,cancion:"Cancion")->None:
        self.__canciones.append(cancion)

    def add_emision(self,emision:"Emision")->None:
        emision.get_programa().add_emision(emision)

    def add_invitado(self,invitado:"Invitados", emision:"Emision")->None:
        self.__invitados.append(invitado)
        invitado.add_emision(emision)
        emision.add_invitado(invitado)
    
    def get_programa_con_mas_canciones_de_artista(self, artista:"Artista")->"Programa":
        aux_programa = None
        max_contador = 0

        for programa in self.__programas:
            contador = 0

            for emision in programa.get_emision():
                for cancion in emision.get_cancion():
                    if artista == cancion.get_artista():
                        contador += 1

    # Verificar si este programa tiene más canciones del artista que el máximo anterior
            if contador > max_contador:
                max_contador = contador
                aux_programa = programa

# Devolver el programa con más canciones del artista
        return aux_programa

            
    

    
    