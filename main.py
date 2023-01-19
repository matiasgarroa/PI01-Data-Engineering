from fastapi import FastAPI
import querys as q

app = FastAPI(title='PI-01 Data Engineering', description='Matias Garro Alou DTS-06')

@app.get('/get_word_count/({keyword}_{platform})')
async def get_word_count(keyword:str,plataforma:str):
    return q.get_word_count(keyword, plataforma)

@app.get('/get_score_count/({platform}_{score}_{year})')
async def get_score_count(plataforma:str,puntaje:int, anho:int):
    return q.get_score_count(plataforma, puntaje, anho)

@app.get('/get_second_score/({plataforma})')
async def get_second_score(plataforma:str):
    return q.get_second_score(plataforma)

@app.get('/get_longest/({plataforma}_{min_o_season}_{anho})')
async def get_longest(plataforma:str, min_o_season:str, anho:int):
    return q.get_longest(plataforma, min_o_season, anho)

@app.get('/get_rating_count/({rating})')
async def get_rating_count(rating:str):
    return q.get_rating_count(rating)