package fp.tipos.cine;

import java.time.LocalDate;

public class Cine {
	
	private String titulo;
	private LocalDate fecha_de_estreno;
	private Integer duracion;
	
	public Cine(String titulo, LocalDate fecha_de_estreno, Integer duracion) {
		this.titulo = titulo;
		this.fecha_de_estreno = fecha_de_estreno;
		this.duracion = duracion;
	}
	
	public Cine(String titulo) {
		this(titulo, null, null);
		
	}

	public LocalDate getFecha_de_estreno() {
		return fecha_de_estreno;
	}

	public void setFecha_de_estreno(LocalDate fecha_de_estreno) {
		this.fecha_de_estreno = fecha_de_estreno;
	}

	public Integer getDuracion() {
		return duracion;
	}

	public void setDuracion(Integer duracion) {
		this.duracion = duracion;
	}

	public String getTitulo() {
		return titulo;
	}

	public TipoMetraje getTipoMetraje() {
		TipoMetraje res = null;
		if (getDuracion() != null) {
			res = TipoMetraje.LARGOMETRAJE;
			if (getDuracion() < 30) {
				res = TipoMetraje.CORTOMETRAJE;
			} else if (getDuracion() >= 30 && getDuracion() <= 60) {
				res = TipoMetraje.MEDIOMETRAJE;
			}
		}
		return res;
	}

	public String formatoCorto () {
		if ( getFecha_de_estreno() != null ){
			return getTitulo() + " (" + getFecha_de_estreno() + ")";
		}else {
			return getTitulo();
		}
	}

	public String toString() {
		return "Cine [getFecha_de_estreno()=" + getFecha_de_estreno() + ", getDuracion()=" + getDuracion()
				+ ", getTitulo()=" + getTitulo() + ", getTipo_de_metraje()=" + getTipoMetraje()
				+ ", formatoCorto()=" + formatoCorto() + "]";
	}
	
}
