package fp.tipos.hoteles;

import fp.tipos.common.Coordenada;

public record Hotel(String nombre, String direccion, String ciudad, String telefono,
		String cadenaHotelera, String descripcion, CategoriaHotelera categoriaHotelera, 
		TipoAlojamiento tipoAlojamiento, CategoriaPrecio categoriaPrecio, Float puntuacion, 
		Integer comentarios, Boolean mascotas, Boolean adaptado, Coordenada coordenadas) {

	//C2: recibe el nombre, la direcci n, la ciudad, el tel fono, la cadena hotelera, y la categor a, y permite
	//crear un hotel de precio medio, sin ning n comentario de los usuarios, que no admite mascotas ni est 
	//adaptado.
	public Hotel(String n, String d, String ciud, String tel, String cadena, CategoriaHotelera cat) {
		this(n, d, ciud, tel, cadena, null, cat, null, CategoriaPrecio.MEDIA, null, 0, false, false, null);
	}
	
	//C3: recibe el nombre, la cadena hotelera y la categor a del hotel, y permite crear un hotel de precio
	//medio, sin comentarios, que no admite mascotas ni est  adaptado (el resto de las propiedades b sicas
	//quedar n con el valor null).
	public Hotel(String n, String cadena, CategoriaHotelera cat) {
		this(n, null, null, null, cadena, null, cat, null, CategoriaPrecio.MEDIA, null, null, false, false, null);
	}
	
	public String getCadenaConFormato() {
		String estrellas = calcularEstrellas(categoriaHotelera());
		return nombre() + " (" + estrellas + ") ";
	}
	
	private String calcularEstrellas(CategoriaHotelera categoriaHotelera) {
		String res = "";
		switch(categoriaHotelera) {
		case CINCO:
			res = "*****";
			break;	
		case CUATRO:
			res = "****";
			break;
		case TRES:
			res = "***";
			break;
		case DOS:
			res = "**";
			break;
		case UNO:
			res = "*";
			break;
		case OTROS:
			res = "N/A";
			break;
		}		
		return res;
	}
	


}

	
	
