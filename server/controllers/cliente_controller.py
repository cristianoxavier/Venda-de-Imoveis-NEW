from server.services.cliente_service import adicionar_cliente, retornar_clientes

def post_cliente(body):
    return adicionar_cliente(body)

def get_clientes():
    return retornar_clientes()