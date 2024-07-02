from depesca.database import get_db
import datetime


class Articulos():
    def __init__(self, id=None, img_portada=None, titulo=None, descripcion=None, comida=False, embarcacion=False, guia=False, equipos=False,
                 carnada=False, wifi=False, hospedaje=False, atencion=False, salvavidas=False, info_descripcion=None, info_ubicacion=None,
                 info_img_principal=None, info_img_descripcion=None, inf_img_1=None, inf_img_2=None, inf_img_3=None, inf_img_4=None,
                 info_provincia=None, info_ciudad=None, info_mapa=None, info_direccion=None, info_telefono=None, info_sitio=None, activo=True,
                 creado=datetime.datetime.now(), actualizado=datetime.datetime.now()
                 ):

        self.id = id
        self.img_portada = img_portada
        self.titulo = titulo
        self.descripcion = descripcion
        self.comida = comida
        self.embarcacion = embarcacion
        self.guia = guia
        self.equipos = equipos
        self.carnada = carnada
        self.wifi = wifi
        self.hospedaje = hospedaje
        self.atencion = atencion
        self.salvavidas = salvavidas
        self.info_descripcion = info_descripcion
        self.info_ubicacion = info_ubicacion
        self.info_img_principal = info_img_principal
        self.info_img_descripcion = info_img_descripcion
        self.inf_img_1 = inf_img_1
        self.inf_img_2 = inf_img_2
        self.inf_img_3 = inf_img_3
        self.inf_img_4 = inf_img_4
        self.info_provincia = info_provincia
        self.info_ciudad = info_ciudad
        self.info_mapa = info_mapa
        self.info_direccion = info_direccion
        self.info_telefono = info_telefono
        self.info_sitio = info_sitio
        self.activo = activo
        self.creado = creado
        self.actualizado = actualizado

    @staticmethod
    def __get_articles_by_query(query):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        articles = []
        for row in rows:
            articles.append(
                Articulos(
                    id=row[0],
                    img_portada=row[1],
                    titulo=row[2],
                    descripcion=row[3],
                    comida=row[4],
                    embarcacion=row[5],
                    guia=row[6],
                    equipos=row[7],
                    carnada=row[8],
                    wifi=row[9],
                    hospedaje=row[10],
                    atencion=row[11],
                    salvavidas=row[12],
                    info_descripcion=row[13],
                    info_ubicacion=row[14],
                    info_img_principal=row[15],
                    info_img_descripcion=row[16],
                    inf_img_1=row[17],
                    inf_img_2=row[18],
                    inf_img_3=row[19],
                    inf_img_4=row[20],
                    info_provincia=row[21],
                    info_ciudad=row[22],
                    info_mapa=row[23],
                    info_direccion=row[24],
                    info_telefono=row[25],
                    info_sitio=row[26],
                    activo=row[27],
                    creado=row[28],
                    actualizado=row[29]
                )
            )
        cursor.close()
        return articles

    @staticmethod
    def get_active_articles():
        return Articulos.__get_articles_by_query(
            """
        SELECT * 
        FROM articulos 
        WHERE activo = true
        ORDER BY creado DESC
        """
        )

    @staticmethod
    def get_article(id_article):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM articulos WHERE id = %s", (id_article,))
        row = cursor.fetchone()
        cursor.close()

        if row:
            return Articulos(
                id=row[0],
                img_portada=row[1],
                titulo=row[2],
                descripcion=row[3],
                comida=row[4],
                embarcacion=row[5],
                guia=row[6],
                equipos=row[7],
                carnada=row[8],
                wifi=row[9],
                hospedaje=row[10],
                atencion=row[11],
                salvavidas=row[12],
                info_descripcion=row[13],
                info_ubicacion=row[14],
                info_img_principal=row[15],
                info_img_descripcion=row[16],
                inf_img_1=row[17],
                inf_img_2=row[18],
                inf_img_3=row[19],
                inf_img_4=row[20],
                info_provincia=row[21],
                info_ciudad=row[22],
                info_mapa=row[23],
                info_direccion=row[24],
                info_telefono=row[25],
                info_sitio=row[26],
                activo=row[27],
                creado=row[28],
                actualizado=row[29]
            )
        return None

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id:  # Actualizar un articulo que ya existe
            cursor.execute(
                """
                    UPDATE articulos
                    SET img_portada = %s, titulo = %s, descripcion = %s, comida = %s, embarcacion = %s, guia = %s, equipos = %s, carnada = %s, 
                    wifi = %s, hospedaje = %s, atencion = %s, salvavidas = %s, info_descripcion = %s, info_ubicacion = %s, 
                    info_img_principal = %s, info_img_descripcion = %s, inf_img_1 = %s, inf_img_2 = %s, inf_img_3 = %s, inf_img_4 = %s, 
                    info_provincia = %s, info_ciudad = %s, info_mapa = %s, info_direccion = %s, info_telefono = %s, info_sitio = %s, 
                    activo = %s, actualizado = %s
                    WHERE id = %s
                """,
                (
                    self.img_portada, self.titulo, self.descripcion, self.comida, self.embarcacion, self.guia, self.equipos, self.carnada,
                    self.wifi, self.hospedaje, self.atencion, self.salvavidas, self.info_descripcion, self.info_ubicacion,
                    self.info_img_principal, self.info_img_descripcion, self.inf_img_1, self.inf_img_2, self.inf_img_3, self.inf_img_4,
                    self.info_provincia, self.info_ciudad, self.info_mapa, self.info_direccion, self.info_telefono, self.info_sitio,
                    self.activo, self.actualizado, self.id
                )
            )
        # De lo contrario si no tiene un id_article especificado, significa que es una nueva
        else:  # Crear un nuevo Articulo
            cursor.execute(
                """
                    INSERT INTO articulos
                    (img_portada, titulo, descripcion, comida, embarcacion, guia, equipos, carnada, wifi, hospedaje, atencion, salvavidas, 
                    info_descripcion, info_ubicacion, info_img_principal, info_img_descripcion, inf_img_1, inf_img_2, inf_img_3, inf_img_4, 
                    info_provincia, info_ciudad, info_mapa, info_direccion, info_telefono, info_sitio, activo, creado, actualizado)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    self.img_portada, self.titulo, self.descripcion, self.comida, self.embarcacion, self.guia, self.equipos, self.carnada,
                    self.wifi, self.hospedaje, self.atencion, self.salvavidas, self.info_descripcion, self.info_ubicacion,
                    self.info_img_principal, self.info_img_descripcion, self.inf_img_1, self.inf_img_2, self.inf_img_3, self.inf_img_4,
                    self.info_provincia, self.info_ciudad, self.info_mapa, self.info_direccion, self.info_telefono, self.info_sitio,
                    self.activo, self.creado, self.actualizado
                )
            )
            # Obtengo el ultimo valor de id, y se lo asigno al id_article
            self.id_article = cursor.lastrowid
        db.commit()                 # Hago efectivos los cambio sen las tablas
        cursor.close()

    def delete(self):
        # En realidad no se borra el registrofisicamente de la base. Se pone el estado del activo en false y de esta forma queda inactivo
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE articulos SET activo = false WHERE id = %s", (self.id_article,))
        db.commit()
        cursor.close()

    def serializer(self):
        return {
            'id': self.id,
            'img_portada': self.img_portada,
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'comida': self.comida,
            'embarcacion': self.embarcacion,
            'guia': self.guia,
            'equipos': self.equipos,
            'carnada': self.carnada,
            'wifi': self.wifi,
            'hospedaje': self.hospedaje,
            'atencion': self.atencion,
            'salvavidas': self.salvavidas,
            'info_descripcion': self.info_descripcion,
            'info_ubicacion': self.info_ubicacion,
            'info_img_principal': self.info_img_principal,
            'info_img_descripcion': self.info_img_descripcion,
            'inf_img_1': self.inf_img_1,
            'inf_img_2': self.inf_img_2,
            'inf_img_3': self.inf_img_3,
            'inf_img_4': self.inf_img_4,
            'info_provincia': self.info_provincia,
            'info_ciudad': self.info_ciudad,
            'info_mapa': self.info_mapa,
            'info_direccion': self.info_direccion,
            'info_telefono': self.info_telefono,
            'info_sitio': self.info_sitio,
            'activo': self.activo,
            'creado': self.creado,
            'actualizado': self.actualizado,
        }
