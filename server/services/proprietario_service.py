from server.models.proprietario import ProprietarioSchema, tb_proprietario
from server import db


def adicionar_proprietario(body):
    proprietario = tb_proprietario()
    proprietario.nm_proprietario = body['nm_proprietario']
    proprietario.cpf_proprietario = body['cpf_proprietario']
    proprietario.rg_proprietario = body['rg_proprietario']
    proprietario.data_nascimento = body['data_nascimento']
    proprietario.estado_civil = body['estado_civil']
    proprietario.profissao = body['profissao']
    try:
        db.session.add(proprietario)
        db.session.commit()
    except:
        db.session.rollback()
    rett = ProprietarioSchema(many=False).jsonify(proprietario)
    return rett


def retorna_proprietarios():
    proprietario = tb_proprietario()
    proprietario = proprietario.query.all()
    rett = ProprietarioSchema(many=True).jsonify(proprietario)
    return rett
