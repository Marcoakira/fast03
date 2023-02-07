from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

app.title = 'GetinOxy com FastApi'
app.version = '0.0.1 by Dr'

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 2,
        'title': 'Avatar 2',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 3,
        'title': 'Avatar 3',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } 
]

@app.get('/', tags=['home'])



def message():
    #return 'hello world'
    #return {'Hello', 'world'} # podemos retornar uma string, mas podemos retornar outras coisas como um dicionario.
    
    return HTMLResponse ('<h1> Viva la vida</h1>')
    

@app.get('/movies', tags=['filmes'])

def get_movies():
    return movies

@app.get('/movies/{id}', tags=['Buscar filme'])

def get_movie_id(id: int):
    return movies[id]

@app.get('/page')

def page():
    return HTMLResponse('Esse é uma pagina qualquer')