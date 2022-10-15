package airbnb;

import java.time.LocalDate;
import java.util.Objects;


import uitles.Checkers;

public class airbnb {
	
	private int room_id, host_id;
	private double price;
	private boolean animal;
	private room_type room_type; 
	private String neighborhood, location;
	private LocalDate date;
	
	// room_id, host_id, room_type, animal, neighborhood, price, date, location
	
	
 	//Constructor 1: devuelve todos los atributos de la clase airbnb.
	
	public airbnb(int room_id, int host_id, room_type room_type, boolean animal, String neighborhood, Float price, LocalDate date, String location) {
		this.room_id = room_id;
		this.host_id = host_id;
		this.room_type = room_type;
		this.animal = animal;
		this.neighborhood = neighborhood;
		this.price = price;
		Checkers.checkFecha(date);
		this.date = date;
		this.location = location;
		
	}
	
	//Constructor 2: devuelve el room_id, el host_id del usuario y el precio y todos los demás datos los devuelve null.
	
	public airbnb(int room_id, int host_id, double price) {
		this.room_id = room_id;
		this.host_id = host_id;
		this.room_type = null;
		this.animal = false;
		this.neighborhood = null;
		this.price = price;
		this.date = null;
		this.location = null;
		
	}

	//Todas las propiedades son consultables y modificables.

	public int getRoom_id() {
		return room_id;
	}
	public void setRoom_id(int room_id) {
		this.room_id = room_id;
	}
	public int getHost_id() {
		return host_id;
	}
	public void setHost_id(int host_id) {
		this.host_id = host_id;
	}
	public double getPrice() {
		return price;
	}
	public void setPrice(double price) {
		this.price = price;
	}
	public boolean getAnimal() {
		return animal;
	}
	public void setAnimal(boolean animal) {
		this.animal = animal;
	}
	public String getNeighborhood() {
		return neighborhood;
	}
	public void setNeighborhood(String neighborhood) {
		this.neighborhood = neighborhood;
	}
	public String getLocation() {
		return location;
	}
	public void setLocation(String location) {
		this.location = location;
	}
	public LocalDate getDate() {
		return date;
	}
	public void setDate(LocalDate date) {
		Checkers.checkFecha(date);
		this.date = date;
	}
	public room_type getRoom_type() {
		return room_type;
	}
	public void set_room_type(room_type room_type){
		this.room_type = room_type;
	}
	
	//Propiedad Derivada: devuelve el precio de la habitación.
	
	public String precioHabitacion() {
		
		//Checkers.check("El precio de la habitación es negativo", getPrice() < 0.0);
		
		return "La habitación con id: " + getRoom_id() + " tiene un precio de " + getPrice() +"€.";
		
	}
	
	
	//ToString
	
	public String toString() {
		return "airbnb [getRoom_id()=" + getRoom_id() + ", getHost_id()=" + getHost_id() + ", getPrice()=" + getPrice()
				+ ", getAnimal()=" + getAnimal() + ", getNeighborhood()=" + getNeighborhood() + ", getLocation()="
				+ getLocation() + ", getDate()=" + getDate() + ", precioHabitacion()=" + precioHabitacion() + "]";
	}

	
	//Equals

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		airbnb other = (airbnb) obj;
		return animal == other.animal && Objects.equals(date, other.date) && host_id == other.host_id
				&& Objects.equals(location, other.location) && Objects.equals(neighborhood, other.neighborhood)
				&& Double.doubleToLongBits(price) == Double.doubleToLongBits(other.price) && room_id == other.room_id
				&& room_type == other.room_type;
	}
	
	//CompareTo: la habitación con mayor precio es mayor.
	
	public int compareTo(Object o) {
		  
		  airbnb  Airbnb = (airbnb) o; 
		  if (this.getPrice() == Airbnb.getPrice()) return 0; 
		  else if (this.getPrice() > Airbnb.getPrice()) return 1; 
		  else return -1; 
		}
	
	
}
