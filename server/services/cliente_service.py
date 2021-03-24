from server.models.cliente import tb_cliente, ClienteSchema
from server import db


def adicionar_cliente(body):
    cliente = tb_cliente()
    cliente.nm_cliente = body['nm_cliente']
    cliente.cpf_cliente = body['cpf_cliente']
    cliente.rg_cliente = body['rg_cliente']
    cliente.endereco = body['endereco']
    cliente.cep = body['cep']
    cliente.uf = body['uf']
    cliente.data_nascimento = body['data_nascimento']
    cliente.estado_civil = body['estado_civil']
    cliente.profissao = body['profissao']
    try:
        db.session.add(cliente)
        db.session.commit()
    except:
        db.session.rollback()
    rett = ClienteSchema(many=False).jsonify(cliente)
    return rett


def retornar_clientes():
    cliente = tb_cliente
    cliente = cliente.query.all()
    rett = ClienteSchema(many=True).jsonify(cliente)
    return rett
