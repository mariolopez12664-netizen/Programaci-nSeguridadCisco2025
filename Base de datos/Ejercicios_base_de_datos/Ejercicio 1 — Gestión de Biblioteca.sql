CREATE DATABASE biblioteca;
USE biblioteca;

CREATE TABLE autores (
    autor_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    nacionalidad VARCHAR(50),
    fecha_nacimiento DATE
);

CREATE TABLE libros (
    libro_id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    anio_publicacion INT,
    autor_id INT,
    -- Definición de la Clave Foránea
    CONSTRAINT fk_autor 
        FOREIGN KEY (autor_id) 
        REFERENCES autores(autor_id)
        ON DELETE CASCADE
);


INSERT INTO autores (nombre, nacionalidad, fecha_nacimiento) VALUES
('Gabriel García Márquez', 'Colombiana', '1927-03-06'),
('Isabel Allende', 'Chilena', '1942-08-02'),
('George Orwell', 'Británica', '1903-06-25');


INSERT INTO libros (titulo, anio_publicacion, autor_id) VALUES
('Cien años de soledad', 1967, 1),
('El amor en los tiempos del cólera', 1985, 1),
('La casa de los espíritus', 1982, 2),
('1984', 1949, 3),
('Rebelión en la granja', 1945, 3);

SELECT l.titulo, l.anio_publicacion, a.nombre AS autor
FROM libros l
JOIN autores a ON l.autor_id = a.autor_id;

SELECT titulo FROM libros 
WHERE autor_id = 1; -- Filtra por Gabriel García Márquez

SELECT a.nombre, COUNT(l.libro_id) AS total_libros
FROM autores a
LEFT JOIN libros l ON a.autor_id = l.autor_id
GROUP BY a.nombre;


