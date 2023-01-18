from fastapi import FastAPI
import pandas as pd

app = FastAPI(title='PI-01 Data Engineering', description='Matias Garro Alou DTS-06')

@app.get("/")
async def index():
    return "Hello World"

@app.on_event('startup')
async def startup():
    global plataformas_df
    plataformas_df = pd.read_csv('plataformas_df.csv') 

@app.get('/count_keyword_titulo/({keyword}, {platform})')
async def count_keyword_titulo(keyword:str,plataforma:str):
    
    keyword = keyword.lower()
    plataforma = plataforma.lower()

    cantidad = ((plataformas_df['platform'] == plataforma) & (plataformas_df['tittle'].str.contains(keyword))).sum()
    if cantidad == 0:
        return ('La palabra', keyword, 'no se encuentra en los titulos de', plataforma.capitalize())
    elif cantidad == 1:
        return ('La palabra', keyword, 'se encuentra 1(una) vez en los titulos de', plataforma.capitalize())
    elif cantidad > 1:
        return ('La palabra', keyword, 'se encuentra', cantidad, 'veces en los titulos de', plataforma.capitalize())