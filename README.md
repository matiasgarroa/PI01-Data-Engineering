<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Data Engineering`**</h1>

# <h1 align=center>**`Matias Garro Alou - DTS-06`**</h1>

<p align="center">
<img src="https://files.realpython.com/media/What-is-Data-Engineering_Watermarked.607e761a3c0e.jpg"  height=300>
</p>

Este es mi primer proyecto individual en el rol de Data Engineer. El objetivo de este proyecto es construir una API usando el framework FastAPI que permita consultar información transformada de diferentes datasets.

<hr>  

## Contexto

En este proyecto, me desempeñé como parte del equipo de data de una empresa. El área de análisis de datos le solicitó al área de Data Engineering ciertos requerimientos para el óptimo desarrollo de sus actividades. Mi tarea fue elaborar las transformaciones requeridas y disponibilizar los datos mediante la elaboración y ejecución de una API.

<p align=center>
<img src = 'https://i.ibb.co/9t3dD7D/blog-zenvia-imagens-3.png' height=250><p>

## **`Transformaciones`**

Para este proyecto, se realizaron las siguientes transformaciones en los datos:

+ Generación de campo id: Cada id se compone de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets.
+ Los valores nulos del campo rating fueron reemplazados por el string “G” (corresponde al maturity rating: “general for all audiences”).
+ Cambio de formato de fecha a AAAA-mm-dd.
+ El campo duration se divide en dos campos: duration_int y duration_type. El primero de tipo integer y el segundo de tipo string indicando la unidad de medición de duración: min (minutos) o season (temporadas).
+ Los campos de texto pasan a estar en minúsculas, sin excepciones.
  
<br/>

## **`Desarrollo API`**

Para disponibilizar los datos, se construyó una API usando el framework FastAPI. Los analistas de datos requieren consultar la siguiente información:

+ ***get_word_count():***Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma

+ ***get_score_count():***Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

+ ***get_second_score():***La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

+ ***get_longuest():***Película que más duró según año, plataforma y tipo de duración

+ ***get_rating_count():***Cantidad de series y películas por rating

<br/>

<b>El link a mi [API](https://8wj1za.deta.dev/docs) aquí: https://8wj1za.deta.dev/docs</b>

<br/>

## **`Deployment`** 

Para realizar el deploy de la aplicación, se utilizó Deta.

<br/>

## **`Video`**

Click [aquí](https://drive.google.com/file/d/17gLBc4XtgWop3dHuooTPiwhvnvT0qcCY/view?usp=sharing) para ver un pequeño resumen

<br/>

## **`Contacto`**

Tambien dejo mi perfil de [LinkedIn](https://www.linkedin.com/in/mat%C3%ADasgarroalou/), donde estaré publicando proximos proyectos

<br/>
