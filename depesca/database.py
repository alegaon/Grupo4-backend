import os
import psycopg2
from flask import g
from dotenv import load_dotenv

# Cargo las variables de entorno provenientes del archivo .env
load_dotenv()


# Configuro la base de datos, partiendo de las variables de entorno cargadas en el sistema
DATABASE_CONFIG = {
    'user': os.getenv('PGSQL_USERNAME'),
    'password': os.getenv('PGSQL_PASSWORD'),
    'host': os.getenv('PGSQL_HOST'),
    'database': os.getenv('PGSQL_DATABASE'),
    'port': os.getenv('PGSQL_PORT'),
}


def test_conn():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()
    conn.commit()
    cur.close()
    conn.close()


def create_articulos():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS public.articulos
        (
            id SERIAL PRIMARY KEY,
            img_portada character varying,
            titulo character varying COLLATE pg_catalog."default" NOT NULL,
            descripcion text COLLATE pg_catalog."default" NOT NULL,
            comida boolean NOT NULL,
            embarcacion boolean NOT NULL,
            guia boolean NOT NULL,
            equipos boolean NOT NULL,
            carnada boolean NOT NULL,
            wifi boolean NOT NULL,
            hospedaje boolean NOT NULL,
            atencion boolean NOT NULL,
            salvavidas boolean NOT NULL,
            info_descripcion text COLLATE pg_catalog."default" NOT NULL,
            info_ubicacion character varying COLLATE pg_catalog."default" NOT NULL,
            info_img_principal character varying,
            info_img_descripcion character varying,
            inf_img_1 character varying,
            inf_img_2 character varying,
            inf_img_3 character varying,
            inf_img_4 character varying,
            info_provincia character varying COLLATE pg_catalog."default",
            info_ciudad character varying COLLATE pg_catalog."default",
            info_mapa character varying COLLATE pg_catalog."default",
            info_direccion character varying COLLATE pg_catalog."default",
            info_telefono character varying COLLATE pg_catalog."default",
            info_sitio character varying COLLATE pg_catalog."default",
            activo boolean NOT NULL,
            creado TIMESTAMPTZ DEFAULT NOW() NOT NULL,
            actualizado TIMESTAMPTZ DEFAULT NOW() NOT NULL
        )
        """
    )
    conn.commit()

    cur.close()
    print('Tabla Articulos Creada')

# Funcion para estableer la conexion a la BD


def get_db():
    # Si 'db' no esta en el contexto global de Flas "g"
    if 'db' not in g:
        # Establezco una nueva conexion a la BD y la guardo en 'g'
        g.db = psycopg2.connect(**DATABASE_CONFIG)
    # Retorno la conexion a la base de datos
    return g.db

# Funcion para cerrar la conexion a la BD


def close_db(e=None):
    # Elimino de "g" la conexion a la BD
    db = g.pop('db', None)
    # Si la conexion existe, la cierro
    if db is not None:
        db.close()

# Funcion para inicializar la aplicacion con el manejo de base de datos


def init_app(app):
    # registro 'close_db' para que se ejecute al final del contexto de la app
    app.teardown_appcontext(close_db)
