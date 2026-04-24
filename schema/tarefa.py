def tarefaSerializada(tarefa):
    return {
        "id": str(tarefa['_id']),
        "descricao": tarefa['descricao'],
        "prioridade": tarefa['prioridade'],
        "concluida": tarefa['concluida'],
        "data_criacao": tarefa['data_criacao'],
        "prazo": tarefa['prazo']
    }

def lista_tarefas_serializadas(lista_tarefas):
    lista_tarefas = [tarefaSerializada(tarefa) for tarefa in lista_tarefas]
    return lista_tarefas