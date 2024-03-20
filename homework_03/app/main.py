import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get('/get_length_of_frase')
def get_length_of_frase(frase: str = ''):
    return {"frase lenght: ", len(frase)}


@app.get('/ping/')
def ping():
    return {"message": "pong"}


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)
