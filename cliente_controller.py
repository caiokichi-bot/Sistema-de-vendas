from flask import Flask, jsonify, request, Blueprint
from cliente_repository import ClienteRepository

cliente_bp = Blueprint("cliente",__name__)

@cliente_bp.route("/ola", methods = ['GET'])
def ola():
    return 'minha primeira API'

@cliente_bp.route("/clientes", methods = ['GET'])
def listar_clientes():
    repo = ClienteRepository()
    dados = repo.find_all()
    cabecalhos = ['id','nome', 'cpf','email', 'telefone', 'endereco', 'cidade', 'estado', 'cep']
    dados_retorno = [dict(zip(cabecalhos, d))for d in dados]
    return jsonify(dados_retorno)

@cliente_bp.route('/clientes/<int:clienteID>', methods = ['GET'])
def buscar_por_id(clienteID):
    repo = ClienteRepository()
    categoria = repo.find_by_id(clienteID)
    categoria_retorno = {'id':categoria[0],'nome':categoria[1],'cpf':categoria[2], 'email':categoria[3], 'telefone':categoria[4], 'endereco':categoria[5], 'cidade':categoria[6], 'estado':categoria[7], 'cep':categoria[8]}
    return jsonify(categoria_retorno)

@cliente_bp.route('/clientes', methods = ['POST'])
def cadastrar_cliente():
    repo = ClienteRepository()
    #recebendo os dados via protocolo POST http
    dados_json = request.get_json()

    #pegando os dados recebidos do json
    id = dados_json.get('id')
    nome = dados_json.get('nome')
    cpf = dados_json.get('cpf')
    email = dados_json.get('email')
    telefone = dados_json.get('telefone')
    endereco = dados_json.get('endereco')
    cidade = dados_json.get('cidade')
    estado = dados_json.get('estado')
    cep = dados_json.get('cep')
    
    #enviando para o banco de dados
    repo.create(nome, cpf, email, telefone, endereco, cidade, estado, cep)

    return jsonify({
        'mensagem':'Categoria cadastrada com sucesso',
        'nome':nome,
        'cpf':cpf,
        'email':email,
        'telefone':telefone,
        'endereco':endereco,
        'cidade':cidade,
        'estado':estado,
        'cep':cep
        }), 201

@cliente_bp.route('/clientes/<int:id_cliente>', methods = ['DELETE'])
def remover_cliente(id_cliente):
    #objeto de comunicação com o banco de dados
    repo = ClienteRepository()
    #removendo a categoria do banco de dados
    repo.delete(id_cliente)
    return jsonify({
        "mensagem":"Categoria removida com sucesso"

    })
