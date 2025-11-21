CREATE TABLE clientes (
  id_cliente SERIAL PRIMARY KEY,
  nombre VARCHAR(120),
  ruc VARCHAR(11),
  contacto_email VARCHAR(120),
  plan_suscripcion VARCHAR(50)
);

CREATE TABLE usuarios (
  id_usuario SERIAL PRIMARY KEY,
  id_cliente INT REFERENCES clientes(id_cliente),
  email VARCHAR(120),
  hash_password VARCHAR(200),
  rol VARCHAR(50)
);

CREATE TABLE eventos_logs (
  id_evento SERIAL PRIMARY KEY,
  id_cliente INT REFERENCES clientes(id_cliente),
  fuente VARCHAR(40),
  log_texto TEXT,
  severidad VARCHAR(20),
  timestamp TIMESTAMP
);

CREATE TABLE incidentes (
  id_incidente SERIAL PRIMARY KEY,
  id_cliente INT REFERENCES clientes(id_cliente),
  tipo VARCHAR(120),
  descripcion TEXT,
  estado VARCHAR(20),
  fecha_detectado TIMESTAMP,
  fecha_cerrado TIMESTAMP
);

CREATE TABLE reglas_correlacion (
  id_regla SERIAL PRIMARY KEY,
  nombre VARCHAR(120),
  condicion TEXT,
  severidad VARCHAR(20),
  activo BOOLEAN
);
