from fastapi import FastAPI
from routes.tarefa import tarefa_router
from fastapi.middleware.cors import CORSMiddleware 

cliente_app= [ # portas q sao permitidas
    "http://localhost:3000" # porta do react
]

app = FastAPI()

app.include_router(tarefa_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins = cliente_app,
    allow_credentials = True, # cokkies e autenticacao
    allow_methods = ["*"],
    allow_headers = ["*"]
)