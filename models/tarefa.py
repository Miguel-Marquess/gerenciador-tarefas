from pydantic import BaseModel
from typing import Optional
from datetime import datetime # para salvar no mongo como ISODate formato(XXXX-XX-XXT00:00:00). Dessa forma permite filtrar as datas de forma correta
from enum import Enum

class Tarefa(BaseModel):
    titulo: str
    descricao: str
    prioridade: str
    concluida: bool = False
    data_criacao: datetime
    prazo: datetime

class AtualizarTarefa(BaseModel):
    titulo: Optional[str] = None # Campo Opcional, Padrão None
    descricao: Optional[str] = None
    data_criacao: Optional[datetime] = None
    prazo: Optional[datetime] = None

class TipoPrioridade(str, Enum):
    alta = "alta"
    media = "media"
    baixa = "baixa"

class Message(BaseModel):
    message: str