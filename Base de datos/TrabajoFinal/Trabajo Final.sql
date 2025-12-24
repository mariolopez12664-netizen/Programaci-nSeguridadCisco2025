CREATE DATABASE gestion_academica;
USE gestion_academica;

CREATE TABLE departamento (
    id_departamento INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE estudiante (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    fecha_nacimiento DATE,
    id_departamento INT,
    FOREIGN KEY (id_departamento) REFERENCES departamento(id_departamento)
);

CREATE TABLE profesor (
    id_profesor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    id_departamento INT,
    FOREIGN KEY (id_departamento) REFERENCES departamento(id_departamento)
);

CREATE TABLE curso (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    creditos INT,
    id_departamento INT,
    FOREIGN KEY (id_departamento) REFERENCES departamento(id_departamento)
);

CREATE TABLE clase (
    id_clase INT AUTO_INCREMENT PRIMARY KEY,
    id_curso INT,
    id_profesor INT,
    horario VARCHAR(50),
    FOREIGN KEY (id_curso) REFERENCES curso(id_curso),
    FOREIGN KEY (id_profesor) REFERENCES profesor(id_profesor)
);

CREATE TABLE inscripcion (
    id_inscripcion INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT,
    id_clase INT,
    fecha DATE,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante),
    FOREIGN KEY (id_clase) REFERENCES clase(id_clase)
);

CREATE TABLE calificacion (
    id_calificacion INT AUTO_INCREMENT PRIMARY KEY,
    id_inscripcion INT,
    nota DECIMAL(5,2),
    FOREIGN KEY (id_inscripcion) REFERENCES inscripcion(id_inscripcion)
);

INSERT INTO departamento (nombre) VALUES
('Informática'),
('Educación'),
('Matemáticas');

INSERT INTO estudiante (nombre, apellido, fecha_nacimiento, id_departamento) VALUES
('Ana','Pérez','2001-03-15',1),
('Luis','Gómez','2000-07-10',1),
('María','Rodríguez','2002-01-20',2);

INSERT INTO profesor (nombre, apellido, id_departamento) VALUES
('Carlos','López',1),
('Juana','Martínez',2);

INSERT INTO curso (nombre, creditos, id_departamento) VALUES
('Base de Datos',4,1),
('Didáctica',3,2);

INSERT INTO clase (id_curso, id_profesor, horario) VALUES
(1,1,'Lunes 8-10'),
(2,2,'Martes 2-4');

INSERT INTO inscripcion (id_estudiante, id_clase, fecha) VALUES
(1,1,'2025-01-10'),
(2,1,'2025-01-10'),
(3,2,'2025-01-11');

INSERT INTO calificacion (id_inscripcion, nota) VALUES
(1,90),
(2,85),
(3,95);

SELECT * FROM estudiante;

SELECT nombre, apellido FROM estudiante;

SELECT * FROM estudiante
WHERE id_departamento = 1;

SELECT * FROM estudiante
ORDER BY fecha_nacimiento ASC;


SELECT e.nombre, e.apellido, d.nombre AS departamento
FROM estudiante e
JOIN departamento d ON e.id_departamento = d.id_departamento;

SELECT e.nombre, c.nombre AS curso, cal.nota
FROM estudiante e
JOIN inscripcion i ON e.id_estudiante = i.id_estudiante
JOIN calificacion cal ON i.id_inscripcion = cal.id_inscripcion
JOIN clase cl ON i.id_clase = cl.id_clase
JOIN curso c ON cl.id_curso = c.id_curso;

SELECT AVG(nota) AS promedio_general FROM calificacion;

SELECT MAX(nota) AS nota_maxima FROM calificacion;

SELECT MIN(nota) AS nota_minima FROM calificacion;

SELECT COUNT(*) AS total_estudiantes FROM estudiante;

UPDATE estudiante
SET apellido = 'González'
WHERE id_estudiante = 1;

DELETE FROM calificacion
WHERE id_calificacion = 2;



