from fastapi import APIRouter, HTTPException
from bson import ObjectId
from models.tarefa import Tarefa, AtualizarTarefa, TipoPrioridade, Message
from database.database import conexao
from schema.tarefa import tarefaSerializada, lista_tarefas_serializadas, validar_id, retorna_se_existir
from pymongo import ASCENDING
from datetime import datetime

# instancia o app das rotas
tarefa_router = APIRouter()

@tarefa_router.get("/")
async def inicio():
    return {"Bem vindo ao TO-DO"}

# Lista todas as tarefas do banco
@tarefa_router.get('/tarefa')
async def listar_tarefas(concluida: bool = None, prioridade: TipoPrioridade = None, ordenar_prazo: bool = None, tarefas_atrasadas: bool = None): # TipoPrioridade usa Enum para colocar caixa de selecao de prioridades.
    query={} # {"concluida": False, "prazo"}
    if concluida is not None:
        query["concluida"] =  concluida
    if prioridade is not None:
        query["prioridade"] = prioridade # find({concluisda: False}) 
    if tarefas_atrasadas is not None:
        query["prazo"] = {"$lt": datetime.now()} # 
        query["concluida"] = False

    tarefa_mongo = conexao.tarefa.find(query)
    if ordenar_prazo is not None:
        tarefa_mongo = tarefa_mongo.sort("prazo", ASCENDING)
    return lista_tarefas_serializadas(tarefa_mongo)

# adiciona novas tarefas
@tarefa_router.post('/tarefa', response_model=Tarefa, status_code=201)
async def adicionar_tarefa(tarefa: Tarefa):
    tarefa_mongo = conexao.tarefa.insert_one(tarefa.dict())
    return tarefaSerializada(tarefa_mongo)

# deleta tarefas
@tarefa_router.delete('/tarefa/{tarefa_id}', response_model=Tarefa, responses= {404: {"model": Message}, 400: {"model": Message}})
async def deletar_tarefa(tarefa_id):
    id_validado = validar_id(tarefa_id)
    tarefa_mongo = conexao.tarefa.find_one_and_delete(
        {'_id': id_validado}
    )
    if retorna_se_existir(tarefa_mongo):
        return {"Mensagem" : "Tarefa deletada com sucesso."}

# atualiza o campo 'concluido'
@tarefa_router.put('/tarefa/{tarefa_id}', response_model=Tarefa, responses={404: {"model": Message}, 400: {"model": Message}})
async def marcar_concluida(tarefa_id):
    id_validado = validar_id(tarefa_id)
    tarefa_mongo = conexao.tarefa.find_one_and_update(
        {'_id': id_validado},
        {'$set': {'concluida': True}}
    )
    return tarefaSerializada(retorna_se_existir(tarefa_mongo))

# atualiza a prioridade
@tarefa_router.put('/tarefa/atualizar_prioridade/{tarefa_id}', response_model=Tarefa, responses={404: {"model": Message}, 400: {"model": Message}})
async def atualizar_prioridade(tarefa_id, campo_prioridade: TipoPrioridade):
    id_validado = validar_id(tarefa_id)
    tarefa_mongo = conexao.tarefa.find_one_and_update(
        {'_id': id_validado},
        {'$set': {"prioridade": campo_prioridade}}
    )
    if retorna_se_existir(tarefa_mongo):
        return tarefaSerializada(conexao.tarefa.find_one({'_id': id_validado})) # retorna_se_existir: se a tarefa for Nula, levanta erro 404.

# atualizar tarefa
@tarefa_router.put('/tarefa/atualizar/{tarefa_id}', response_model=Tarefa, responses={404: {"model": Message}, 400: {"model": Message}}) # response_model: define o formato da resposta da API. responses: 
async def atualizar_tarefa(tarefa_id, tarefa: AtualizarTarefa):
    id_validado = validar_id(tarefa_id)
    tarefa_mongo = conexao.tarefa.find_one_and_update(
        {'_id': id_validado},
        {'$set': tarefa.dict(exclude_unset=True)} # o exclude é uma funcao do pydantic q remove os campos nulos. model_dump e a mesma coisa de .dict() so que nao e obsoleto
    )
    return tarefaSerializada(retorna_se_existir(tarefa_mongo))
