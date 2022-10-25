/*
   Si no tienes una base de datos, copia las siguientes dos líneas que no están comentadas
*/
CREATE DATABASE IF NOT EXISTS pruebas;
USE pruebas;

/*
   Si ya tienes una base de datos, sólo copia lo siguiente
*/
CREATE TABLE tblUsuarios (
   idx INT PRIMARY KEY AUTO_INCREMENT,
   usuario VARCHAR(20),
   nombre VARCHAR(20),
   sexo VARCHAR(1),
   nivel TINYINT,
   email VARCHAR(50),
   telefono VARCHAR(20),
   marca VARCHAR(20),
   compañia VARCHAR(20),
   saldo FLOAT,
   activo BOOLEAN
);

INSERT INTO tblUsuarios 
VALUES 
('1','BRE2271','BRENDA','M','2','brenda@live.com','655-330-5736','SAMSUNG','IUSACELL','100','1'),
('2','OSC4677','OSCAR','H','3','oscar@gmail.com','655-143-4181','LG','TELCEL','0','1'),
('3','JOS7086','JOSE','H','3','francisco@gmail.com','655-143-3922','NOKIA','MOVISTAR','150','1'),
('4','LUI6115','LUIS','H','0','enrique@outlook.com','655-137-1279','SAMSUNG','TELCEL','50','1'),
('5','LUI7072','LUIS','H','1','luis@hotmail.com','655-100-8260','NOKIA','IUSACELL','50','0'),
('6','DAN2832','DANIEL','H','0','daniel@outlook.com','655-145-2586','SONY','UNEFON','100','1'),
('7','JAQ5351','JAQUELINE','M','0','jaqueline@outlook.com','655-330-5514','BLACKBERRY','AXEL','0','1'),
('8','ROM6520','ROMAN','H','2','roman@gmail.com','655-330-3263','LG','IUSACELL','50','1'),
('9','BLA9739','BLAS','H','0','blas@hotmail.com','655-330-3871','LG','UNEFON','100','1'),
('10','JES4752','JESSICA','M','1','jessica@hotmail.com','655-143-6861','SAMSUNG','TELCEL','500','1'),
('11','DIA6570','DIANA','M','1','diana@live.com','655-143-3952','SONY','UNEFON','100','0'),
('12','RIC8283','RICARDO','H','2','ricardo@hotmail.com','655-145-6049','MOTOROLA','IUSACELL','150','1'),
('13','VAL6882','VALENTINA','M','0','valentina@live.com','655-137-4253','BLACKBERRY','AT&T','50','0'),
('14','BRE8106','BRENDA','M','3','brenda2@gmail.com','655-100-1351','MOTOROLA','NEXTEL','150','1'),
('15','LUC4982','LUCIA','M','3','lucia@gmail.com','655-145-4992','BLACKBERRY','IUSACELL','0','1'),
('16','JUA2337','JUAN','H','0','juan@outlook.com','655-100-6517','SAMSUNG','AXEL','0','0'),
('17','ELP2984','ELPIDIO','H','1','elpidio@outlook.com','655-145-9938','MOTOROLA','MOVISTAR','500','1'),
('18','JES9640','JESSICA','M','3','jessica2@live.com','655-330-5143','SONY','IUSACELL','200','1'),
('19','LET4015','LETICIA','M','2','leticia@yahoo.com','655-143-4019','BLACKBERRY','UNEFON','100','1'),
('20','LUI1076','LUIS','H','3','luis2@live.com','655-100-5085','SONY','UNEFON','150','1'),
('21','HUG5441','HUGO','H','2','hugo@live.com','655-137-3935','MOTOROLA','AT&T','500','1');

SELECT * FROM tblUsuarios;

SELECT nombre AS "Nombre De Usuarios" FROM tblUsuarios;

SELECT max(saldo) AS "saldo de mujeres" FROM tblUsuarios WHERE sexo = "M";

SELECT nombre, telefono, marca FROM tblusuarios WHERE marca = "NOKIA" OR marca = "BLACKBERRY" OR marca ="SONY"; 
SELECT nombre, telefono, marca FROM tblUsuarios WHERE marca IN ("NOKIA", "BLACKBERRY", "SONY");

#Contar los usuarios sin saldo o inactivos
SELECT COUNT(usuario) AS "usuarios sin saldo o inactivos" FROM tblusuarios WHERE saldo = 0 or activo = 0;

#Listar el login de los usuarios con nivel 1, 2 o 3
SELECT usuario AS "Login", nivel AS "usuarios nivel 1, 2 y 3" FROM tblUsuarios WHERE nivel IN(1, 2, 3) ORDER BY nivel;

#Listar los números de teléfono con saldo menor o igual a 300
SELECT telefono, saldo FROM tblusuarios WHERE saldo <= 300 ORDER BY saldo DESC;

#Calcular la suma de los saldos de los usuarios de la compañia telefónica NEXTEL
SELECT SUM(saldo) AS "cantidad de saldo de los usuarios de la compañia NEXTEL" FROM tblusuarios WHERE compañia = "NEXTEL";

#Contar el número de usuarios por compañía telefónica
SELECT  compañia, count(usuario) AS " cantidad de usuarios por compañia" FROM tblusuarios GROUP BY compañia;

#Contar el número de usuarios por nivel
SELECT  nivel, count(usuario) AS " cantidad de usuarios por nivel" FROM tblusuarios GROUP BY nivel ORDER BY nivel;

#Listar el login de los usuarios con nivel 2 solo imprimir lo que se pedi
SELECT usuario AS "login de usuarios con nivel 2" FROM tblUsuarios WHERE nivel = 2;

#Mostrar el email de los usuarios que usan gmail se recomienta listar la entidad con limit por temas de memoria
SELECT email FROM tblusuarios WHERE email LIKE "%gmail.%"; 

# Listar nombre y teléfono de los usuarios con teléfono que no sea de la marca LG o SAMSUNG
SELECT nombre, telefono, FROM tblusuarios WHERE marca != "LG" AND marca != "SAMSUNG";
SELECT nombre, telefono,  FROM tblusuarios WHERE marca NOT in( "LG","SAMSUNG");

# Listar el login y teléfono de los usuarios con compañia telefónica IUSACELL
SELECT usuario, telefono, FROM tblusuarios WHERE compañia = "IUSACELL";

# Listar el login y teléfono de los usuarios con compañia telefónica que no sea TELCEL
SELECT usuario, telefono, FROM tblusuarios WHERE compañia != "TELCEL";

# Calcular el saldo promedio de los usuarios que tienen teléfono marca NOKIA
SELECT AVG(SALDO) FROM tblusuarios WHERE marca = "NOKIA";
SELECT sum(saldo), COUNT(USUARIO) FROM tblusuarioS WHERE marca = "NOKIA";

# Listar el login y teléfono de los usuarios con compañia telefónica IUSACELL o AXEL
SELECT usuario, telefono FROM tblusuarios WHERE compañia IN ("IUSACELL", "AXEL");

# Mostrar el email de los usuarios que no usan yahoo
SELECT EMAIL FROM tblusuarios WHERE EMAIL NOT LIKE "%YAHOO.%";

# Listar el login y teléfono de los usuarios con compañia telefónica que no sea TELCEL o IUSACELL
SELECT USUARIO, TELEFONO FROM tblusuarios WHERE COMPAÑIA NOT IN("TELCEL", "IUSACELL");

# Listar el login y teléfono de los usuarios con compañia telefónica UNEFON
SELECT USUARIO, TELEFONO FROM tblusuarios WHERE COMPAÑIA = "unefon";

# Listar las diferentes marcas de celular en orden alfabético descendentemente
SELECT DISTINCT MARCA FROM tblusuarios ORDER BY MARCA DESC;

# Listar las diferentes compañias en orden alfabético aleatorio
SELECT COMPAÑIA AS "lISTADO DE COMPAÑIAS EN ORDEN ALEATORIO" FROM tblusuarios ORDER BY RAND();

# Listar el login de los usuarios con nivel 0 o 2
SELECT USUARIO FROM tblusuarios WHERE NIVEL IN(0, 2);

# Calcular el saldo promedio de los usuarios que tienen teléfono marca LG
SELECT AVG(SALDO) AS "PROMEDIO DE SALDO DE USUARIOS CON TELEFONOS LG" FROM tblusuarios WHERE MARCA = "LG";

# Listar el login de los usuarios con nivel 1 o 3
SELECT USUARIO AS "LOGIN DE USUARIOS CON NIVEL 1 O 3" FROM tblusuarios WHERE NIVEL IN(1, 3);










