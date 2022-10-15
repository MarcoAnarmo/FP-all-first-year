package fp.tipos.hoteles.test;

import fp.tipos.common.Coordenada;
import fp.tipos.hoteles.CategoriaHotelera;
import fp.tipos.hoteles.CategoriaPrecio;
import fp.tipos.hoteles.Hotel;
import fp.tipos.hoteles.TipoAlojamiento;

public class TestHotel {

	public static void main(String[] args) {
		Hotel h1 = new Hotel("Ál Andalus", "NH", CategoriaHotelera.CUATRO);
		System.out.println(h1);
	}

}
