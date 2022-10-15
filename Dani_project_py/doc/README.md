# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  \<XX\>/\<YY\>)
Autor/a: \<Daniel Vela Camacho\>   uvus:\<danvelcam\>

El Dataset con el que voy a trabajar consta de 8 columnas con los siguientes valores:
	4 strs, 
	1 int, 
	1 float, 
	1 boolean, 
	1 date. 



## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
    * **\<modulo1.py\>**: Definiremos las funciones con las que vamos a trabajar.
    * **\<modulo1_test.py\>**: Definiremos las funciones main de las diferentes entregas.
* **/data**: Contiene el dataset del proyecto
    * **\<vgsales.csv\>**:Es un arhivo con datos sobre el Top 500 juegos más vendidos. 
* **/doc**: Contiene un fichero con la información del proyecto
    * **\<README.md\>**: Fichero donde explicamos todo sobre el proyecto.
  
## Estructura del *dataset*

El dataset está compuesto por \<8\> columnas, con la siguiente descripción:

* **\<columna 1>**: de tipo \<int\>, representa el ranking del juego dentro del Top 500.
* **\<columna 2>**: de tipo \<str\>, representa el nombre del videojuego.
* **\<columna 3>**: de tipo \<str\>, representa la plataforma a la que pertenece dicho juego.
* **\<columna 4>**: de tipo \<date\>, representa la fecha en la que se publicó el juego.
* **\<columna 5>**: de tipo \<str\>, representa el género al que pertenece el juego.
* **\<columna 6>**: de tipo \<str\>, representa la publicadora que lanzó el juego.
* **\<columna 7>**: de tipo \<float\>, representa la venta en millones de dicho juego.
* **\<columna 8>**: de tipo \<boolean\>, representa si dicho es juego es multijugador o no.

## Tipos implementados

Se define una namedtuple con la siguiente forma: v = namedtuple("v", "Rank, Name, Platform, Date , Genre ,Publisher,  Global_Sales, Multiplayer_Game")

## Funciones implementadas

### \<modulo1\>

* **<r_videogames(file)>**: En esta primera función,recibirá como entrada el archivo .csv a leer. Donde se almacenarán los datos contenidos en una lista de tuplas 
de tipo Videogames, para ello usaremos la librería que incluye las "namedtuples" para facilitar el trabajo con dichos datos. Recordar el uso de "delimiter= ;" en la lectura del .csv para determinar que la lectura de distintos datos vendrá dado por ese carácter. Se deben de transfomar los datos incluidos en dicho .csv según su tipo, ya sea int,float, o en el caso de que sea una fecha, usaremos la librería datetime
para el correspondiente trata de fechas. 
        ENTRADA = "Archivo .csv a leer" 
               -> "str"
        SALIDA = "Lista de tuplas con la información del .csv"
               -> [Videogames(int,str,str,date,str,str,float,boolean)].
* **<f_platform(platform,v)>**: Esta funcion se encargará de devolver los 5 juegos más vendidos de una determinada plataforma, según el interés del usuario.
        ENTRADA = "Plataforma sobre la que obtener los 5 juegos más vendidos , "Lista de tuplas con la información dataset" (platform, v)
                -> "str", [Videogames(int,str,str,date,str,str,float,boolean)]
        SALIDA  = Lista con los 5 juegos más vendidos de la plataforma indicada.
                -> ["str", "str", "str", "str" , "str"]
* **<calculate_platformsells(platform,v)>**: Esta funcion se encargará de devolver la venta media (en millones) de una determinada plataforma. Utilizaremos funcion built-in, como sum() y len() para facilitar dichos cálculos. Además usaremos round() para dar el resultado numérico con un numero específico de decimales
        ENTRADA = "Plataforma sobre la que obtener la media de ventas  , "Lista de tuplas con la información dataset" (platform, v)
                -> "str", [Videogames(int,str,str,date,str,str,float,boolean)]
        SALIDA  = Número de ventas (en millones)
                -> "float"
* **<maxsellsplatform(platform,multiplayergame,v)>**: Esta funcion se encargará de devolver los 5 juegos menos vendidos de una plataforma, ateniéndose si dichos títulos disponen de modalidad multijugador. 
Para realizar la ordenación de los juegos menos vendidos utilizaremos el metodo .sort() e indicando que los juegos se ordenen con el criterio del 2 elemento de la tupla, es decir la venta de dicho juego,
y los ordenará de menor a mayor.
        ENTRADA = "Plataforma sobre la que obtener los juegos menos vendidos"  ,"Criterio de si el juego es multijugador o no "Lista de tuplas con la información dataset" (platform,multiplayergame, v)
                -> "str", boolean,  [Videogames(int,str,str,date,str,str,float,boolean)]
        SALIDA = Lista de tuplas con los 5 juegos menos vendidos de una determinanada plataforma, segun sean multijugador o no. (Nombre del juego, Ventas)
                -> [("str","float"),("str","float"),("str","float"),("str","float"),("str","float")]
* **<datefiltered(platform,v )>**: Esta función se encargará de devolver los 5  primeros juegos publicados  de una determinada plataforma  (más antigüos primero). De nuevo recurriremos al método .sort() y dando como clave de ordenación,
el 2 elemento de la tupla, es decir su fecha de lanzamiento, obteniéndose así los juegos ordenados cronológicamente.
        ENTRADA = "Plataforma sobre la que obtener los 5 primeros juegos lanzados"  , "Lista de tuplas con la información dataset" (platform, v)
                -> "str",[Videogames(int,str,str,date,str,str,float,boolean)]
        SALIDA = Lista de tuplas con los 5 juegos lanzados en la plataforma especificada (Nombre del juego,Fecha de lanzamiento)
                -> [("str", "datetime.strptime"),("str", "datetime.strptime"),("str", "datetime.strptime"),("str", "datetime.strptime"),("str", "datetime.strptime"),]
* **<platformdictionary(platform ,v)>**: Esta función se encargará de contabilizar cuántos juegos hay disponibles de los diversos géneros en una plataforma específica. Para ello, realizaremos un diccionario 
donde cada clave será cada tipo de género, y su valor, el número de juegos de ese género en esa determinada plataforma. Para facilitar la creación de dicho diccionario, usaremos la librería "Counter"
que se encargará de contar cuantas veces aparece un género en una determinada plataforma.
        ENTRADA = "Plataforma sobre la que obtener la cantidad de juegos de cada género  , "Lista de tuplas con la información dataset" (platform, v)
                -> "str", [Videogames(int,str,str,date,str,str,float,boolean)]
        SALIDA = Diccionario donde se recopilan la cantidad de juegos de cada género.
                -> {género1("str"):valor1("int"),género2("str"):valor2("int")...}
* **dictionary_plat(v)>**: Esta función devolverá un diccionario donde se enumerarán cuántos juegos de cada plataforma están en el TOP 500 juegos más vendidos de todos los tiempos.De nuevo para llevar a cabo dicho diccionario, recurriremos a la librería "Counter", para contabilizar cuantas veces aparece cada plataforma en el dataset.
        ENTRADA =  "Lista de tuplas con la información dataset" (v)
                -> [Videogames(int,str,str,date,str,str,float,boolean)]
        SALIDA = Diccionario donde se recopilan la cantidad de juegos de cada plataforma
                -> {plataforma1("str"):valor1("int"),plataforma2("str"):valor2("int")...}
* **aux_sells(v)>**:Esta función auxiliar (la utilizaremos en la funcion maxsells(v)) devolverá un diccionario donde se contabilizarán las ventas de juegos de una determinada plataforma.Siendo las claves las plataformas, y los valores sus correspondientes ventas totales. En este caso, llevaremos a cabo la creación de dicho diccionario de la manera tradicional, a través de un bucle. El segundo bucle esta llevado a cabo para mostrar el valor de las ventas con un determinado número de decimales, en este caso 3, todo ello para facilitar la visualización del contenido del diccionario. 
        ENTRADA =  "Lista de tuplas con la información dataset" (v)
                -> [Videogames(int,str,str,date,str,str,float,boolean)]
        SALIDA = Diccionario donde se recopilan las ventas de juegos de cada plataforma
                -> {plataforma1("str"):valor1("float"),plataforma2("str"):valor2("float")...} 
* ** maxsells(v)>**: Esta función se encargará de sacar la plataforma con más ventas, utilizando como ayuda la funcion auxiliar (aux_sells(v)). En este caso esta función determinará la clave-valor , con el valor mas elevado, del diccionario creado por la función auxiliar. Para ello utilizaremos la librería "Operator" que nos permitirá encontrar dicho clave-valor.
        ENTRADA =  "Lista de tuplas con la información dataset" (v)
                -> [Videogames(int,str,str,date,str,str,float,boolean)]
        SALIDA = Clave-Valor (Platforma-Ventas totales), con las  mayores Ventas Totales 
                -> Clave("str) - Valor("flaot")
* ** percentagesells(v)>**: En esta funcion de nuevo recurriremos a la funcion auxiliar de (aux_sells(v)) para hacer un nuevo diccionario donde se registren nuevos clave-valor, donde cada clave es cada plataforma.
Dichas claves corresponden al porcentaje de ventas que supusieron respecto el total de ventas. 
        ENTRADA =  "Lista de tuplas con la información dataset" (v)
                -> [Videogames(int,str,str,date,str,str,float,boolean)]
        SALIDA = Diccionario donde se recopilan que porcentaje de ventas respecto el total que supuso cada plataforma. 
                -> {plataforma1("str"):porcentaje1("float"),plataforma2("str"):porcentaje2("float")...}                 
* ** gamespergenre(v,n)>**: Esta función creará un diccionario donde se mostrarán como claves los diversos géneros y los valores serán una lista con los juegos más vendidos de ese determinado género. Para llevar a cabo la creación de dicho diccionario recurriremos a la librería "Defaultdict" para facilitar el proceso. Donde se indicarán que los valores serán las listas con los juegos más vendidos.
La creacion del diccionario vacío "d1" será utilizado para volcar los datos creados por la librería "Defaultdict" tras realizar un slicing, para mostrar los "n" juegos más vendidos de un género.
Siendo "n" el numero de juegos a mostrar.  
        ENTRADA =  "Lista de tuplas con la información dataset", Número de juegos a mostrar en los valores del diccionario (v,n)
                -> [Videogames(int,str,str,date,str,str,float,boolean)], "int"
        SALIDA = Diccionario donde se recopilan los "n" juegos más vendidos de todos los géneros.
                -> {género1("str"):[juego1,juego2...juego"n"("str","str","str")],género2("str"):[juego1,juego2...juego"n"("str","str","str")]}              
                
### \<módulo biathlon_test\>

* **<main_1()>**: Se llama a la funcion r_videogames(file) y se obtiene de la lista de tuplas las primeras 5 lineas y su longitud.
* **<main_2()>**: La función main de esta entrega llama a la función r_videogames(file) definida en el modulo1 con la que conseguimos una
	   lista de tuplas de un fichero csv, la llamaremos v. Tenemos esta función dividida en dos bloques:
	    
        En el primer bloque de la entrega obtenemos:
        
            -El filtrado de los juegos en el Top 500:
                - los  5 juegos más vendidos de una determinada plataforma.
            
            -El cálculo de la media de ventas de una determinada plataforma.
        
        En el segundo bloque de la entrega obtenemos:
            
            -El filtrado de los 5 juegos más vendidos de una determinada plataforma,ateniéndose al criterio de si dicho juego es multijugador o no. 
            
            -El filtrado de los 5 primeros juegos publicados en una determinada plataforma.
            
            -Un diccionario en el que las claves registran los diversos tipos de géneros de juegos y el valor la cantidad de juegos que poseen dicho género en 
            una determinada plataforma.
* **<main_3()>**: La función main de esta entrega llama a la función r_videogames(file) definida en el modulo1 con la que conseguimos una
	   lista de tuplas de un fichero csv, la llamaremos v:
	   		
	   		Encontramos los siguientes tratamientos:
	   			
	   			-Creación de un  diccionario donde se almacenarán los géneros (claves) y de cuántos títulos dispone cada género entre todas las plataformas.
	   			
	   			- Función auxiliar para crear un diccionario, donde las claves sean las plataformas, y los valores, las ventas totales de dichas plataformas.Con esta 
	   			función podremos hacer las siguientes operaciones:
	   					-Mostrar cuál es la plataforma con mas ventas, y la cantidad de de dichas ventas.
	   					-Creación de un diccionario donde las claves sean las distintas plataformas, y los valores el porcentaje de ventas que supuso dicha plataforma
	   					respecto el total.
	   					
	   			- Creación de un diccionario donde las claves son los géneros de los juegos, y los valores, una lista con los "n" juegos más vendidos de dicho género.
	   			
	   				   		
	   		
	   
	   
