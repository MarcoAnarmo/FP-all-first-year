package fp.tipos.musica;

import java.time.Duration;
import java.time.LocalDate;
import java.util.Objects;

import fp.utiles.Checkers;

public class Cancion implements Comparable<Cancion>{
	// Atributos
	private String titulo;
	private String artista;
	private Duration duracion;
	private LocalDate fechaLanzamiento;
	private Genero genero;
	
	
	
	// Restricciones
	// •	R1: el valor en segundos de la duración 
	//      de una canción siempre es positivo.
	
	// Constructores
	// El de t� la vida
	public Cancion(String titulo, String artista, Duration duracion,
			LocalDate fecha, Genero genero) {
		//checkDuracion(duracion);
		Checkers.check("La duración no puede ser negativa", duracion.toSeconds() >=0);
		this.titulo = titulo;
		this.artista = artista;
		this.duracion = duracion;
		fechaLanzamiento = fecha;
		this.genero = genero;
	}
	
	// Constructor del enunciado
	public Cancion(String titulo, String artista) {
		this.titulo = titulo;
		this.artista = artista;
		this.duracion = Duration.ZERO;
		this.fechaLanzamiento = null;
		this.genero = null;
	}
	
	
	public String getTitulo() {
		return titulo;
	}
	
	public void setTitulo(String t){
		titulo = t;
	}

	public String getArtista() {
		return artista;
	}

	public void setArtista(String artista) {
		this.artista = artista;
	}

	public Duration getDuracion() {
		return duracion;
	}

	public void setDuracion(Duration duracion) {
		//checkDuracion(duracion);
		Checkers.check("La duración no puede ser negativa", duracion.toSeconds()>= 0);
		this.duracion = duracion;
	}

	public LocalDate getFechaLanzamiento() {
		return fechaLanzamiento;
	}

	public void setFechaLanzamiento(LocalDate fechaLanzamiento) {
		this.fechaLanzamiento = fechaLanzamiento;
	}

	public Genero getGenero() {
		return genero;
	}

	public void setGenero(Genero genero) {
		this.genero = genero;
	}
	
	// Propiedad derivada
	public String getFormatoCorto() {
		return getTitulo() + " ("+getArtista() + ") " + durACadena(getDuracion()); 
	}
	
	
	
	// Si decidimos hacer la restricción con un método privado
//	private void checkDuracion(Duration duracion) {
//		if (duracion.toSeconds() < 0) {
//			throw new IllegalArgumentException("La duración debe ser positiva");
//		}
//	}
//	
	

	@Override
	public String toString() {
		return "Cancion [titulo=" + getTitulo() + ", artista=" + artista + ", duracion=" + duracion + ", fechaLanzamiento="
				+ fechaLanzamiento + ", genero=" + genero + "]";
	}
	
	private String durACadena(Duration duracion) {
		Long minutos = duracion.toMinutes();
		Integer segundos = duracion.toSecondsPart();
		return minutos + ":" + segundos;
	}

	
	// Criterio de igualdad: dos canciones son iguales si lo son sus títulos 
	//y sus artistas.
	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((artista == null) ? 0 : artista.hashCode());
		result = prime * result + ((titulo == null) ? 0 : titulo.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Cancion other = (Cancion) obj;
		if (artista == null) {
			if (other.artista != null)
				return false;
		} else if (!artista.equals(other.artista))
			return false;
		if (titulo == null) {
			if (other.titulo != null)
				return false;
		} else if (!titulo.equals(other.titulo))
			return false;
		return true;
	}


	

	
	public int compareTo(Cancion c) {
		// artista y título
		int res = this.artista.compareTo(c.getArtista());
		if(res == 0) {
			res = this.titulo.compareTo(c.getTitulo());
		}
		return res;
	}
	
}
