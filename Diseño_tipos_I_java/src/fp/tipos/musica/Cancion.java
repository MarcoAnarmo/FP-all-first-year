package fp.tipos.musica;

import java.time.Duration;
import java.time.LocalDate;

public class Cancion {
	
	
	private String titulo;
	private String artista;
	private Duration duracion;
	private LocalDate fechaLanzamiento;
	private Genero genero;
	
	public Cancion(String titulo, String artista) {
		this.titulo = titulo;
		this.artista = artista;
		this.duracion = duracion.ZERO;
		this.fechaLanzamiento = null;
		this.genero = null;
	}
	
	public String getTitulo() {
		return titulo;
	}
	public void setTitulo(String titulo) {
		this.titulo = titulo;
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
	public void setDuracion(Duration duracion){
		this.duracion = duracion;
	}
	
	public LocalDate getFechaLanzamiento() {
		return fechaLanzamiento;
	}
	public void setfechaLanzamiento(LocalDate fechaLanzamiento) {
		this.fechaLanzamiento = fechaLanzamiento;
	}
	
	public Genero getGenero() {
		return genero;
	}
	public void setGenero(Genero genero) {
		this.genero = genero;
	}
	
	public String getFormatoCorto() {
		return getTitulo()+ "(" + getArtista() + ")" + durACadena(getDuracion());
	}
	private String durACadena(Duration Duracion) {
		Long minutos = duracion.toMinutes();
		Integer segundos = duracion.toSecondsPart();
		return minutos + ":" + segundos;
	}
	
	
	public String toString() {
		return "Cancion [ getTitulo() = " + getTitulo() + ", getArtista() = " + getArtista() 
		+ ", getDuracion() = " + getDuracion() + ", getFechaLanzamiento() = " + getFechaLanzamiento() 
		+ ", getGenero() = " + getGenero() +", getFormatoCorto() = " + getFormatoCorto() + " ]";
	}
	
	
}
