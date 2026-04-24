from pydantic import BaseModel

class Tarefa(BaseModel):
    titulo: str
    descricao: str
    prioridade: str
    concluida: bool
    data_criacao: str
    prazo: str

