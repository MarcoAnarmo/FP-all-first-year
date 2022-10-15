package prueba_java;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Stream;

import airbnb.airbnb;
import airbnb.airbnb_factoria;

public class prueba_ueue {
	
	public static Airbnb leerAirbnb(String filename) {
		
		//Leer los datos y guardarlos en un Stream<Airbnb>
		Airbnb res = null;
		try {
			Stream<Airbnb> sv =Files.lines(Paths.get(filename))
					.skip(1)
					.map(airbnb_factoria :: parse);//Stream<String> --> Stream<Vino>
			
			//2.Crear un objeto de tipo Airbnb mediante el construtcor a partir de Sream<Airbnb>
			
			res= new Airbnb("Airbnb",sv);
			
		} catch (IOException e) {
			System.out.println("No se ha encontrado el fichero");
			e.printStackTrace();
		}
		return res;
	}
	
	////////////////////////////////////////////////////////////////////////////////////////////
	
	public static airbnb leerAirbnb(String filename) {
		airbnb res = null;
		try {
			Stream<airbnb>strm = Files.lines(Paths.get(filename),StandardCharsets.UTF_8)
					.skip(1) //eliminamos la cabecera
					.map(airbnb_factoria :: parse);
			
			res = new airbnb(strm);
			
		} catch (IOException e) {
			
			e.printStackTrace();
			
		}
		
		return res;
	 }
}
