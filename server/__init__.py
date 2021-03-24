from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import connexion
from flask_cors import CORS

host = "localhost"
dbname = "compra_imoveis"
user = "postgres"
password = "123"

postgre_url = f"postgresql://{user}:{password}@{host}/{dbname}"

db = SQLAlchemy()
ma = Marshmallow()


def init_api():
    app = connexion.App(__name__, specification_dir="./swagger/")
    CORS(app.app)
    app.add_api("swagger.yaml", arguments={f"host_with_port": f"{host}:8080"})
    app.app.config['SQLALCHEMY_DATABASE_URI'] = postgre_url
    db.init_app(app.app)
    ma.init_app(app.app)
    return app
