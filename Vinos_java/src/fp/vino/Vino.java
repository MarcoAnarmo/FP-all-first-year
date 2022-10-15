package fp.vino;
import fp.utiles.Checkers;

public record Vino(String pais, String region, Integer puntos, Double precio, String uva) {
	
	public Vino{
		Checkers.check("Los puntos deben estra entre el cero y el cien", puntos >= 0 && puntos <= 100);
		Checkers.check("El precio debe ser mayor que cero", precio > 0 );
	}
	
	public Double getCalidadPrecio() {
		return puntos/precio;
	}
	
	
}
