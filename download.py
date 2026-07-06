"""
☠══════════════════════════════════════☠
        APAGADOR 3000 V3
          Download das Sombras
☠══════════════════════════════════════☠
"""

import asyncio
import hashlib
import os
import tempfile

from telegram import File

from config import MAX_RETRIES, RETRY_DELAY


async def calcular_sha256(arquivo: File):

    caminho = None

    for tentativa in range(MAX_RETRIES):

        try:

            fd, caminho = tempfile.mkstemp(
                prefix="shadow_"
            )

            os.close(fd)

            await arquivo.download_to_drive(caminho)

            sha = hashlib.sha256()

            with open(caminho, "rb") as f:

                while True:

                    bloco = f.read(1024 * 1024)

                    if not bloco:
                        break

                    sha.update(bloco)

            return sha.hexdigest()

        except Exception as erro:

            print(
                f"☠ Tentativa {tentativa+1}/{MAX_RETRIES} falhou:"
            )

            print(erro)

            await asyncio.sleep(RETRY_DELAY)

        finally:

            if caminho:

                try:

                    os.remove(caminho)

                except Exception:

                    pass

    return None
