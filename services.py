
from database import get_db_connection


def criar_registro(registro):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO registros (titulo, descricao, ativo) VALUES (?, ?, ?)",
        (registro.titulo, registro.descricao, registro.ativo)
    )

    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()

    return {**registro.model_dump(), "id": novo_id}


def listar_registros():
    conn = get_db_connection()

    registros = conn.execute("SELECT * FROM registros").fetchall()

    conn.close()

    return [dict(registro) for registro in registros]


def buscar_registro(registro_id: int):
    conn = get_db_connection()

    registro = conn.execute(
        "SELECT * FROM registros WHERE id = ?",
        (registro_id,)
    ).fetchone()

    conn.close()

    return dict(registro) if registro else None


def atualizar_registro(registro_id: int, registro):
    conn = get_db_connection()

    existente = conn.execute(
        "SELECT * FROM registros WHERE id = ?",
        (registro_id,)
    ).fetchone()

    if existente is None:
        conn.close()
        return None

    conn.execute(
        "UPDATE registros SET titulo = ?, descricao = ?, ativo = ? WHERE id = ?",
        (registro.titulo, registro.descricao, registro.ativo, registro_id)
    )

    conn.commit()
    conn.close()

    return {**registro.model_dump(), "id": registro_id}



def deletar_registro(registro_id: int):
    conn = get_db_connection()

    existente = conn.execute(
        "SELECT * FROM registros WHERE id = ?",
        (registro_id,)
    ).fetchone()

    if existente is None:
        conn.close()
        return False

    conn.execute(
        "DELETE FROM registros WHERE id = ?",
        (registro_id,)
    )

    conn.commit()
    conn.close()

    return True
