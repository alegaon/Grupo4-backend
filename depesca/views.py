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
    return jsonify([articulos.serializer() for articulo in articulos])


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
    articulo.img_portada = data['img_portada']
    articulo.titulo = data['titulo']
    articulo.descripcion = data['descripcion']
    articulo.comida = data['comida']
    articulo.embarcacion = data['embarcacion']
    articulo.guia = data['guia']
    articulo.equipos = data['equipos']
    articulo.carnada = data['carnada']
    articulo.wifi = data['wifi']
    articulo.hospedaje = data['hospedaje']
    articulo.atencion = data['atencion']
    articulo.salvavidas = data['salvavidas']
    articulo.info_descripcion = data['info_descripcion']
    articulo.info_ubicacion = data['info_ubicacion']
    articulo.info_img_principal = data['info_img_principal']
    articulo.info_img_descripcion = data['info_img_descripcion']
    articulo.inf_img_1 = data['inf_img_1']
    articulo.inf_img_2 = data['inf_img_2']
    articulo.inf_img_3 = data['inf_img_3']
    articulo.inf_img_4 = data['inf_img_4']
    articulo.actualizado = datetime.today()
    articulo.save()
    return jsonify({'message': 'Article updated succesfully', 'data': data, 'id': id_article})


def active_article(id_article):
    articulo = Articulos.get_article(id_article)
    if not articulo:
        return jsonify({'message': 'Article not found'}), 404
    articulo.delete()
    return jsonify({'message': 'Article deleted successfully'})
