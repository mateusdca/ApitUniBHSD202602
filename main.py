from fastapi import FastAPI, HTTPException
from database import get_db_connection, create_tables
from models import RegistroBase, RegistroResponse
from services import criar_registro as service_criar_registro
from services import listar_registros as service_listar_registros
from services import buscar_registro as service_buscar_registro
from services import atualizar_registro as service_atualizar_registro
from services import deletar_registro as service_deletar_registro

app = FastAPI(
    title="API de Gerenciamento - Projeto A3",
    description="Template inicial integrando FastAPI, SQLite e validações Pydantic.",
    version="1.0.0"
)





# Cria a tabela automaticamente ao iniciar a API
@app.on_event("startup")
def startup_event():
    create_tables()


# ==========================================
# 3. CAMADA DE ROTAS (Endpoints HTTP)
# ==========================================

@app.post("/registros", response_model=RegistroResponse, status_code=201)
def criar_registro(registro: RegistroBase):
    if not registro.titulo.strip():
        raise HTTPException(status_code=400, detail="O título não pode estar em branco.")

    try:
        return service_criar_registro(registro)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno no banco de dados: {str(e)}")


@app.get("/registros", response_model=list[RegistroResponse], status_code=200)
def listar_registros():
    return service_listar_registros()

@app.get("/registros/{registro_id}", response_model=RegistroResponse, status_code=200)
def buscar_registro(registro_id: int):
    registro = service_buscar_registro(registro_id)

    if registro is None:
        raise HTTPException(status_code=404, detail="Registro não encontrado.")

    return registro


@app.put("/registros/{registro_id}", response_model=RegistroResponse, status_code=200)
def atualizar_registro(registro_id: int, registro: RegistroBase):
    resultado = service_atualizar_registro(registro_id, registro)

    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail="Registro não encontrado para atualização."
        )

    return resultado


@app.delete("/registros/{registro_id}", status_code=200)
def deletar_registro(registro_id: int):
    resultado = service_deletar_registro(registro_id)

    if not resultado:
        raise HTTPException(
            status_code=404,
            detail="Registro não encontrado para exclusão."
        )

    return {"mensagem": "Registro removido com sucesso."}