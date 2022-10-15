package fp.tipos.musica.test;

import java.time.Duration;

import fp.tipos.musica.Cancion;
import fp.tipos.musica.Genero;

public class TestCancion {
	
	public static void mostrarCancion(Cancion c) {
		System.out.println("Artista: " + c.getArtista());
		System.out.println("Titulo: " + c.getTitulo());
		System.out.println("Fecha lanzamiento: " + c.getFechaLanzamiento());
		System.out.println("Genero: " + c.getGenero());
		System.out.println("Formato corto: " + c.getFormatoCorto());
		System.out.println(c);
	}
	
	
	
	public static void main(String[] args) {
		Cancion c = new Cancion("Whole Lotta Love" , "Whole Lotta Love");
		mostrarCancion(c);
		
		c.setTitulo("Thriller");
		c.setArtista("Michael Jackson");
		c.setDuracion(Duration.ofSeconds((160)));
		c.setGenero(Genero.POP);
		System.out.println("Cancion tras el cambio: " + c);
	}

}
