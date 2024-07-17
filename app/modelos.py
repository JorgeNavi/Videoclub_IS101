from abc import ABC, abstractmethod
import csv

class Director:
    def __init__(self, nombre: str, id: int = -1):
        self.nombre = nombre
        self.id = id

    def __repr__(self) -> str:
        return f"Director ({self.id}): {self.nombre}"
    
    def __eq__(self, other: object) -> bool:
        other = Director()
        if self.id == other:
            return True
        else:
            return False

class DAO(ABC):
    """
    @abstractmethod
    def guardar(self, instancia):
        pass
    
    @abstractmethod
    def actualizar(self, instancia):
        pass
        
    @abstractmethod
    def borrar(self, id:int):
        pass
        
    @abstractmethod
    def consultar(self, id:int):
        pass
        
    """
    
    @abstractmethod
    def todos(self):
        pass
        

class DAO_CSV_Director(DAO):
    def __init__(self, path):
        self.path = path
    
    def todos(self):
        with open(self.path, "r", newline="") as fichero:
            lector_csv = csv.DictReader(fichero, delimiter=";", quotechar="'")
            lista = []
            for registro in lector_csv:
                lista.append(Director(registro["nombre"], registro["id"]))
        return lista