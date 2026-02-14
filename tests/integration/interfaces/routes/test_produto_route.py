

#
#   VALIDAÇÃO PARA CRIAR
#
def test_criar_produto_route(client):
    response = client.post("/produto", json={
        "nome": "Mouse",
        "preco": 150
    })

def test_criar_produto_invalido_route(client):
    response = client.post("/produto", json={
        "nome1": "Mouse",
        "preco": 150
    })

#
#   VALIDAÇÃO PARA EDITAR
#
def test_editar_produto_route(client):
    response = client.post("/produto", json={
        "nome": "Mouse",
        "preco": 150
    })

    response_edit = client.put("/produto/1", json={
        "nome": "Mouse gamer",
        "preco": 150
    })

def test_editar_produto_inexistente_route(client):
    response = client.post("/produto", json={
        "nome": "Mouse",
        "preco": 150
    })

    response_edit = client.put("/produto/3232", json={
        "nome": "Mouse gamer",
        "preco": 150
    })

def test_editar_produto_nome_campos_inalidos_route(client):
    response = client.post("/produto", json={
        "nome": "Mouse",
        "preco": 150
    })

    response_edit = client.put("/produto/1", json={
        "asdfasdf": "Mouse gamer",
        "asdfasdf": 150
    })

#
#   VALIDAÇÃO PARA DELETAR
#
def test_deletar_produto_route(client):
    response = client.post("/produto", json={
        "nome": "Mouse",
        "preco": 150
    })

    client.delete("/produto/1")

def test_deletar_produto_inexistente_route(client):
    response = client.post("/produto", json={
        "nome": "Mouse",
        "preco": 150
    })

    client.delete("/produto/23423")


#
#   VALIDAÇÃO PARA DELETAR
#
def test_buscar_produto_route(client):
    response = client.post("/produto", json={
        "nome": "Mouse",
        "preco": 150
    })

    reponse = client.get("/produto/1")

def test_buscar_produto_inexistente_route(client):
    response = client.post("/produto", json={
        "nome": "Mouse",
        "preco": 150
    })

    reponse = client.get("/produto/234234")

#
#   VALIDAÇÃO PARA LISTAR
#
def test_listar_produto_route(client):
    response = client.post("/produto", json={
        "nome": "Mouse",
        "preco": 150
    })

    reponse = client.get("/produto")