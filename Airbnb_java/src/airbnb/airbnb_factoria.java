package airbnb;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.time.LocalDate;

import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;

import uitles.Checkers;


public class airbnb_factoria {
	
	 public static List<airbnb> leeListaAirbnb(String filename){
		 
		 // 1. Crear una List<airbnb> vacía para añadir los datos
		List<airbnb> res=new ArrayList<airbnb>();
		
		try {
			// 2. Leer los datos y guardarlos en una List<Airbnb>
			
			List<String> lineas = Files.readAllLines(Paths.get(filename));
			
			for(String linea:lineas.subList(1, lineas.size())) {
				
				res.add(parse(linea));
				
			}
			
		}catch(IOException e) {
			
			e.printStackTrace();
			
		}
		return res;
	 }
	
	 
	 public static ListaAirbnb leerAirbnb(String filename) {
			
			// 1. Leer los datos y guardarlos en un Stream<Airbnb>
			ListaAirbnb res = null;
			try {
				Stream<airbnb> lineas =Files.lines(Paths.get(filename))
						.skip(1)
						.map(airbnb_factoria :: parse);//Stream<String> --> Stream<airbnb>
				
				// 2. Crear un objeto de tipo Airbnb mediante el constructor a partir de Sream<Airbnb>
				
				res= new ListaAirbnb("Airbnb",lineas);
				
			} catch (IOException e) {
				System.out.println("No se ha encontrado el fichero");
				e.printStackTrace();
			}
			return res;
		}
	
	
	 static airbnb parse(String linea) {
		//room_id;host_id;room_type;animal;neighborhood;price;date;location
		
		//12331794;41933599;SHARED_ROOM;false;Eixample;1404.22;2017-07-28 14:49:29.434152;0101000020E6100000C828CFBC1C56014060E63BF889B14440
		
		String[] partes=linea.split(";");
		if(partes.length!=8) {
			throw new IllegalArgumentException("Formato: Integer room_id, Integer host_id, room_type room_type, Boolean animal, String neighborhood,"
					+ " Float price, LocalDateTime date, String location");
		}
		Integer room_id = Integer.parseInt(partes[0].trim());
		Integer host_id = Integer.parseInt(partes[1].trim());
		room_type Room_type = room_type.valueOf(partes[2].trim());
		Boolean animal = Boolean.parseBoolean(partes[3].trim());
		String neighborhood = partes[4].trim();
		Float price = Float.valueOf(partes[5].trim());
		LocalDate date = LocalDate.parse(partes[6].trim(), DateTimeFormatter.ofPattern("M/dd/yyyy"));
		String location = partes[7].trim();
		
		return new airbnb(room_id, host_id, Room_type, animal, neighborhood, price, date, location);
	}
	
	
}
