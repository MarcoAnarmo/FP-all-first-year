package fp.tipos.cine.test;

import java.time.LocalDate;

import fp.tipos.cine.*;

public class TestCine {
	
	public static void mostrarPelicula(Cine c) {
		System.out.println("Titulo: " + c.getTitulo());
		System.out.println("Fecha de estreno: " + c.getFecha_de_estreno());
		System.out.println("Duracion; " + c.getDuracion());
		System.out.println("Formato Corto: " + c.formatoCorto());
		System.out.println(c);
		
	}
	
	public static void main(String[] args) {
		Cine c1 = new Cine("El buen patrón", LocalDate.of(2021, 10, 15), 120);
		mostrarPelicula(c1);
		
		System.out.println("\n###################################################\n");
		
		Cine c2 = new Cine("Tiempos modernos");
		mostrarPelicula(c2);
	}
}
