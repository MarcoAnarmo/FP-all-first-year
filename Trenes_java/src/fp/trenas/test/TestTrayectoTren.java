package fp.trenas.test;

import java.time.LocalTime;

import fp.trenes.TipoTren;
import fp.trenes.TrayectoTren;
import fp.trenes.TrayectoTrenImpl;

public class TestTrayectoTren {
	public static void main(String[] args) {
		TrayectoTren tt = new TrayectoTrenImpl("02471", "Sevilla-Madrid", TipoTren.AV_CITY, "SEVILLA-SANTA JUSTA", "MADRID-PUERTO DE ATOCHA"
				, LocalTime.of(1, 0), LocalTime.of(10,2));
		
		System.out.println(tt);
		
	}
}
