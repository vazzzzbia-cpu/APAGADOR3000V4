from datetime import datetime

from detector import verificar, salvar
from download import calcular_sha256


def obter_dados(msg):

    if msg.photo:
        foto = msg.photo[-1]
        return (
            "FOTO",
            foto.file_unique_id,
            foto.file_size,
            foto.get_file,
        )

    if msg.video:
        return (
            "VIDEO",
            msg.video.file_unique_id,
            msg.video.file_size,
            msg.video.get_file,
        )

    if msg.animation:
        return (
            "GIF",
            msg.animation.file_unique_id,
            msg.animation.file_size,
            msg.animation.get_file,
        )

    if msg.document:
        return (
            "DOCUMENTO",
            msg.document.file_unique_id,
            msg.document.file_size,
            msg.document.get_file,
        )

    return None


async def processar_mensagem(msg):
    dados = obter_dados(msg)

    if dados is None:
        return

    tipo, file_unique_id, tamanho, get_file = dados

    print("=" * 40)
    print("TIPO:", tipo)
    print("FILE_ID:", file_unique_id)
    print("TAMANHO:", tamanho)

    sha256 = None

    try:
        arquivo = await get_file()
        sha256 = await calcular_sha256(arquivo)

        print("SHA:", sha256)
        print("=" * 40)

    except Exception as erro:
        print("Erro ao calcular SHA:", erro)

    duplicado = await verificar(
        file_unique_id,
        sha256,
    )

    if duplicado:
        print("DUPLICADO! Apagando...")
        try:
            await msg.delete()
        except Exception as erro:
            print("Erro ao apagar:", erro)
        return

    salvar(
        tipo,
        file_unique_id,
        sha256,
        tamanho,
        datetime.now().isoformat(),
    )
