from abc import ABC
from typing import List,Any,Optional
from Person import Locutor

class Programa:
    def __init__(self, nombre:str, locutores: List["Locutor"]) -> None:
        self.__nombre= nombre
        self.__serial:int=None
        self.__emisiones: List["Emision"]=[]
        self.__locutores= locutores
        for locutor in self.__locutores:
            locutor.add_programa(self)
    
    def add_emision(self, emision:"Emision") ->bool:
        self.__emisiones.append(emision)
        return True
    
    def add_locutor(self, locutor:"Locutor") ->bool:
        self.__locutores.append(locutor)
        locutor.add_programa(self)
        return True

class Emision:
    def __init__(self, programa:"Programa")-> None:
        self.__serial:int = None
        self.__canciones: List["Cancion"]=[]
        self.__invitados: List["Invitado"]=[]
        self.__programa= programa
        programa.add_emision(self)
    
    def get_programa(self) -> "Programa":
        return self.__programa
    
    def add_cancion(self, cancion:"Cancion")->bool:
        self.__canciones.append(cancion)
        return True
    
    def add_invitado(self, invitado:"Invitado")->bool:
        self.__invitados.append(invitado)
        return True