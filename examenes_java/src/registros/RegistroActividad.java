package registros;

import java.time.Duration;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;

public class RegistroActividad {
	//atributos
	private String usuario;
	private tipoActividad tipo;
	private Boolean RegistroRuta;
	private List<LocalDateTime> horas;
	private List<Coordenada> coordenadas;
	private List<Double> alturas;
	private Double alturaMaxima;
	private Double distancia;
	private Duration duracion;
	private LocalDateTime inicio;
	private LocalDateTime fin;
	private LocalDate fecha;
	
	//CONSTRUCTOR 2
	public RegistroActividad(String usuario, tipoActividad tipo, List<LocalDateTime> horas, List<Coordenada> coordenadas,List<Double> alturas) {
		Checkers.check("", horas.size()==coordenadas.size() && horas.size() == alturas.size());
		Checkers.check("", horas.size()>=2);
		Checkers.check("", sonHorasOK(horas));
		
	}

	private Boolean sonHorasOK(List<LocalDateTime> horas2) {
		Boolean res = true;
		
		return res;
	}
	
	
	
}
