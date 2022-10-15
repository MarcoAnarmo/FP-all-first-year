# Proyecto del Segundo Cuatrimestre Fundamentos de Programación (Curso  \<XX\>/\<YY\>)
Autor/a: \<Marco Antonio Arnaiz Montero\>   uvus:\<mararnmon\>

Dataset sobre registros de alquilres de airbnb en Barcelona a partir del año 2017. Contiene las siguientes columnas:

(room_id, host_id, room_type, animal, neighborhood, price, date, location)


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes archivos que forman parte del proyecto.
    
   * **\<airbnb\>**: Paquete que contiene las clases del proyecto.
    * **\<airbnb_factoria.java\>**: Clase que contiene el tipo factoría del proyecto.
     * **\<airbnb.java\>**: Clase que contiene el tipo Airbnb.
     * **\<ListaAirbnb.java\>**: Clase que contiene la lista de tipo airbnb.
     * **\<room_type.java\>**: Clase que contiene el enum con el tipo de habitación.
   * **\<airbnb_test\>**: Paquete que contiene las clases de test del proyecto.
    * **\<airbnb_factoria_test.java\>**: Clase que contiene los test del tipo Factoria Airbnb.
     * **\<airbnb_test.java\>**: Clase que contiene los test del tipo Airbnb.                 
     * **\<listaAirbnb_test.java\>**: Clase que contiene los test del tipo Lista Airbnb.
   * **\<uitles\>**: Paquete que contiene las clases de utilidad.
    * **\<Checkers.java\>**: Clase que contiene los tipos Checkers del proyecto.
* **/data**: Contiene el dataset del proyecto
    * **\<tomslee_airbnb_barcelona_1477_2017.csv\>**: dataset sobre registros de alquiler de airbnb en Barcelona a partir del año 2017.
* **/doc**: Contiene la documentación del proyecto
    * **\<README.md\>**: descripción genérica de la entrega.
    
## Estructura del *dataset*


El dataset está compuesto por \<8\> columnas, con la siguiente descripción:

* **\<room_id>**: de tipo \<Integer\>, representa el id de la habitación.
* **\<host_id>**: de tipo \<Integer\>, representa el id del arrendatario.
* **\<room_type>**: de tipo \<room_type\>, representa el tipo de habitación qeu alquila.
* **\<animal>**: de tipo \<Boolean\>, representa si lleva mascota (True) o si no (False).
* **\<neighborhood>**: de tipo \<String\>, representa el barrio en el que se encuentra la habitación.
* **\<price>**: de tipo \<Float\>, representa el precio por noche de la habitación.
* **\<date>**: de tipo \<LocalDate\>, representa la fecha de alquiler.
* **\<location>**: de tipo \<String\>, representa las coordenadas de la localización del airbnb.

## Tipos implementados

Usaremos el tipo base Airbnb, el tipo contenedor ListaAirbnb y la factoría de estos tipos.

### Tipo Airbnb (base)

**Propiedades**:

- room_id, de tipo \<Int\>, consultable y modificable. 
- host_id, de tipo \<Int\>, consultable y modificable. 
- room_type, de tipo \<room_type\>, consultable y modificable.
- animal, de tipo \<Boolean\>, consultable y modificable.
- neigborhood, de tipo \<String\>, consultable y modificable.
- price, de tipo \<Float\>, consultable y modificable.
- date, de tipo \<LocalDate\>, consultable y modificable.
- location, de tipo \<String\>, consultable y modificable.

**Propiedades Derivadas**:

- precioHabitación, de tipo \<String\>, consultable.


**Constructores**: 

- C1: airbnb: devuelve todos los atributos de la clase airbnb.
- C2: airbnb: devuelve el room_id, el host_id del usuario y el precio y todos los demás datos los devuelve null.


**Restricciones**:
 
- R1: El precio de la habitación no puede ser negativo.
- R2: La fecha del alquiler no puede ser anterior a 2017.

**ToString**: describe el tipo Airbnb.

**HashCode**: devuelve el HashCode del tipo Airbnb.

**Criterio de igualdad**: deben ser idénticas.

**Criterio de ordenación**: la habitación con mayor precio es la mayor.


#### Tipo utiles
Paquete que contiene la clase Checkers con las restricciones que usaremos en nuestros tipos.

### Factoría

- leeListaAirbnb: Recibe como argumento la ruta del fichero y devuelve una Lista del tipo Airbnb con sus objetos correspondientes parseados.
- leerAirbnb: Recibe como argumento la ruta del fichero y devuelve un stream del tipo Airbnb con sus objetos correspondientes parseados.
- parse:  Recibe como argumento una linea del fichero del tipo String y parsea cada propiedad con su tipo correspondiente.

### Tipo ListaAirbnb (contenedor)

**Propiedades**:

- barrio, de tipo \<String\>, consultable y modificable.
- localizaciones, de tipo \<List < airbnb >\>, consultable.


**Constructores**: 

- C1: Recibe un String barrio y devuelve el barrio junto a una lista vacía.
- C2: Recibe un String barrio y una Lista de tipo airbnb con localizaciones. Devuelve el barrio y una lista con todas las localizaciones dadas.
- C3: Recibe un String barrio y un Stream de tipo airbnb con localizaciones. Devuelve el barrio y una lista con todas las localizaciones dadas.

**Restricciones**:
 
- R1: El precio de la habitación no puede ser negativo.
- R2: La fecha del alquiler no puede ser anterior a 2017.
- R3: El barrio se debe encontrar entre las localizaciones.

**Criterio de igualdad**: deben ser idénticas.

**Criterio de ordenación**: idéntico al orden natural del tipo base.

**ToString**: describe el tipo ListaAirbnb.

**HashCode**: devuelve el HashCode del tipo ListaAirbnb.

**Otras operaciones**:

- incorpora(): podremos incorporar un barrio, una lista de localizaciones o una lista del tipo airbnb.
- eliminarPrimera() y eliminarUltima().
- numeroBarrios(): devuelve la longitud de la lista.
- existeBarrio() y existeBarrios(): podremos comprobar si existe un barrio o una colección de ellos.

**Métodos con bucles tradicionales**:

- numeroDeRegistroBarrios(String barrio): devuelve un Integer con la cantidad de veces que aparece el barrio que recibe como parámetro.
- filtroPorBarrio(String barrio): Filtramos por el barrio dado como parámetro y devuelve una lista con con los objetos filtrados por el barrio recibido.
- agruparPorBarrios(): Map<String, List< airbnb >> donde asocia a cada barrio sus objetos airbnb asociados en una lista.
- conteoDeBarrios(): Map<String, Integer> donde asocia a cada barrio el conteo de las veces que aparece.

**Métodos con stream**:

- numeroDeRegistrosBarriosS(String barrio): devuelve un Integer con la cantidad de veces que aparece el barrio que recibe como parámetro.
- filtroPorBarrioS(String barrio): Filtramos por el barrio dado como parámetro y devuelve una lista con con los objetos filtrados por el barrio recibido.
- agruparPorBarriosS(): Map<String, List< airbnb >> donde asocia a cada barrio sus objetos airbnb asociados en una lista.
- conteoDeBarriosS(): Map<String, Long> donde asocia a cada barrio el conteo de las veces que aparece.
