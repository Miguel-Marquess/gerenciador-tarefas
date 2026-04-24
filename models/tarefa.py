from pydantic import BaseModel
from typing import Optional

class Tarefa(BaseModel):
    titulo: str
    descricao: str
    prioridade: str
    concluida: bool = False
    data_criacao: str
    prazo: str

class AtualizarTarefa(BaseModel):
    titulo: Optional[str] = None # Campo Opcional, Padrão None
    descricao: Optional[str] = None 
    prioridade: Optional[str] = None
    concluida: Optional[bool] = None
    data_criacao: Optional[str] = None
    prazo: Optional[str] = None

class AtualizarPrioridade(BaseModel):
    prioridade: str