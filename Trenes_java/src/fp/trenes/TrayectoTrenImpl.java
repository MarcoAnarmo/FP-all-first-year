package fp.trenes;

import java.time.Duration;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
//import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Objects;


import fp.utiles.Checkers;
import fp.utiles.Validators;


public class TrayectoTrenImpl implements TrayectoTren {
	
	private String codigoTren;
	private String nombreTrayecto;
	private TipoTren tipo;
	private List<String> estaciones;
	private List<LocalTime> horasSalida;
	private List<LocalTime> horasLlegada;
	
	// PRIMER CONSTRUCTOR
	public TrayectoTrenImpl(String codigoTren, String nombreTrayecto, TipoTren tipo, String origen, String destino, LocalTime horaSalida, LocalTime horaLlegada) {
		
		Checkers.check("El código dell tren no está formado por 5 dígitos", esCodigoTrenOK(codigoTren));
		Checkers.checkNoNull(horaSalida, horaLlegada);
		Checkers.check("La hora de salida no es anterior a la de llegada", horaSalida.isBefore(horaLlegada));
		
		this.codigoTren = codigoTren;
		this.nombreTrayecto = nombreTrayecto;
		this.tipo = tipo;
		
		this.estaciones = new LinkedList<String>();
		estaciones.add(origen);
		estaciones.add(destino);
		
		this.horasSalida = new LinkedList<LocalTime>();
		horasSalida.add(horaSalida);
		horasSalida.add(null);
		
		this.horasLlegada = new LinkedList<LocalTime>();
		horasLlegada.add(null);
		horasLlegada.add(horaLlegada);
		
	}
	
	// CONDICION DEL PRIMER CHECKER
	private Boolean esCodigoTrenOK(String codigo) {
		return codigo.length() == 5 && Validators.sonDigitos(codigo);
	}
	
	// GETTERS
	public String getCodigoTren() {
		return codigoTren;
	}

	public String getNombreTrayecto() {
		return nombreTrayecto;
	}

	public TipoTren getTipo() {
		return tipo;
	}

	public List<String> getEstaciones() {
		return estaciones;
	}

	public List<LocalTime> getHorasSalida() {
		return horasSalida;
	}

	public List<LocalTime> getHorasLlegada() {
		return horasLlegada;
	}
	
	// PROPIEDADES DERIVADAS
	public LocalTime getHoraSalida() {
		return horasSalida.get(0);
	}
	public LocalTime getHoraLLegada() {
		return horasLlegada.get( horasLlegada.size() - 1 );
	}
	public Duration getDuracionTrayecto() {
		return Duration.between(getHoraSalida(), getHoraLLegada());
	}
	public LocalTime getHoraSalida(String estacion) {
		LocalTime res = null;
		int pos = estaciones.indexOf(estacion);
		if (pos >= 0) {
			res = horasSalida.get(pos);
		}
		return res;
	}
	public LocalTime getHoraLlegada(String estacion) {
		LocalTime res = null;
		int pos = estaciones.indexOf(estacion);
		if (pos >= 0) {
			res = horasLlegada.get(pos);
		}
		return res;
	}
	public void anadirEstacionIntermedia(int posicion, String nombre, LocalTime horaLLegada, LocalTime horaSalida) {
		Checkers.check("la posicion intermedia no está entre 1 y n", posicion > 0 && posicion<=estaciones.size() - 1);
		Checkers.check("La hora de salida no es posterios a la de llegada", horaSalida.isAfter(horaLLegada));
		Checkers.check("Hora llegada nos es posterior a hora salida estacion anterior", horaLLegada.isAfter(horasSalida.get(posicion-1)));
		Checkers.check("Hora salida no es anterior a hora llegada estación posterior", horaSalida.isBefore(horasLlegada.get(posicion)));
		estaciones.add(posicion, nombre);
		horasSalida.add(posicion, horaSalida);
		horasLlegada.add(posicion, horaLLegada);
	}
	public void eliminarEstacionIntermedia(String estacion) {
		int index = estaciones.indexOf(estacion);
		Checkers.check("La estación no está en el trayecto", index != -1);
		Checkers.check("La estacion a eliminar no puede ser la primera", index != 0);
		Checkers.check("La estación a eliminar no puede ser la última", index != estaciones.size()-1);
		estaciones.remove(index);
		horasLlegada.remove(index);
		horasSalida.remove(index);
	}

	public int hashCode() {
		return getCodigoTren().hashCode() + 31*getNombreTrayecto().hashCode() + 13*getHoraSalida().hashCode();
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		TrayectoTrenImpl other = (TrayectoTrenImpl) obj;
		return Objects.equals(codigoTren, other.codigoTren) && Objects.equals(estaciones, other.estaciones)
				&& Objects.equals(horasLlegada, other.horasLlegada) && Objects.equals(horasSalida, other.horasSalida)
				&& Objects.equals(nombreTrayecto, other.nombreTrayecto) && tipo == other.tipo;
	}

	public int compareTo(TrayectoTren tt) {
		int res = getNombreTrayecto().compareTo(tt.getNombreTrayecto());
		if (res == 0) {
			res = getHoraSalida().compareTo(tt.getHoraSalida());
			if (res == 0) {
				res = getCodigoTren().compareTo(tt.getCodigoTren());
			}
		}
		return res;
	}
	public String toString() {
		String res = getNombreTrayecto() + "-" + getTipo() + " (" + getCodigoTren() + ")\n";
		for (int i = 0; i < estaciones.size(); i++) {
			res += "\t" + estaciones.get(i) + "\t" + formateaHora(horasLlegada.get(i)) + "\t" + formateaHora(horasSalida.get(i)) + "\n";
		}
		return res;
	}
	private String formateaHora(LocalTime hora) {
		String res = "		";
		if( hora != null) {
			res = hora.format(DateTimeFormatter.ofPattern("hh:mm"));
		}
		return res;
	}

	@Override
	public LocalTime getHoraLlegada() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public void añadirEstacionIntermedia(int posicion, String estacion, LocalTime horaLlegada, LocalTime horaSalida) {
		// TODO Auto-generated method stub
		
	}
	
}
