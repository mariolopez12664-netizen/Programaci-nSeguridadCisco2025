CREATE DATABASE colegio;
USE colegio;

CREATE TABLE estudiantes (
    estudiante_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    edad INT,
    email VARCHAR(100) UNIQUE
);

CREATE TABLE cursos (
    curso_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_curso VARCHAR(100) NOT NULL,
    descripcion TEXT,
    creditos INT
);

CREATE TABLE matriculas (
    matricula_id INT AUTO_INCREMENT PRIMARY KEY,
    estudiante_id INT,
    curso_id INT,
    fecha_inscripcion DATE DEFAULT (CURRENT_DATE),
    -- Relaciones
    CONSTRAINT fk_estudiante FOREIGN KEY (estudiante_id) 
        REFERENCES estudiantes(estudiante_id) ON DELETE CASCADE,
    CONSTRAINT fk_curso FOREIGN KEY (curso_id) 
        REFERENCES cursos(curso_id) ON DELETE CASCADE
);

INSERT INTO estudiantes (nombre, apellido, edad, email) VALUES
('Laura', 'Pérez', 20, 'laura@email.com'),
('Javier', 'Soto', 22, 'javier@email.com'),
('Marta', 'Ruiz', 19, 'marta@email.com');


INSERT INTO cursos (nombre_curso, creditos) VALUES
('Bases de Datos I', 5),
('Programación Web', 6),
('Matemáticas Discretas', 4);

INSERT INTO matriculas (estudiante_id, curso_id) VALUES
(1, 1), -- Laura en Bases de Datos
(1, 2), -- Laura en Programación Web
(2, 1), -- Javier en Bases de Datos
(3, 3); -- Marta en Matemáticas

SELECT 
    e.nombre, 
    e.apellido, 
    c.nombre_curso
FROM estudiantes e
JOIN matriculas m ON e.estudiante_id = m.estudiante_id
JOIN cursos c ON m.curso_id = c.curso_id;

SELECT 
    c.nombre_curso, 
    COUNT(m.estudiante_id) AS total_alumnos
FROM cursos c
LEFT JOIN matriculas m ON c.curso_id = m.curso_id
GROUP BY c.nombre_curso;

SELECT c.nombre_curso
FROM cursos c
JOIN matriculas m ON c.curso_id = m.curso_id
WHERE m.estudiante_id = 1; -- Cursos de Laura