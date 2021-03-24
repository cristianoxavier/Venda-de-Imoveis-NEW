from server.services.proprietario_service import adicionar_proprietario, retorna_proprietarios

def post_proprietario(body):
    return adicionar_proprietario(body)

def get_proprietarios():
    return retorna_proprietarios()