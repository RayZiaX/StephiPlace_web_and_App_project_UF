from cx_Freeze import setup, Executable

setup(
    name = "Stephiplace-Software",
    version = "1.0",
    description = "Programme utilisable uniquement par les agents de l'entreprise Stephiplace qui leur servira pour ajouter les annonces dans la base de donnée",
    executables = [Executable("main.py")]
)