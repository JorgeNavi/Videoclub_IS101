from abc import ABC, abstractmethod
import csv

class Model(ABC):
    
    @classmethod
    @abstractmethod
    def create_from_dict(cls, diccionario):#cls es la forma estandar de poner la propia clase en el metodo de clase. los metodos de instancia llevan self, y los metodos de clase llevan cls
        pass


class Director(Model):
    def __init__(self, nombre: str, id: int = -1):
        self.nombre = nombre
        self.id = id

    @classmethod
    def create_from_dict(cls, diccionario):#cls es la forma estandar de poner la propia clase en el metodo de clase. los metodos de instancia llevan self, y los metodos de clase llevan cls
        return cls(diccionario["nombre"], int(diccionario["id"]))

    def __repr__(self) -> str:
        return f"Director ({self.id}): {self.nombre}"
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self.id == other.id and self.nombre == other.nombre
        return False
    
    def __hash__(self):
        return hash((self.id, self.nombre))
    

class Pelicula(Model):
    def __init__(self, titulo: str, genero: object, sinopsis: str, director: object, id: int = -1):
        self.titulo = titulo
        self.sinopsis = sinopsis
        self.id = id
        self.director = director
        self.genero = genero
        self.num_copias = 0

    @classmethod
    def create_from_dict(cls, diccionario):
        return cls(diccionario["titulo"], diccionario["sinopsis"],
                                      int(diccionario["director_id"]), int(diccionario["id"]))


    def __repr__(self) -> str:
        return f"Pelicula ({self.id}: {self.titulo}, {self.director})"
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self.id == other.id and self.titulo == other.titulo and self.sinopsis == other.sinopsis and self.director == other.director
        return False
    
    def __hash__(self):
        return hash((self.id, self.titulo, self.sinopsis, self.director))

    @property    
    def director(self):
        return self._director
    
    @director.setter
    def director(self, value):
        if isinstance(value, Director):
            self._director = value
            self._id_director = value.id
        elif isinstance(value, int):
            self._director = None
            self._id_director = value
        else:
            raise TypeError(f"{value} debe ser un entero o instancia de Director")
        
    def añadir_copia(self, n: int):
        copia = Copia(n)
        self.num_copias += copia.num_copias
        return self.num_copias

        

class Genero(Model):

    def __init__(self, tipo: str):
        self.tipo = tipo

    @classmethod
    def create_from_dict(cls, diccionario):
        return cls(diccionario["genero"])

    def __repr__(self) -> str:
        return f"Genero: {self.tipo}"
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self.tipo == other.tipo
        return False
    
    def __hash__(self):
        return hash(self.tipo)
    
class Copia(Model):

    def __init__(self, num_copias: int):
        self.num_copias = num_copias

    @classmethod
    def create_from_dict(cls, diccionario):
        return cls(int(diccionario["num_copias"]))

    def __repr__(self) -> str:
        return f"num_copias: {self.num_copias}"
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self.num_copias == other.num_copias
        return False
    
    def __hash__(self):
        return hash(self.num_copias)




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

class DAO_CSV(DAO):
    model = None

    def __init__(self, path):
        self.path = path
        
    def todos(self):
        with open(self.path, "r", newline="", encoding="utf-8") as fichero: #el encoding sirve para adaptar el tipo de texto que lee el pc para que no haya conflictos a la hora de traducir en texto
            lector_csv = csv.DictReader(fichero, delimiter=";", quotechar="'")
            lista = []
            for registro in lector_csv:
                lista.append(self.model.create_from_dict(registro))
        return lista

class DAO_CSV_Director(DAO_CSV):
    model = Director
    
class DAO_CSV_Pelicula(DAO_CSV):
    model = Pelicula

class DAO_CSV_Genero(DAO_CSV):
    model = Genero

class DAO_CSV_Copia(DAO_CSV):
    model = Copia