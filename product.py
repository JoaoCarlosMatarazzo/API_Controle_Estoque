from flask_restful import Resource, reqparse
from models import db, Product

product_parser = reqparse.RequestParser()
product_parser.add_argument('nome', type=str, required=True, help='Nome incorreto')
product_parser.add_argument('quantidade', type=int, required=True, help='Quantidade incorreta')

class ProductResource(Resource):
    def get(self, product_id):
        product = Product.query.get_or_404(product_id)
        return {'id': product.id, 'nome': product.nome, 'quantidade': product.quantidade}

    def put(self, product_id):
        args = product_parser.parse_args()
        product = Product.query.get_or_404(product_id)
        product.nome = args['nome']
        product.quantidade = args['quantidade']
        db.session.commit()
        return {'message': 'Product updated', 'product': {'id': product.id, 'nome': product.nome, 'quantidade': product.quantidade}}

    def delete(self, product_id):
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return {'message': 'Product deleted'}

class ProductListResource(Resource):
    def get(self):
        products = Product.query.all()
        return [{'id': product.id, 'nome': product.nome, 'quantidade': product.quantidade} for product in products]

    def post(self):
        args = product_parser.parse_args()
        product = Product(nome=args['nome'], quantidade=args['quantidade'])
        db.session.add(product)
        db.session.commit()
        return {'message': 'Product created', 'product': {'id': product.id, 'nome': product.nome, 'quantidade': product.quantidade}}, 201


