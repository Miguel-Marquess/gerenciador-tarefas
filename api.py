from fastapi import FastAPI
from routes.tarefa import tarefa_router
app = FastAPI()

app.include_router(tarefa_router)