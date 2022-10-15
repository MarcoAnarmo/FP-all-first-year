# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  \<XX\>/\<YY\>)
Autor/a: \<Marco Antonio Arnaiz Montero\>   uvus:\<mararnmon\>

El Dataset con el que voy a trabajar consta de 8 columnas con los siguientes valores:
	4 strs, 
	1 int, 
	1 float, 
	1 boolean, 
	1 date. 



## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
    * **\<biathon.py\>**: Definiremos las funciones con las que vamos a trabajar
    * **\<biathlon_test.py\>**: Definiremos las funciones main de las diferentes entregas.
* **/data**: Contiene el dataset del proyecto
    * **\<olympic_biathlon.csv\>**:Es un arhivo con datos sobre el podio del Biathlon olímpico en diferentes años. 
* **/doc**: Contiene un fichero con la información del proyecto
    * **\<README.md\>**: Fichero donde explicamos todo sobre el proyecto.
  
## Estructura del *dataset*

El dataset está compuesto por \<8\> columnas, con la siguiente descripción:

* **\<columna 1>**: de tipo \<str\>, representa la ciudad de la que proviene cada atleta.
* **\<columna 2>**: de tipo \<str\>, representa la disciplina en la que compitió.
* **\<columna 3>**: de tipo \<boolean\>, representa el género de cada atleta.
* **\<columna 4>**: de tipo \<str\>, representa la ciudad en la que se realizó los JJOO.
* **\<columna 5>**: de tipo \<int\>, representa el lugar en el podio en que quedó el atleta.
* **\<columna 6>**: de tipo \<float\>, representa el tiempo que hizo en la carrera el atleta.t
* **\<columna 7>**: de tipo \<str\>, representa el nombre del atleta..
* **\<columna 8>**: de tipo \<date\>, representa la fecha en la que participó..

## Tipos implementados

Se define una namedtuple con la siguiente forma: ("Biathlon", "Country, Discipline, Gender, Host_city, Medal, Result, Winner, Date").

## Funciones implementadas

### \<módulo biathlon\>

* **<lee_biathlon(fichero)>**: Recibe un fichero csv y devuelve una lista de tuplas.
* **<filtra_ganador(biathlon, podio= 1)>**: Recibe una lista de tuplas y una posición de podio deseada que usaremos para filtrar los datos. Devuelve una lista por comprensión con la que obtenemos el nombre de los participantes que hayan quedado en el podio indicado en el argumanto de la función.
* **<calcula_media_de_resultados_olímpicos(biathlon)>**: Recibe una lista de tuplas de la que extraemos una lista por comprensión con los diferentes registros de los resultados. Devuelve un float de la media de los resultados que se encuentran en la lista por comprensión obtenida.
* **<obtener_registro_mejor_resultado(biathlon)>**: Recibe una lista de tuplas de la que obtendremos el resultado máximo para posteriormente pasar un filtro con este valor y crear una lista de tuplas con todos los resultados que coincidadn con el máximo.
* **<obtener_registro_por_nacionalidad(biathlon, pais = "ITA")>**: Recibe una cadena de tuplas y la abreviatura correspondiente al país por el que queremos filtrar nuestra lista. Obtenemos una lista con los registros que sean de la nacionalidad que coincida con la indicada. La ordenaremos con el método sort() válido para listas. Se ordena en orden a las disciplinas registradas.
* **<agrupar_por_nacionalidades_registradas(biathlon)>**: Recibe una lista de tuplas de la que primeramente obtendremos una lista por comprensiñon con los registros de las diferentes nacionalidades de nuestro fichero. Crearemos un diccionario con esta lista por comprensión en el que las claves serán las diferentes nacionalidades registradas y el valor asociado será cuñantas veces se han repetido estas nacionalidades.
* **<contador_disciplinas(biathlon)>**: Esta función recibe una lista de tuplas de la que primeramente obtendremos una lista por comprensión con los registros de las diferentes disciplinas de nuestro fichero. Crearemos un diccionario con esta lista por comprensión en el que las claves serán las diferentes disciplinas registradas y el valor asociado será cuántas veces se ha repetido esta disciplina.
* **<max_suma_result_por_disciplina(biathlon)>**: Esta función recibe una lista de tuplas de la que primeramente obtendremos (a través de una función auxiliar) un diccionario al que se asociará a cada clave una disciplina registrada y el valor asociado será la suma de todos los tiempos registrados en esas disciplinas. Posteriormente se obtiene una tupla de la forma (disciplina,resultado) con la mayor suma de los tiempos registrados y para terminar se muestra por pantalla la tupla (max_result, resultado) que muestra en primer lugar la disciplina en la que se ha encontrado la mayor suma y en lugar la mayor suma registrada. 
* **<aux_result(biathlon)>**: Esta función auxiliar nos servirá para crear un diccionario a través de una lista de tuplas en el que las claves serán las diferentes disciplinas registradas y el valor asociado será la suma de todos los tiempos registrados en cada disciplina. Para terminar devuelve un diccionario en el que el valor de la suma se ha aproximado a 3 únicos decimales.
* **<porcentaje_resultados(biathlon)>**: Esta función recibe una lista de tuplas del tipo biathlon y para comenzar crearemos una lista vacía en la que registraremos los porcentajes y llamamos de nuevo a la función auxiliar descrita con anterioreidad. Despues crearemos una variable del tipo lista con las claves del diccionario obtenido con la función auxiliar y otra de sus valores. Para terminar realizamos el porcentaje de cada valor registrado en la lista con los valores, lo añadimos a la lista porcentajesy redondeamos estos valores a 3 decimales exactos. Por último, devolvemos un diccionario en el que por el método zip hemos asociado a cada clave las diferentes disciplinas registradas y a cada valor su correspondiente porcentaje. 
* **<ganador_por_disciplina(biathlon, n=3)>**: Esta función recibe una lista de tuplas del tipo biathlon y un número entero 'n' preestablecido con el valor 3. A través de un bucle 'for' creamos un diccionario al que asignamos a cada una de las diferentes disciplinas una tupla con todos los ganadores que se han registrado en ellas. Para terminar devolvemos un diccionario en el que ordenamos los valores (ganadores) alfabéticamente y nos quedamos con los 'n' primeros.

### \<módulo biathlon_test\>

* **<main_entrega1()>**: Se llama a la funcion lee_biathlon(fichero) y se obtiene de la lista de tuplas las primeras 5 lineas y su longitud.
* **<main_entrega2()>**: La función main de esta entrega llama a la función lee_biathlon definida en el modulo1 con la que conseguimos una
	   lista de tuplas de un fichero csv, la llamaremos Biathlon. Tenemos esta función dividida en dos bloques:
	    
        En el primer bloque de la entrega obtenemos:
        
            -El filtrado de los ganadores en Biathlon:
                - cuantos ganadores hay en la tupla.
                - los primeros 3 ganadores que aparecen en la la lista de tuplas.
            
            -El cálculo de la media de todos los tiempos olímpicos en las diferentes pruebas del biathlon.
        
        En el segundo bloque de la entrega obtenemos:
            
            -El cálculo del mejor resultado registrado en la lista de tuplas Biathlon (al no coincidir ningún resultado
            con la característica de ser máximo, la función tan solo devuelve uno). 
            
            -Todos los registros filtrados por nacionalidad y que se encuentran ordenados en función a la disciplina registrada, es decir,
            según el orden de aparición en la lista de tuplas.
            
            -Un diccionario en el que la clave registra la nacionalidad y el valor indica la cantidad de veces que se ha
            registrado dicha nacionalidad.
* **<main_entrega3()>**: La función main de esta entrega llama a la función lee_biathlon definida en lee_biathlon con la que conseguimos una lista de tuplas de un fichero csv, la llamaremos Biathlon.
Crearemos 4 distintas funciones de las que mostramos por pantalla:
        
            -El contador de las diferentes disciplians registradas:
                - la clave es la disciplina.
                - el valor asociado cuántas veces se ha registrado dicha clave.
            
            -Una tupla de la forma (max_result, resultado) en la que mostramos:
                - max_result muestra la disciplina en la que se ha registrado el mayor resultado.
                - resultado muestra la mayor suma de todos los tiempos registrados en las diferentes disciplinas.
     
            -Un diccionario en el que:
                - las claves son las diferentes disciplinas registradas en Biathlon.
                - los valores son los porcentajes que corresponden a la suma de los tiempos en cada disciplina.
            
            -Un diccionario en el que:
                - las claves corresponden a cada una de las diferentes disciplinas registradas.
                - el valor muestra los 'n' primeros ganadores registrados en cada disciplina, ordenados alfabéticamente.