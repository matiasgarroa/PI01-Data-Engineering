<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Data Engineering`**</h1>

# <h1 align=center>**`Matias Garro Alou - DTS-06`**</h1>

<p align="center">
<img src="https://files.realpython.com/media/What-is-Data-Engineering_Watermarked.607e761a3c0e.jpg"  height=300>
</p>

¡Bienvenidos a mi primer proyecto individual, esta vez, en el rol de un ***Data Engineer***!  

<hr>  

## **Descripción del problema (Contexto y rol a desarrollar)**

## Contexto

`Application Programming Interface`  es una interfaz que permite que dos aplicaciones se comuniquen entre sí, independientemente de la infraestructura subyacente. Son herramientas muy versátiles que permiten por ejemplo, crear pipelines facilitando mover y brindar acceso simple a los datos que se quieran disponibilizar a través de los diferentes endpoints, o puntos de salida de la API.

Hoy en día contamos con **FastAPI**, un web framework moderno y de alto rendimiento para construir APIs con Python.
<p align=center>
<img src = 'https://i.ibb.co/9t3dD7D/blog-zenvia-imagens-3.png' height=250><p>

## Rol a desarrollar

Como parte del equipo de data de una empresa, el área de análisis de datos le solicita al área de Data Engineering ciertos requerimientos para el óptimo desarrollo de sus actividades. Usted deberá elaborar las *transformaciones* requeridas y disponibilizar los datos mediante la *elaboración y ejecución de una API*.



## **Propuesta de trabajo**

**`Transformaciones`**:  Se realizaron las siguientes transformaciones en los datos:


+ Generación de campo **`id`**: Cada id se compone de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets

+ Los valores nulos del campo rating fueron reemplazados por el string “**`G`**” (corresponde al maturity rating: “general for all audiences”)

+ Cambio de formato de fecha a **`AAAA-mm-dd`**

+ El campo ***duration*** se divide en dos campos: **`duration_int`** y **`duration_type`**. El primero de tipo integer y el segundo de tipo string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

+ Los campos de texto pasan a estar en **minúsculas**, sin excepciones
  
<br/>

**`Desarrollo API`**:  Para disponibilizar los datos la empresa usa el framework ***FastAPI***. El analista de datos requiere consultar:

+ ***get_word_count():***Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma

+ ***get_score_count():***Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

+ ***get_second_score():***La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

+ ***get_longuest():***Película que más duró según año, plataforma y tipo de duración

+ ***get_rating_count():***Cantidad de series y películas por rating

<br/>

<b>El link a mi [API](https://8wj1za.deta.dev/docs) aquí: https://8wj1za.deta.dev/docs</b>

<br/>


**`Deployment`**: La empresa suele usar [Deta](https://www.deta.sh/?ref=fastapi) (no necesita dockerizacion) para realizar el deploy de sus aplicaciones.
<br/>

<br/>

**`Video`**: Click [aquí]() para ver un pequeño resumen
<br/>
**`Contacto`**: Tambien dejo mi perfil de [LinkedIn](https://www.linkedin.com/in/mat%C3%ADasgarroalou/), donde estaré publicando proximos proyectos

<br/>

## **Material de apoyo**

Imagen Docker con Uvicorn/Guinicorn para aplicaciones web de alta performance:

+ https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi/ 

+ https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker

FAST API Documentation:

+ https://fastapi.tiangolo.com/tutorial/

"Prolijidad" del codigo:

+ https://pandas.pydata.org/docs/development/contributing_docstring.html

<br/>

## `Disclaimer`
De parte del equipo de Henry se aclara y remarca que el fin de los proyectos propuestos es exclusivamente pedagógico, con el objetivo de realizar simular un entorno laboral, en el cual se trabajan diversas temáticas ajustadas a la realidad. No reflejan necesariamente la filosofía y valores de la organización. Además, Henry no alienta ni tampoco recomienda a los alumnos y/o cualquier persona leyendo los repositorios (y entregas de proyectos) que tomen acciones con base a los datos que pudieran o no haber recabado. Toda la información expuesta y resultados obtenidos en los proyectos nunca deben ser tomados en cuenta para la toma real de decisiones (especialmente en la temática de finanzas, salud, política, etc.).
