-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS baseds;
USE baseds;

-- Crear la tabla "usuarios"
CREATE TABLE IF NOT EXISTS usuarios (
  CODIGO VARCHAR(10) PRIMARY KEY,
  ALIAS VARCHAR(50),
  CLAVE VARCHAR(50),
  NOMBRE VARCHAR(100),
  ACCESO INT
);

-- Insertar los registros del CSV
INSERT INTO usuarios (CODIGO, ALIAS, CLAVE, NOMBRE, ACCESO) VALUES
('u20', 'pepe', '123456', 'Jose Duarte', 1),
('u21', 'lsanchez', 'lu444', 'Luis Sanchez', 2),
('u22', 'rolo21', 'rtjui', 'Rolando Trujillo', 1),
('u23', 'gmarquez', 'goyo22', 'Gabriel Terrones', 1),
('u24', 'tluis', 'lucho40', 'Tomas Tafur', 1),
('u25', 'mgarcia', 'mkkk35', 'Miriam Garcia', 2);
