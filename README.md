#  Gerenciador de Tarefas API

Uma API REST desenvolvida com **FastAPI** e **MongoDB** para gerenciamento de tarefas, com suporte a criação, atualização, filtragem e organização por prioridade, prazo e status.

---

##  Tecnologias utilizadas

* Python 3
* FastAPI
* MongoDB
* PyMongo
* Pydantic

---

##  Estrutura do projeto

```
gerenciador_tarefas/
│── api.py
│── database/
│   └── database.py
│── models/
│   └── tarefa.py
│── routes/
│   └── tarefa.py
│── schema/
│   └── tarefa.py
```

---

##  Funcionalidades

###  Tarefas

* Criar tarefa
* Listar todas as tarefas
* Atualizar tarefa
* Deletar tarefa

###  Filtros

* Tarefas concluídas
* Tarefas não concluídas
* Filtrar por prioridade
* Ordenar por prazo
* Tarefas atrasadas

###  Estatísticas

* Contar tarefas concluídas

---

##  Modelo de Tarefa

```json
{
  "titulo": "string",
  "descricao": "string",
  "prioridade": "string",
  "concluida": false,
  "data_criacao": "datetime",
  "prazo": "datetime"
}
```

---

##  Endpoints principais

###  Criar tarefa

```
POST /tarefa
```

###  Listar tarefas

```
GET /tarefa
```

###  Tarefas concluídas

```
GET /tarefa-concluida
```

###  Tarefas não concluídas

```
GET /tarefa-naoconcluida
```

###  Tarefas atrasadas

```
GET /tarefa-atrasadas
```

###  Atualizar tarefa

```
PUT /tarefa-atualizar/{id}
```

###  Marcar como concluída

```
PUT /tarefa/{id}
```

###  Deletar tarefa

```
DELETE /tarefa/{id}
```

---

##  Lógica de funcionamento

* Os dados são validados com **Pydantic** antes de entrar no sistema
* As operações são feitas no **MongoDB** via PyMongo
* As respostas são serializadas para JSON antes de retornar
* Datas são armazenadas como `datetime` para permitir filtros e ordenações

---

##  Exemplos de filtros MongoDB

```python
# tarefas atrasadas
{ "prazo": { "$lt": datetime.now() }, "concluida": False }

# tarefas concluídas
{ "concluida": True }
```

---

##  Possíveis melhorias futuras

* Autenticação (JWT)
* Paginação de resultados
* Organização por usuários
* Frontend em React
* Deploy da API

---

##  Autor

Projeto desenvolvido para estudo de backend com Python, FastAPI e MongoDB.
