package airbnb_test;

import java.util.List;

import airbnb.ListaAirbnb;
import airbnb.airbnb;
import airbnb.airbnb_factoria;

public class airbnb_factoria_test {

	public static void main(String[] args) {
		
		System.out.println("\n####################    ENTREGA 3    ####################\n");
		System.out.println("--------- FACTORÍA PARA LISTA_AIRBNB ---------\n");
		
		List<airbnb> datos_csv = airbnb_factoria.leeListaAirbnb("data/tomslee_airbnb_barcelona_1477_2017-07-23.csv");
		
	    ListaAirbnb listaAirbnb  = new ListaAirbnb("Barrios");
	    
	    listaAirbnb.incorpora(datos_csv.subList(0, 10)); //nos quedamos tan solo con los 10 primero datos, es decir del 1 al 11 
	    												//pues nos saltamos la cabecera en la factoría
	    
	    System.out.println(listaAirbnb);
		
		System.out.println("\n--------- Método: numeroDeRegistrosBarriosS ---------");
		System.out.println("\n¿Cuántas veces se registra el barrio Eixample en ListaAirbnb? --> " + listaAirbnb.numeroDeRegistrosBarriosS("Eixample"));
	    
		System.out.println("\n--------- Método: filtroPorBarrioS ---------");
		System.out.println("\nFiltramos los registros por el barrio Eixample --> \n" + listaAirbnb.filtroPorBarrioS("Eixample"));
	    
		System.out.println("\n--------- Método: agruparPorBarriosS ---------");
		System.out.println("\nObtenemos un map de ListaAirbnb donde asocia a cada barrio sus registros asociados --> \n" + listaAirbnb.agruparPorBarriosS());
		
		System.out.println("\n--------- Método: conteoDeBarriosS ---------");
		System.out.println("\nObtenemos un map de ListaAirbnb donde asocia a cada barrio el conteo de las veces que aparece --> \n" + listaAirbnb.conteoDeBarrios());
		
	}
	
	
}


