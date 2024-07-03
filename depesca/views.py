from flask import jsonify, request
from datetime import datetime
from depesca.model import Articulos


def index():
    return jsonify(
        {
            'message': 'Hola Mundo APIS con Flask!!'
        }
    )


def get_articles():
    articulos = []
    articulos = Articulos.get_articles()
    print(articulos)
    if not articulos:
        return jsonify({'message': 'Articles not found'}), 404
    return jsonify([articulo.serializer() for articulo in articulos])


def get_article(id_article):
    articulo = Articulos.get_article(id_article)
    if not articulo:
        return jsonify({'message': 'Article not found'}), 404
    return jsonify(articulo.serializer())


def get_active_articles():
    articulos = Articulos.get_active_articles()
    return jsonify([articulo.serializer() for articulo in articulos])


def new_article():
    # Estaria bueno implementar algo que compruebe que las keys del diccionario estan todas para
    # que no se rompa.
    data = request.json
    new_art = Articulos(
        img_portada=data['img_portada'],
        titulo=data['titulo'],
        descripcion=data['descripcion'],
        comida=data['comida'],
        embarcacion=data['embarcacion'],
        guia=data['guia'],
        equipos=data['equipos'],
        carnada=data['carnada'],
        wifi=data['wifi'],
        hospedaje=data['hospedaje'],
        atencion=data['atencion'],
        salvavidas=data['salvavidas'],
        info_descripcion=data['info_descripcion'],
        info_ubicacion=data['info_ubicacion'],
        info_img_principal=data['info_img_principal'],
        info_img_descripcion=data['info_img_descripcion'],
        inf_img_1=data['inf_img_1'],
        inf_img_2=data['inf_img_2'],
        inf_img_3=data['inf_img_3'],
        inf_img_4=data['inf_img_4'],
        info_provincia=data['info_provincia'],
        info_ciudad=data['info_ciudad'],
        info_mapa=data['info_mapa'],
        info_direccion=data['info_direccion'],
        info_telefono=data['info_telefono'],
        info_sitio=data['info_sitio'],
        activo=True,
        creado=data['creado'],
        actualizado=data['actualizado']
    )
    new_art.save()
    return jsonify({'message': 'Article created successfully'}), 201


def update_article(id_article):
    articulo = Articulos.get_article(id_article)
    if not articulo:
        return jsonify({'message': 'Article not found'}), 404
    data = request.json
    if not data:
        return jsonify({'message': 'Nada que actualizar'}), 404
    # los if son para corroborar que la Key del diccionario a actualizar fue enviada, sino la pasa por alto. De lo contrario se rompe el Update
    if 'img_portada' in data:
        articulo.img_portada = data['img_portada']
    if 'titulo' in data:
        articulo.titulo = data['titulo']
    if 'descripcion' in data:
        articulo.descripcion = data['descripcion']
    if 'comida' in data:
        articulo.comida = data['comida']
    if 'embarcacion' in data:
        articulo.embarcacion = data['embarcacion']
    if 'guia' in data:
        articulo.guia = data['guia']
    if 'equipos' in data:
        articulo.equipos = data['equipos']
    if 'carnada' in data:
        articulo.carnada = data['carnada']
    if 'wifi' in data:
        articulo.wifi = data['wifi']
    if 'hospedaje' in data:
        articulo.hospedaje = data['hospedaje']
    if 'atencion' in data:
        articulo.atencion = data['atencion']
    if 'salvavidas' in data:
        articulo.salvavidas = data['salvavidas']
    if 'info_descripcion' in data:
        articulo.info_descripcion = data['info_descripcion']
    if 'info_ubicacion' in data:
        articulo.info_ubicacion = data['info_ubicacion']
    if 'info_img_principal' in data:
        articulo.info_img_principal = data['info_img_principal']
    if 'info_img_descripcion' in data:
        articulo.info_img_descripcion = data['info_img_descripcion']
    if 'inf_img_1' in data:
        articulo.inf_img_1 = data['inf_img_1']
    if 'inf_img_2' in data:
        articulo.inf_img_2 = data['inf_img_2']
    if 'inf_img_3' in data:
        articulo.inf_img_3 = data['inf_img_3']
    if 'inf_img_4' in data:
        articulo.inf_img_4 = data['inf_img_4']
    # este queda automatico, cada vez que se realice un Update, se actualiza la fecha automaticamente.
    articulo.actualizado = datetime.today()
    articulo.save()
    return jsonify({'message': 'Article updated succesfully', 'data': data, 'id': id_article})


def active_article(id_article):
    articulo = Articulos.get_article(id_article)
    if not articulo:
        return jsonify({'message': 'Article not found'}), 404
    articulo.delete()
    return jsonify({'message': 'Article deleted successfully'})
