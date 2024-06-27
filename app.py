from flask import Flask
from flask_restful import Api
from models import db
from resources.product import ProductResource, ProductListResource

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    api = Api(app)
    api.add_resource(ProductListResource, '/products')
    api.add_resource(ProductResource, '/products/<int:product_id>')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

