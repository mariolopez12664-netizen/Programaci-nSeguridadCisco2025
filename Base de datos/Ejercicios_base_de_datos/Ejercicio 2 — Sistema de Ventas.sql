CREATE DATABASE ventas;
USE ventas;

CREATE TABLE clientes (
    cliente_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    telefono VARCHAR(20)
);

CREATE TABLE productos (
    producto_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_producto VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT DEFAULT 0
);

CREATE TABLE facturas (
    factura_id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    cliente_id INT,
    producto_id INT,
    cantidad INT,
    total DECIMAL(10, 2),
    CONSTRAINT fk_cliente FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id),
    CONSTRAINT fk_producto FOREIGN KEY (producto_id) REFERENCES productos(producto_id)
);

INSERT INTO clientes (nombre, email, telefono) VALUES
('Ana García', 'ana@email.com', '555-1234'),
('Carlos López', 'carlos@email.com', '555-5678');

INSERT INTO productos (nombre_producto, precio, stock) VALUES
('Laptop', 850.00, 10),
('Mouse Inalámbrico', 25.00, 50),
('Monitor 24"', 150.00, 15);

INSERT INTO facturas (cliente_id, producto_id, cantidad, total) VALUES
(1, 1, 1, 850.00), -- Ana compró 1 Laptop
(1, 2, 2, 50.00),  -- Ana compró 2 Mouse
(2, 3, 1, 150.00); -- Carlos compró 1 Monitor

SELECT 
    f.factura_id, 
    c.nombre AS cliente, 
    p.nombre_producto, 
    f.cantidad, 
    f.total, 
    f.fecha
FROM facturas f
JOIN clientes c ON f.cliente_id = c.cliente_id
JOIN productos p ON f.producto_id = p.producto_id;

SELECT 
    c.nombre, 
    SUM(f.total) AS total_acumulado
FROM clientes c
JOIN facturas f ON c.cliente_id = f.cliente_id
GROUP BY c.nombre;

SELECT 
    c.nombre, 
    SUM(f.total) AS total_acumulado
FROM clientes c
JOIN facturas f ON c.cliente_id = f.cliente_id
GROUP BY c.nombre;

SELECT 
    p.nombre_producto, 
    SUM(f.cantidad) AS unidades_vendidas
FROM productos p
JOIN facturas f ON p.producto_id = f.producto_id
GROUP BY p.nombre_producto
ORDER BY unidades_vendidas DESC;