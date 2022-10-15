package fp.trenes;

import java.time.Duration;
import java.time.LocalTime;
import java.util.List;

public interface TrayectoTren extends Comparable<TrayectoTren>{
	
	String getCodigoTren();
	String getNombreTrayecto();
	TipoTren getTipo();
	List<String> getEstaciones();
	List<LocalTime> getHorasSalida();
	List<LocalTime> getHorasLlegada();
	LocalTime getHoraSalida();
	LocalTime getHoraLlegada();
	LocalTime getHoraSalida(String estación);
	LocalTime getHoraLlegada(String estacion);
	Duration getDuracionTrayecto();
	void añadirEstacionIntermedia(int posicion, String estacion, LocalTime horaLlegada, LocalTime horaSalida);
	void eliminarEstacionIntermedia(String estacion);
	
}
