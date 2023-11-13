from abc import ABC
from typing import List,Any,Optional
from Person import Locutor

class Programa:
    def __init__(self, nombre:str, locutores: "Locutor") -> None:
        self.__nombre= nombre
        self.__serial:int=None
        self.__emisiones: List["Emision"]=[]
        self.__locutores: List["Locutor"]= [locutores]
        self.__locutores[0].add_programa(self)
    
    @property
    def name(self)-> str:
        return self.__nombre
    
    def add_emision(self, emision:"Emision") ->bool:
        self.__emisiones.append(emision)
        return True
    
    def add_locutor(self, locutor:"Locutor") ->bool:
        self.__locutores.append(locutor)
        locutor.add_programa(self)
        return True
    
    def get_emision(self) -> List["Emision"]:
        return self.__emisiones

    def get_last_emision(self)-> "Emision":
        return self.__emisiones[-1]
        
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
    
    def get_cancion(self)->List["Cancion"]:
        return self.__canciones