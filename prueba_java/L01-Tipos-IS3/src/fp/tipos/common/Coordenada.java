package fp.tipos.common;

public record Coordenada(Double latitud, Double longitud) {
	
	static final Double RADIO_TIERRA = 6371.0;
	
	// Otras operaciones
	public Double getDistancia(Coordenada c) {
		Double difLat = c.latitud() - latitud();
		Double difLong = c.longitud() - longitud();
		return Math.sqrt(difLat*difLat + difLong+difLong);
	}
	
	public Double getDistanciaHaversine(Coordenada c) {
		Double difLat = Math.toRadians(c.latitud()-latitud());
	    Double difLon = Math.toRadians(c.longitud()-longitud());
	    Double a = Math.pow(Math.sin(difLat/2),2) +
	    		   Math.cos(Math.toRadians(latitud())) * 
	    		   Math.cos(Math.toRadians(c.latitud())) *
	    		   Math.pow(Math.sin(difLon/2),2);
	    Double calc = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
	    return RADIO_TIERRA*calc;
	}
	
}
