package registros;

public record Coordenada(Double Latitud, Double Longitud) {
	
	private Double getMediaLatitudDada(Double latitutd2) {
		return this.Latitud/latitutd2;
	}
	
}
