from fastapi import APIRouter
from bson import ObjectId
from models.tarefa import Tarefa, AtualizarTarefa, AtualizarPrioridade
from database.database import conexao
from schema.tarefa import tarefaSerializada, lista_tarefas_serializadas
from pymongo import ASCENDING
# instancia o app das rotas
tarefa_router = APIRouter()

@tarefa_router.get("/")
async def inicio():
    return {"Bem vindo ao TO-DO"}

# Lista todas as tarefas do banco
@tarefa_router.get('/tarefa')
async def listar_todas_tarefas():
    return lista_tarefas_serializadas(conexao.todo.tarefa.find())

# lista tarefas nao concluidas
@tarefa_router.get('/tarefa-naoconcluida')
async def lista_tarefas_nao_concluidas():
    return lista_tarefas_serializadas(conexao.todo.tarefa.find({'concluida': False}))

# lista tarefas concluidas
@tarefa_router.get('/tarefa-concluida')
async def lista_tarefas_concluidas():
    return lista_tarefas_serializadas(conexao.todo.tarefa.find({'concluida': True}))

# filtrar por prioridade
@tarefa_router.get('/tarefa-filtro_prioridade/{prioridade}')
async def filtrar_por_prioridade(prioridade: str):
    return lista_tarefas_serializadas(conexao.todo.tarefa.find({'prioridade': prioridade}))

@tarefa_router.get('/tarefa-prazos')
async def filtrar_por_prazos():
    return lista_tarefas_serializadas(conexao.todo.tarefa.find().sort('prazo', ASCENDING)) # desending é a mesma coisa q -1, ascending seria 1

# adiciona novas tarefas
@tarefa_router.post('/tarefa')
async def adicionar_tarefa(tarefa: Tarefa):
    conexao.todo.tarefa.insert_one(dict(tarefa))
    return lista_tarefas_serializadas(conexao.todo.tarefa.find())

# deleta tarefas
@tarefa_router.delete('/tarefa/{tarefa_id}')
async def deletar_tarefa(tarefa_id):
    return tarefaSerializada(conexao.todo.tarefa.find_one_and_delete(
        {'_id': ObjectId(tarefa_id)}
    ))

# atualiza o campo 'concluido'
@tarefa_router.put('/tarefa/{tarefa_id}')
async def marcar_concluida(tarefa_id):
    conexao.todo.tarefa.find_one_and_update({
        '_id': ObjectId(tarefa_id)
    },
    {
        '$set': {'concluida': True}
    }
    )
    return lista_tarefas_serializadas(conexao.todo.tarefa.find({'concluida': True}))

# atualiza a prioridade
@tarefa_router.put('/tarefa-atualizar_prioridade/{tarefa_id}')
async def atualizar_prioridade(tarefa_id, campo_prioridade: AtualizarPrioridade):
    conexao.todo.tarefa.find_one_and_update(
        {'_id': ObjectId(tarefa_id)},
        {'$set': dict(campo_prioridade)}
    )
    return tarefaSerializada(conexao.todo.tarefa.find_one({'_id': ObjectId(tarefa_id)}))

# atualizar tarefa
@tarefa_router.put('/tarefa-atualizar/{tarefa_id}')
async def atualizar_tarefa(tarefa_id, tarefa: AtualizarTarefa):
    conexao.todo.tarefa.find_one_and_update(
        {'_id': ObjectId(tarefa_id)},
        {'$set': (tarefa.dict(exclude_unset=True))} # o exclude é uma funcao do pydantic q remove os campos nulos.
    )
    return tarefaSerializada(conexao.todo.tarefa.find_one({'_id': ObjectId(tarefa_id)}))