from abc import ABC
from typing import List,Any,Optional

class Persona(ABC):
    def __init__(self, nombre:str)->None:
        self._nombre= nombre

class Locutor(Persona):
    def __init__(self, nombre: str) ->None:
        super().__init__(nombre)
        self.__programas: List["Programa"]= []
    
    def add_programa(self, programa: "Programa") -> bool:
        self.__programas.append(programa)
        return True

class Invitado(Persona):
    def __init__(self, nombre: str)->None:
        super().__init__(nombre)
        self.__emisiones: List["Emision"] = []
    
    def add_emision(self, emision:"Emision")->bool:
        self.__emisiones.append(emision)
        return True

class Artista(Persona):
    def __init__(self, nombre:str)->None:
        super().__init__(nombre)
        self.__canciones: List["Cancion"]= []
    
    def add_cancion(self, cancion: "Cancion") ->bool:
        self.__canciones.append(cancion)