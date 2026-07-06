"""
☠══════════════════════════════════════☠
        Banco das Sombras
☠══════════════════════════════════════☠
"""

import sqlite3

db = sqlite3.connect("dados.db", check_same_thread=False)

cur = db.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS arquivos(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    tipo TEXT NOT NULL,

    file_unique_id TEXT,

    sha256 TEXT,

    tamanho INTEGER,

    data TEXT

)
""")

cur.execute("""
CREATE INDEX IF NOT EXISTS idx_sha
ON arquivos(sha256)
""")

cur.execute("""
CREATE INDEX IF NOT EXISTS idx_file
ON arquivos(file_unique_id)
""")

cur.execute("""
CREATE INDEX IF NOT EXISTS idx_tipo
ON arquivos(tipo)
""")

db.commit()
