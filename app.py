from flask import Flask
from depesca.views import *
from depesca.database import *

app = Flask(__name__)

# Rutas
app.route('/', methods=['GET'])(index)

app.route('/api/articulos', methods=['GET'])(get_articles)

app.route('/api/articulos/<int:id_article>', methods=['GET'])(get_article)
app.route('/api/articulos/activos', methods=['GET'])(get_active_articles)

app.route('/api/articulo/create', methods=['POST'])(new_article)

app.route('/api/articulos/update/<int:id_article>', methods=['PUT'])(update_article)
app.route('/api/articulos/activo/<int:id_article>', methods=['DELETE'])(active_article)

# Realizo una prueba de conexion a la base de datos
test_conn()
create_articulos()

init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
