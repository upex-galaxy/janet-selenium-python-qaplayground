from dataclasses import dataclass
from typing import Literal

@dataclass
class Perro: 
    #parametos de tipado -- parameter
    name: str
    has_chip: bool
    raza:str = "poodel"
    
    #constructor,propiedades exclusivas de la clase, localizadores
    def __post_init__(self):
        self.nombre_completo = self.name + " nutella"
        self.raza_comercial = self.raza + " trucha"
        self.alimentacion = "perrarina" + self.name
        self.puede_viajar = self.has_chip and self.raza=="poodel"
    
    #metodos,las interacciones del objeto de la clase. capacidades
    def comer(self):
        if self.has_chip:
            print("Come poquito")
        else:
            print("Come mucho")
    
    def jugar(self,rabia: bool,con: Literal["la pelota","la banbalina","los ninos","los zapatos"]):
        if rabia:
            print(f"Esta destrozando {con}")
        else:
            print(f"Esta jugando con {con}")
        
        
                    
                    
        
        
#Inicializacion
"""perro_1 = Perro(name= "Carlos", has_chip= True, raza= "dragon")
print(perro_1)
data={
    "name_full": perro_1.nombre_completo,
    "raza_comercial": perro_1.raza_comercial,
    "alimentacion": perro_1.alimentacion,
    "puede_viajar": perro_1.puede_viajar
 }
print(data)"""
"""perro_2 = Perro(name="Doki", has_chip=False,raza="caniche")
print(perro_2.)"""

perro_1 = Perro(name= "Carlos", has_chip= True)
data={ 
    "name_full": perro_1.nombre_completo,
    "raza_comercial": perro_1.raza_comercial,
    "alimentacion": perro_1.alimentacion,
    "puede_viajar": perro_1.puede_viajar
 }
perro_1.comer()
perro_1.jugar(con="los ninos",rabia=False)
