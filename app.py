from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
<<<<<<< HEAD
=======

>>>>>>> 200f8b94f31d6b87fe4d6eabe9f7cce09a6baf5a
def ola_mundo():
    return{"teste":"Olá mundo!"}

@app.get("/teste")
<<<<<<< HEAD
def teste():
    return{"teste":"testando"}

@app.get("/alunos")
def alunos():
    return{"nome":"andré","turma":"imi3"}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
=======

def teste():
    return{"teste":"testando"}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
>>>>>>> 200f8b94f31d6b87fe4d6eabe9f7cce09a6baf5a
