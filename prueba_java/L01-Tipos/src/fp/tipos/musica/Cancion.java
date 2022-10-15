package fp.tipos.musica;

import java.time.Duration;
import java.time.LocalDate;

public class Cancion {
	// Atributos
	private String titulo;
	private String artista;
	private Duration duracion;
	private LocalDate fechaLanzamiento;
	private Genero genero;
	
	
	// Constructores
	// El de tó la vida
	public Cancion(String titulo, String artista, Duration duracion,
			LocalDate fecha, Genero genero) {
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
	
	
	
	
	
	
}
