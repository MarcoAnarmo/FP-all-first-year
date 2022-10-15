package fp.vino;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.charset.StandardCharsets;
import java.nio.file.Paths;
import java.util.stream.Stream;


public class FactoriaVinos {
	public static Vinos leerVinos(String filename) {
		Vinos res=null;
		try {
			Stream<Vino>strm=Files.lines(Paths.get(filename),StandardCharsets.UTF_8)
					.skip(1) //eliminamos la cabecera
					.map(FactoriaVinos::parse);
			
			res = new Vinos(strm);
			
		} catch (IOException e) {
			
			e.printStackTrace();
			
		}
		
		return res;
	}
	
	private static Vino parse(String linea) {
		//US,California,96,235.0,Cabernet Sauvignon
		String[] partes=linea.split(",");
		if(partes.length!=5) {
			throw new IllegalArgumentException("Formato: String pais, String region, Integer puntos, Double precio, String uva");
		}
		String pais=partes[0].trim();
		String region=partes[1].trim();
		Integer puntos=Integer.parseInt(partes[2].trim());
		Double precio=Double.parseDouble(partes[3].trim());
		String uva=partes[4].trim();
		
		return new Vino(pais, region, puntos, precio, uva);
	}
	
}