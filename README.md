# **PROYECTO DATA ENGINEER - Matias Garro Alou**

## ***Contexto y rol del proyecto:***

<p>El departamento de data analysis requiere realizar consultas a diversos datasets de las principales plataformas de streaming de series y películas (amazon prime, netflix, etc).
</p>
<p>Para ello, primero se debe aplicar un proceso de <strong>limpieza y transformación de los datasets (ETL)</strong>.</p>
<p>Luego, realizar las consultas específicas y disponibilizar los datos mediante la creación y ejecución de una <em>API</em>.
</p>

## ***Transformaciones requeridas:***
+ Generar campo **`id`**: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = **`as123`**)

+ Los valores nulos del campo rating deberán reemplazarse por el string “**`G`**” (corresponde al maturity rating: “general for all audiences”

+ De haber fechas, deberán tener el formato **`AAAA-mm-dd`**

+ Los campos de texto deberán estar en **minúsculas**, sin excepciones

+ El campo ***duration*** debe convertirse en dos campos: **`duration_int`** y **`duration_type`**. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

## ***Consultas requeridas:***
+ Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma

+ Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

+ La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

+ Película que más duró según año, plataforma y tipo de duración

+ Cantidad de series y películas por rating

## ***Ejecución del proyecto:***
Debido a que todos los datasets presentaban la misma estructura y forma, en el archivo ***`“data.py”`*** decidí crear una función que automáticamente limpie y transforme los datos de cada dataset.

Recibiendo únicamente un argumento (la ruta del dataset), la función retorna un dataframe de pandas con el formato deseado

Luego de aplicar la función creada a cada dataset, decidí concatenar todos para formar una única fuente de datos y exportarla con el nombre ***`“data.csv”`***

En el archivo ***`“main.py”`*** cargué el dataset ya limpio y comencé a crear la API y diseñar cada uno de las consultas requeridas

Decidí utilizar la librería de **FastAPI** para crear mi API debido a su sencillez y eficacia.

Una vez creadas todas las consultas y verificar que la API devuelve los valores correctos, utilicé **Deta** para realizar el deployment de la API y que los analistas puedan acceder a ella de manera pública por internet.

### **Accediendo a este link (https://8wj1za.deta.dev/docs) se pueden visualizar y realizar las consultas requeridas desde la API**.

### **Video Explicativo: [Click aquí](https://drive.google.com/file/d/17gLBc4XtgWop3dHuooTPiwhvnvT0qcCY/view?usp=sharing)**. <br>
### ***Linkedin***: [https://www.linkedin.com/in/matiasgarroalou/](https://www.linkedin.com/in/matiasgarroalou/)<br>
### ***GitHub***: [https://github.com/matiasgarroa](https://github.com/matiasgarroa)</p>
### ***Email***: matiasgarroalou@gmail.com</p>
