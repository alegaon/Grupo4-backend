from flask import current_app, jsonify, request
from werkzeug.utils import secure_filename
from datetime import datetime
from depesca.model import Articulos

import os


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


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def __allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def new_article():
    # Estaria bueno implementar algo que compruebe que las keys del diccionario estan todas para
    # que no se rompa.
    data = request.json
    # Assuming 'img_portada' contains the file path
    img_portada = data.get('img_portada')

    # Handle file upload
    if img_portada:
        # Assuming img_portada contains the path to the image file on the server
        filename = os.path.basename(img_portada)
        dest = os.path.join(current_app.static_url_path, filename)

        # Move the uploaded file to the static directory
        os.rename(img_portada, dest)
        # Store relative path in database
        img_portada = os.path.join('\static', filename)

    new_art = Articulos(
        img_portada=img_portada,
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
    # Si se envia un diccionario vacio, se retorna un mesaje.
    if not data:
        return jsonify({'message': 'Nothing to update.', 'id': id_article}), 404

    # Lista de los campos que se pueden actualizar
    campos_actualizables = [
        'img_portada', 'titulo', 'descripcion', 'comida', 'embarcacion', 'guia',
        'equipos', 'carnada', 'wifi', 'hospedaje', 'atencion', 'salvavidas',
        'info_descripcion', 'info_ubicacion', 'info_img_principal',
        'info_img_descripcion', 'inf_img_1', 'inf_img_2', 'inf_img_3', 'inf_img_4'
    ]

    # Itero sobre cada campo, si esta en la lista, lo actualizo.
    for campo in campos_actualizables:
        if campo in data:
            setattr(articulo, campo, data[campo])

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
