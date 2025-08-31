from fastapi import FastAPI

app = FastAPI(
    title="SafePass API",
    description="Uma API para um gerenciador de senhas pessoal",
    version="0.1.0"
)


@app.get("/")
def read_root():
    """
        Endpint raiz que retorna uma mensagem de boas vindas
    """
    return {"message": "Bem-vindo a safepass API!"}