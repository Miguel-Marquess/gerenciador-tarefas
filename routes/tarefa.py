from fastapi import APIRouter
from bson import ObjectId
from models.tarefa import Tarefa
from database.database import conexao
from schema.tarefa import tarefaSerializada, lista_tarefas_serializadas

# instancia o app das rotas
tarefa_router = APIRouter()

@tarefa_router.get("/")
async def inicio():
    return {"Bem vindo ao TO-DO"}

@tarefa_router.post('/tarefa')
async def adicionar_tarefa(tarefa: Tarefa):
    conexao.todo.tarefa.insert_one(dict(tarefa))
    return lista_tarefas_serializadas(conexao.todo.tarefa.find())