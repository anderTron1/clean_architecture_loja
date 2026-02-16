import pytest

from src.domain.exceptions.produto_exceptions import ProdutoInvalidoException


def test_salvar_produto_route(client):
    response = client.post("/produto", json={
        "nome": "Mouse Gamer",
        "preco": 120.45
    })

    data = response.get_json()

    assert response.status_code  == 201
    assert data["nome"] == "Mouse Gamer"
    assert data["preco"] == 120.45
    assert "id" in data

def test_salvar_produto_route_invalido(client):
    response = client.post("/produto", json={
        "nome": None,
        "preco": -123
    })

    assert response.status_code == 400

def test_editar_produto_route(client):
    response = client.post("/produto", json={
        "nome": "Mouse Gamer",
        "preco": 120.45
    })
    data = response.get_json()

    response = client.put(f"/produto/{data['id']}", json={
        "nome": "Mouse",
        "preco": 152
    })
    assert response.status_code  == 200

def test_editar_produto_route_invalido(client):
    response = client.post("/produto", json={
        "nome": "Mouse Gamer",
        "preco": 120.45
    })
    data = response.get_json()

    response = client.put(f"/produto/{data['id']}", json={
        "nome": "Mouse",
        "preco": -152
    })
    assert response.status_code  == 400

def test_buscar_produto_route(client):
    response = client.post("/produto", json={
        "nome": "Mouse Gamer",
        "preco": 120.45
    })
    data = response.get_json()

    response_busca = client.get(f"/produto/{data['id']}")

    assert response_busca.status_code == 200

def test_buscar_produto_route_inexistente(client):
    response_busca = client.get("/produto/13212")

    assert response_busca.status_code == 404

def test_listar_produtos_route(client):
    response = client.post("/produto", json={
        "nome": "Mouse Gamer",
        "preco": 120.45
    })
    data = response.get_json()

    response_busca = client.get(f"/produtos")

    assert response_busca.status_code == 200

    lista = response_busca.get_json()

    assert isinstance(lista, list)
    assert len(lista) >= 1
    assert any(p["produto"]["nome"] == "Mouse Gamer" for p in lista)

def test_excluir_produto_route(client):
    response = client.post("/produto", json={
        "nome": "Mouse Gamer",
        "preco": 120.45
    })
    data = response.get_json()

    response = client.delete(f"/produto/{data['id']}")

    assert response.status_code == 200


def test_excluir_produto_route_inexistente(client):
    response = client.delete(f"/produto/123123")

    assert response.status_code == 404