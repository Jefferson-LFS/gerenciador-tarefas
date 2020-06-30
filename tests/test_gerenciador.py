from starlette.status import HTTP_200_OK
from starlette.testclient import TestClient
from gerenciador_tarefas.gerenciador import app, TAREFAS

def test_lista_tarefas_status_200():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert resposta.status_code == HTTP_200_OK

def test_lista_tarefas_formato_json():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert resposta.headers["Content-Type"] == "application/json"

def test_lista_tarefas_retorno_dever_ser_lista():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert isinstance(resposta.json(), list)


def test_deve_listar_tarefas():
    tarefa = {
        "id": 1,
        "titulo":"titulo",
        "descricao":"descricao",
        "estado": "finalizado",
    }
    TAREFAS.append(tarefa)
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert resposta.json() == [tarefa]
    TAREFAS.clear()






