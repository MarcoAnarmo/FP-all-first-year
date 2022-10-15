package airbnb_test;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

import airbnb.ListaAirbnb;
import airbnb.airbnb;
import airbnb.room_type;

public class listaAirbnb_test {
	
	public static void mostrarLista(ListaAirbnb Lista) {
		for(int i = 0; i < Lista.numeroBarrios(); i++) {
			System.out.println("\nEl barrio a" + i + " registrado en ListaAirbnb es:");
			System.out.println(Lista.getLocalizaciones().get(i));
		}
	}
	
	public static void main(String[] args) {

		
		System.out.println("####################    ENTREGA 2    ####################\n");
		
		airbnb a0 = new airbnb(11111111, 12345678, room_type.ENTIRE_HOME, true, "Eixample", 1000.50f, LocalDate.of(2017, 07, 28), "0101000020E6100000C828CFBC1C56014060E63BF889B14440" );
		
		airbnb a1 = new airbnb(22222222, 87654321, room_type.ENTIRE_HOME, true, "Eixample", 1200.00f, LocalDate.of(2017, 07, 28), "0101000020E6100000C828CFBC1C56014060E63BF889B14440");
		
		airbnb a2 = new airbnb(87631221, 87634321, room_type.ENTIRE_HOME, true, "las3000", 100.00f, LocalDate.of(2017, 07, 28), "0101000020E6100000C828CFBC1C56014060E63BF889B14440");
		
		airbnb a3 = new airbnb(33333333, 87634321, room_type.ENTIRE_HOME, true, "Eixample", 100.00f, LocalDate.of(2017, 07, 28), "0101000020E6100000C828CFBC1C56014060E63BF889B14440");
		
		System.out.println("\n~~~~~~~~~~~~~~~~~~~    ARRAYLIST INICIAL    ~~~~~~~~~~~~~~~~~~~");
		List<airbnb> ListaAirbnbInicial = new ArrayList<airbnb>();
		ListaAirbnbInicial.add(a0);
		ListaAirbnbInicial.add(a1);
		ListaAirbnbInicial.add(a2);
		ListaAirbnbInicial.add(a3);
		
		for(int i = 0; i < ListaAirbnbInicial.size(); i++) {
				System.out.println("\nEl objeto " + i + " registrado en ListaAirbnbInicial es:");
				System.out.println(ListaAirbnbInicial.get(i));
		}
		
		System.out.println("\n~~~~~~~~~~~~~~~~~~~    CONSTRUCTOR ListaAirbnb     ~~~~~~~~~~~~~~~~~~~");
		
		ListaAirbnb ListaAirbnb = new ListaAirbnb("ListaAirbnb", ListaAirbnbInicial);
		mostrarLista(ListaAirbnb);
		
		airbnb a4 = new airbnb(55555555, 87634321, room_type.PRIVATE_ROOM, true, "las3000", 1020.00f, LocalDate.of(2017, 07, 28), "0101000020E6100000C828CFBC1C56014060E63BF889B14440");
		
		System.out.println("\n--------- Incorporamos el objeto a4 a ListaAirbnb ---------");
		
		ListaAirbnb.incorpora(a4);
		mostrarLista(ListaAirbnb);
		
		System.out.println("\n--------- Eliminamos el objeto a4 de ListaAirbnb ---------\n");
		
		ListaAirbnb.eliminarUltima(a4);
		mostrarLista(ListaAirbnb);
		
		System.out.println("\n--------- Método: numeroBarrios ---------");
		System.out.println("\nEn ListaAirbnb tenemos registrados finalmente " + ListaAirbnb.numeroBarrios() + " barrios de airbnb.");
		
		System.out.println("\n--------- Método: existeBarrio ---------");
		System.out.println("\n¿Existe el barrio a3 en ListaAirbnb? --> " + ListaAirbnb.existeBarrio(a3));
		
		System.out.println("\n--------- Método: numeroDeRegistrosBarrios ---------");
		System.out.println("\n¿Cuántas veces se registra el barrio Eixample en ListaAirbnb? --> " + ListaAirbnb.numeroDeRegistrosBarrios("Eixample"));
		
		System.out.println("\n--------- Método: filtroPorBarrio ---------");
		System.out.println("\nFiltramos los registros por el barrio Eixample --> \n" + ListaAirbnb.filtroPorBarrio("Eixample"));
		
		System.out.println("\n--------- Método: agruparPorBarrios ---------");
		System.out.println("\nObtenemos un map de ListaAirbnb donde asocia a cada barrio sus registros asociados --> \n" + ListaAirbnb.agruparPorBarrios());
		
		System.out.println("\n--------- Método: conteoDeBarrios ---------");
		System.out.println("\nObtenemos un map de ListaAirbnb donde asocia a cada barrio el conteo de las veces que aparece --> \n" + ListaAirbnb.conteoDeBarrios());
		
		
	}

}
