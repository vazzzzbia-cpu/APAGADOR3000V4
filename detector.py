"""
☠══════════════════════════════════════☠
         DETECTOR DAS SOMBRAS
☠══════════════════════════════════════☠
"""

from database import cur, db
from cache import CACHE_SHA, CACHE_FILE


async def verificar(file_unique_id, sha256):

    # Primeiro verifica o SHA
    if sha256:

        if sha256 in CACHE_SHA:
            return True

        cur.execute(
            "SELECT 1 FROM arquivos WHERE sha256=? LIMIT 1",
            (sha256,)
        )

        if cur.fetchone():

            CACHE_SHA.add(sha256)

            return True

    # Depois verifica o file_unique_id

    if file_unique_id:

        if file_unique_id in CACHE_FILE:
            return True

        cur.execute(
            "SELECT 1 FROM arquivos WHERE file_unique_id=? LIMIT 1",
            (file_unique_id,)
        )

        if cur.fetchone():

            CACHE_FILE.add(file_unique_id)

            return True

    return False


def salvar(
    tipo,
    file_unique_id,
    sha256,
    tamanho,
    data
):

    cur.execute(
        """
        INSERT INTO arquivos
        (
            tipo,
            file_unique_id,
            sha256,
            tamanho,
            data
        )
        VALUES (?,?,?,?,?)
        """,
        (
            tipo,
            file_unique_id,
            sha256,
            tamanho,
            data
        )
    )

    db.commit()

    if file_unique_id:
        CACHE_FILE.add(file_unique_id)

    if sha256:
        CACHE_SHA.add(sha256)
