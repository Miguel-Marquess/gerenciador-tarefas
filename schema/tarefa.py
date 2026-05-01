from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException


def tarefaSerializada(tarefa):
    return {
        "id": str(tarefa['_id']),
        'titulo': tarefa['titulo'],
        "descricao": tarefa['descricao'],
        "prioridade": tarefa['prioridade'],
        "concluida": tarefa['concluida'],
        "data_criacao": str(tarefa['data_criacao']),
        "prazo": str(tarefa['prazo'])
    }

def lista_tarefas_serializadas(lista_tarefas):
    lista_tarefas = [tarefaSerializada(tarefa) for tarefa in lista_tarefas]
    return lista_tarefas

def validar_id(id):
    try:
        return ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="ID inserido é inválido.")
    
def retorna_se_existir(item):
    if item:
        return item
    raise HTTPException(status_code=404, detail="A Tarefa nao existe.")