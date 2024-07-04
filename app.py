from flask import Flask
from flask_cors import CORS
from depesca.views import *
from depesca.database import *
import depesca

app = Flask(__name__, static_url_path='/static')

# Obtener el directorio del módulo depesca
depesca_dir = os.path.dirname(depesca.__file__)

# Crear el directorio static dentro del directorio depesca si no existe
static_dir = os.path.join(depesca_dir, 'static')
app.static_url_path = static_dir
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

# Rutas
app.route('/', methods=['GET'])(index)

app.route('/api/articulos', methods=['GET'])(get_articles)

app.route('/api/articulos/<int:id_article>', methods=['GET'])(get_article)
app.route('/api/articulos/activos', methods=['GET'])(get_active_articles)

app.route('/api/articulo/create', methods=['POST'])(new_article)

app.route('/api/articulos/update/<int:id_article>',
          methods=['PUT'])(update_article)
app.route('/api/articulos/activo/<int:id_article>',
          methods=['DELETE'])(active_article)

# Realizo una prueba de conexion a la base de datos
test_conn()
create_articulos()

init_app(app)
# permitir solicitudes desde cualquier origen
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
