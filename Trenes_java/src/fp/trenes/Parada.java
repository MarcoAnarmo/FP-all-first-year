package fp.trenes;

import java.time.LocalTime;

public record Parada(String estacion, LocalTime horaSalida, LocalTime horaLlegada) {

}
