from app.modelos import Director, DAO_CSV_Director, Pelicula, DAO_CSV_Pelicula, Genero, DAO_CSV_Genero, Copia, DAO_CSV_Copia, DAO_SQLite_Director

def test_create_director():
    director = Director("Robert Redford")

    assert director.nombre == "Robert Redford"
    assert director.id == -1

def test_dao_directores_traer_todos():
    dao = DAO_CSV_Director("tests/data/directores_prueba.csv")
    directores = dao.todos()

    assert len(directores) == 8
    assert directores[7] == Director("Charlie Chaplin", 8)

def test_create_película():
    pelicula = Pelicula("El señor de los anillos", "Fantasia epica", "Sauron es mu malo",  9)

    assert pelicula.titulo == "El señor de los anillos"
    assert pelicula.sinopsis == "Sauron es mu malo"
    assert pelicula._id_director == 9
    assert pelicula.id == -1
    assert pelicula._director is None
    assert pelicula.genero == "Fantasia epica"

def test_create_pelicula_and_informar_director_completo():
    director = Director("Peter Jackson", 9)
    pelicula = Pelicula("El señor de los anillos", "Fantasia epica", "Sauron es mu malo", director)

    assert pelicula.titulo == "El señor de los anillos"
    assert pelicula.sinopsis == "Sauron es mu malo"
    assert pelicula._id_director == 9
    assert pelicula.id == -1
    assert pelicula._director == director
    assert pelicula.genero == "Fantasia epica"

def test_asigna_director_a_pelicula():
    pelicula = Pelicula("El señor de los anillos", "Fantasia epica", "Sauron es mu malo", -1)

    director = Director("Peter Jackson", 9)

    pelicula.director = director

    assert pelicula.titulo == "El señor de los anillos"
    assert pelicula.sinopsis == "Sauron es mu malo"
    assert pelicula._id_director == 9
    assert pelicula.id == -1
    assert pelicula._director == director
    assert pelicula.genero == "Fantasia epica"

def test_dao_peliculas_traer_todos():
    dao = DAO_CSV_Pelicula("tests/data/peliculas_prueba.csv")
    peliculas = dao.todos()

    assert len(peliculas) == 5
    assert peliculas[1] == Pelicula("Los siete samuráis","Una banda de forajidos atemorizan a los habitantes de un pequeño pueblo, saqueándolos periódicamente sin piedad. Para repeler estos ataques, los aldeanos deciden contratar a mercenarios. Finalmente, consiguen los servicios de 7 guerreros, 7 samurais dispuestos a defenderlos a cambio, tan solo, de cobijo y comida.", 2, 17)

def test_create_genero():
    
    genero = Genero("drama")

    assert genero.tipo == "drama"

def test_create_pelicula_e_informar_genero():
    genero = Genero("Fantasia epica")
    director = Director("Peter Jackson", 9)
    
    pelicula = Pelicula("El señor de los anillos", genero, "Sauron es mu malo", director)

    pelicula.director = director
    pelicula.genero = genero

    assert pelicula.titulo == "El señor de los anillos"
    assert pelicula.sinopsis == "Sauron es mu malo"
    assert pelicula._id_director == 9
    assert pelicula.id == -1
    assert pelicula._director == director
    assert pelicula.genero == genero

def test_DAO_generos_traer_todos():
    dao = DAO_CSV_Genero("tests/data/generos_prueba.csv")
    generos = dao.todos()

    assert len(generos) == 8
    assert generos[3] == Genero("Drama")


def test_create_copia():
    
    copias = Copia(15)
    
    assert copias.num_copias == 15

def test_añadir_copia():
    pelicula = Pelicula("El señor de los anillos", "Fantasia epica", "Sauron es mu malo",  9)
    pelicula.añadir_copia(15)
    assert pelicula.num_copias == 15

def test_DAO_copias_traer_todos():
    dao = DAO_CSV_Copia("tests/data/num_copias_prueba.csv")
    copia = Copia(5)
    copias = dao.todos()
    assert len(copias) == 5
    assert copias[3] == copia

def test_DAO_directores_sqlite_traer_todos():
    dao = DAO_SQLite_Director("data/films.sqlite")
    directores = dao.todos()

    assert len(directores) == 76
    assert directores[7] == Director("Charlie Chaplin", 8)
