import pandas as pd

plataformas_df = pd.read_csv('plataformas_df.csv')

#Las siguientes funciones son las que ejecutaremos en la API. Estarán explicadas en el README.md

def get_word_count(keyword, plataforma):
    
    keyword = keyword.lower()
    plataforma = plataforma.lower()

    cantidad = ((plataformas_df['platform'] == plataforma) & (plataformas_df['title'].str.contains(keyword))).sum()
    cantidad = int(cantidad)

    if cantidad == 0:
        return ('La palabra ' + keyword + ' no se encuentra en los titulos de ' + plataforma.capitalize())
    elif cantidad == 1:
        return ('La palabra ' + keyword + ' se encuentra 1(una) vez en los titulos de ' + plataforma.capitalize())
    elif cantidad > 1:
        return ('La palabra ' + keyword + ' se encuentra ' + str(cantidad) + ' veces en los titulos de ' + plataforma.capitalize())

def get_score_count(plataforma, puntaje, anho):

    cantidad = ((plataformas_df['platform'] == plataforma) & (plataformas_df['score'] > puntaje) & (plataformas_df['release_year'] == anho) & (plataformas_df['duration_type'] == "min")).sum()

    if cantidad == 0:
        return ('No se encontraron peliculas con mas de ' + str(puntaje) + ' puntos en ' + plataforma.capitalize())
    elif cantidad == 1:
        return ('Se encontro 1(una) pelicula con mas de ' + str(puntaje) + ' puntos en ' + plataforma.capitalize())
    elif cantidad > 1:
        return ('Se encontraron ' + str(cantidad) + ' peliculas con mas de ' + str(puntaje) + ' puntos en ' + plataforma.capitalize())
    
def get_second_score(plataforma):

    resultado = plataformas_df[(plataformas_df['type'] == 'movie') & (plataformas_df['platform']== plataforma)]

    max_score = resultado['score'].max()
    pelicula = resultado[resultado['score'] == max_score]['title']
    pelicula = pelicula.to_list()
    pelicula = sorted(pelicula)
    pelicula = pelicula[1]
    return str(pelicula), str(max_score)

def get_longest(plataforma, min_o_season, anho):
    resultado = plataformas_df[(plataformas_df['platform']==plataforma) & (plataformas_df['release_year']==anho) & (plataformas_df['duration_type'] == min_o_season)]

    max_duration = resultado['duration_int'].max()
    pelicula = resultado[resultado['duration_int'] == max_duration]['title']
    pelicula = pelicula.to_list()
    pelicula = pelicula[0]
    return pelicula, str(max_duration) + ' ' + str(min_o_season)

def get_rating_count(rating):
        cantidad = (plataformas_df['rating'].str.contains(rating)).sum()
        return rating, int(cantidad)