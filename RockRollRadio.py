

class RockRollRadio:
    def __init__(self) -> None:
        self.__artistas: list["Artista"] = []
        self.__canciones: list["cancion"] = []
        self.__invitados: list["Invitado"] = []
        self.__locutores: list["Locutor"] = []
        self.__programas: list["Programa"] = []
    
    def add_locutor(self,locutor:Locutor)->None:
        self.__locutores.append(locutor)
    
    def add_programa(self, programa:Programa, locutor:Locutor)->None:
        self.__programas.append(programa)
        programa.add_locutor(locutor)
    
    def add_artista(self,artista:Artista)->None:
        self.__artistas.append(artista)
    
    def add_cancion(self,cancion:Cancion, artista:Artista, genero:str)->None:
        self.__canciones.append(cancion)
        artista.add_cancion(cancion)

    def add_emision(self,emision:Emision)->None:
        emision.get_programa().add_emision(emision)

    def add_invitados(self,invitado:Invitados, emision:Emision)->None:
        self.__invitados.append(invitado)
        invitado.add_emision(emision)
        emision.add_invitado(invitado)
    
    def get_programa_con_mas_canciones_de_artista(self, artista:Artista)->"Programa":
        aux_artista = None
        for programa in self.__programas:
            contador = 0
            max = 0
            for emision in programa.get_emision():
                for art in self.__artistas:
                    for cancion in emision.get_cancion():
                        if art == cancion.get_artista():
                            contador = contador + 1
                    if contador > max:
                        max = contador
                        aux_artista = art
            
            if aux_artista == artista:
                return programa

            
    

    
    