CREATE DATABASE banco;
USE DATABASE banco;

CREATE TABLE album (
    ID SERIAL PRIMARY KEY
    name VARCHAR (64) NOT NULL
    name_banda VARCHAR (64) NOT NULL
    release_year VARCHAR (4)
);

CREATE TABLE musica (
    ID SERIAL PRIMARY KEY
    name VARCHAR (64) NOT NULL
    album_musica VARCHAR (64) NOT NULL

    CONSTRAINT FOREIGN KEY (album_musica)
        REFERENCES album (name)
);

INSERT INTO album (name, name_banda, release_year) VALUES ("Walk","Foo Fighters", "2011");
INSERT INTO album (name, name_banda, release_year) VALUES ("Dark Horse","Nickelback", "2008");
INSERT INTO album (name, name_banda, release_year) VALUES ("Cut the Cord","Shinedown", "2015");

INSERT INTO musica (name, album_musica) VALUES ("Walk","Walk");
INSERT INTO musica (name, album_musica) VALUES ("Monsters","ATTENTION ATTENTION");
INSERT INTO musica (name, album_musica) VALUES ("Enemies","Amaryllis");
INSERT INTO musica (name, album_musica) VALUES ("If Today Was Your Last Day","Dark Horse");
INSERT INTO musica (name, album_musica) VALUES ("How You Remind Me","Silver Side Up");
INSERT INTO musica (name, album_musica) VALUES ("Big Me","Foo Fighters");

SELECT name, release_year from musica
INNER JOIN album
on album.name = musica.album_musica;

SELECT name, release_year from musica
LEFT JOIN album
on album.name = musica.album_musica;