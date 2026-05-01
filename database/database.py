from pymongo import MongoClient

client = MongoClient(
    "mongodb://localhost:27017/todo"
)
conexao = client["todo"]