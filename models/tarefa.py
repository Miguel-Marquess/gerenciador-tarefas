from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime # para salvar no mongo como ISODate formato(XXXX-XX-XXT00:00:00). Dessa forma permite filtrar as datas de forma correta
from enum import Enum

class AtualizarTarefa(BaseModel):
    titulo: Optional[str] = None # Campo Opcional, Padrão None
    descricao: Optional[str] = None
    data_criacao: Optional[datetime] = None
    prazo: Optional[datetime] = None

class TipoPrioridade(str, Enum):
    alta = "alta"
    media = "media"
    baixa = "baixa"

class Tarefa(BaseModel):
    titulo: str = Field(..., example="Estudar para prova de Matematica") # ... significa que tem q ter um valor obrigatorio, nao tem um valor padrao
    descricao: str = Field("") # "" significa que se nao colocar nada, o valor padrao e uma string vazia
    prioridade: TipoPrioridade = Field(..., exemple="media") # aqui se o usuario nao colocar valores que estao dentro do TipoPrioridade, a API levanta erro 422
    concluida: bool = False
    data_criacao: datetime
    prazo: datetime

class Message(BaseModel):
    message: str