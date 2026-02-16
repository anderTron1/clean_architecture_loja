import pytest

from src.domain.exceptions.estoque_exceptions import EstoqueNaoEncontradoException

def test_buscar_estoque_route(client):
    response = client.post("/produto", json={
        "nome": "Mouse Gamer",
        "preco": 120.45
    })

    data = response.get_json()

    response = client.get(f"/estoque/{data['id']}")

    data = response.get_json()

    assert response.status_code == 200
    assert data["id"] == 1
    assert data["produto_id"] == data['id']
    assert data['quantidade']  == 0
    assert data['produto']["nome"] == "Mouse Gamer" 
    assert data["produto"]["preco"] == 120.45

def test_buscar_estoque_route_inexistente(client):
    response = client.get(f"/estoque/2312")

    assert response.status_code == 404

def test_adicionar_estoque_route(client):
    response = client.post("/produto", json={
        "nome": "Mouse Gamer",
        "preco": 120.45
    })

    data = response.get_json()

    response = client.put(f"/estoque/{data['id']}", json={
        "quantidade": 20
    })

    assert response.status_code == 200

def test_adicionar_estoque_route_inexistente(client):

    response = client.put(f"/estoque/1212", json={
        "quantidade": 20
    })

    assert response.status_code == 404