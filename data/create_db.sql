CREATE TABLE IF NOT EXISTS"directores" (
	"Id"	INTEGER,
	"nombre"	TEXT NOT NULL,
	"url_foto"	TEXT,
	"url_web"	TEXT,
	PRIMARY KEY("Id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "peliculas" (
	"id"	INTEGER,
	"titulo"	TEXT NOT NULL,
	"id_director"	INTEGER NOT NULL,
	"anyo"	INTEGER NOT NULL,
	"url_caratula"	TEXT,
	"id_generos"	INTEGER,
	"es_animacion"	INTEGER NOT NULL,
	FOREIGN KEY("id_director") REFERENCES "directores"("Id"),
	PRIMARY KEY("id" AUTOINCREMENT)
)