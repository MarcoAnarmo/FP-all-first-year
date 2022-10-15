package fp.tipos.musica.test;

import java.time.Duration;

import fp.tipos.musica.Cancion;
import fp.tipos.musica.Genero;

public class TestCancion {

	public static void main(String[] args) {
		// TODO Auto-generated method 
		Cancion c = new Cancion("Whole Lotta Love", "Led Zeppelin");
		System.out.println(c);
		
		// Probando restricciones
		c.setDuracion(Duration.ofSeconds(3));
		
		// Probando equals
		Cancion c2 = new Cancion("Macarena", "Los del Río");
		Cancion c3 = new Cancion("Macarena", "Los del Río");
		
		System.out.println(c3.equals(c2));
		c3.setGenero(Genero.POP);
		System.out.println(c3.equals(c2));
		
		//Probando orden natural
		// Dos canciones iguales
		System.out.println(c2.compareTo(c3));
		// Dos canciones diferentes
		System.out.println(c2.compareTo(c));

	}
}
