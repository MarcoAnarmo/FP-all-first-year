package airbnb_test;

import java.time.LocalDate;
import airbnb.airbnb;
import airbnb.room_type;

public class airbnb_test {
	
	// int room_id, int host_id, double price, boolean animal, String neighborhood, String location, LocalDateTime date, room_type room_type
	
	
	// int room_id, int host_id
	
	public static void mostrarAirbnb(airbnb a) {
		System.out.println("Room id: " + a.getRoom_id());
		System.out.println("Host id: " + a.getHost_id());
		System.out.println("Price: " + a.getPrice());
		System.out.println("Animal: " + a.getAnimal());
		System.out.println("Neighborhood: " + a.getNeighborhood());
		System.out.println("Location: " + a.getLocation());
		System.out.println("Date: " + a.getDate());
		System.out.println("Room type: " + a.getRoom_type());
		System.out.println(a);
	}
	
	public static void main(String[] args) {
		
		System.out.println("####################    ENTREGA 1    ####################\n");
		
		System.out.println("\n~~~~~~~~~~~~~~~~~~~    OBJETO 1    ~~~~~~~~~~~~~~~~~~~\n");
		
		airbnb a1 = new airbnb(12345678, 12345678, room_type.ENTIRE_HOME, true, "Eixample", 1000.50f, LocalDate.of(17, 07, 28), "0101000020E6100000C828CFBC1C56014060E63BF889B14440");
		mostrarAirbnb(a1);
		
		System.out.println("\n~~~~~~~~~~~~~~~~~~~    OBJETO 2    ~~~~~~~~~~~~~~~~~~~\n");
		
		airbnb a2 = new airbnb(87654321, 87654321, 1200.00);
		mostrarAirbnb(a2);
		
		System.out.println("\n________  PROPIEDAD DERIVADA ________\n");
		
		System.out.println("Objeto 1: " + a1.precioHabitacion() );
		System.out.println("Objeto 2: " + a2.precioHabitacion() );
		
		System.out.println("\n________  TO STRING  ________\n");
		
		System.out.println("Objeto 1: " + a1.toString() );
		System.out.println("Objeto 2: " + a2.toString() );
		
		
		System.out.println("\n________  PROPIEDAD DERIVADA ________\n");
		
		System.out.println("¿Son los objetos iguales? " + a1.equals(a2));
		
		System.out.println("\n________  PROPIEDAD DERIVADA ________\n");
		
		if (a1.compareTo(a2) == 0 ) {
			System.out.println("Ambos objetos son iguales.");
			
		}else if (a1.compareTo(a2) < 0 ) {
			System.out.println("El objeto 2 es mas grande que el objeto 1.");
			
		}else {
			System.out.println("El objeto 1 es más grande que el objeto 2.");
		}
		
	}

}
