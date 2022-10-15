package airbnb;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import uitles.Checkers;

public class ListaAirbnb {
	private String barrio;
	private List<airbnb>localizaciones;
	
	
	// ###############################   ENTREGA 2   #########################################
	
	
	//Constructor 1: devuelve un barrio y la lista vacía.
	
	public ListaAirbnb(String barrio) {
		this.barrio = barrio;
		this.localizaciones = new ArrayList<airbnb>();
		
	}
	
	//Constructor 2: devuelve el barrio y la lista con todas las localizaciones dadas.
	
	public ListaAirbnb(String barrio, List<airbnb> localizaciones) {
		this.barrio = barrio;
		this.localizaciones = new ArrayList<airbnb>();
		this.localizaciones.addAll(localizaciones);
		
	}
	//Constructor 3: recibe un string barrio y un stream y devuelve un titulo default con una lista de todas las localizaciones dadas.
	
	public ListaAirbnb(String barrio, Stream<airbnb> localizaciones) {
		this.barrio = barrio;
		this.localizaciones = localizaciones.collect(Collectors.toList());
	}
	
	//Añadir un barrio a la lista.
	
	public void incorpora(airbnb b) {
		this.localizaciones.add(b);
	}
	
	//Añadir una lista de barrios a la lista.
	
	public void incorpora(ListaAirbnb l) {
		this.localizaciones.addAll(l.getLocalizaciones());
	}
	public void incorpora(List<airbnb> l) {
		this.localizaciones.addAll(l);
	}
	//Eliminar un barrio de la lista.
	
	public void eliminarPrimera(airbnb b) {
		Checkers.check("El barrio está en la lista", localizaciones.contains(b));
		this.localizaciones.remove(b);
	}
	public void eliminarUltima(airbnb b) {
		Checkers.check("El barrio no está en la lista", localizaciones.contains(b));
		int idx = this.localizaciones.lastIndexOf(b);
		this.localizaciones.remove(idx);
	}
	
	//Getters and Setters
	
	public String getBarrio() {
		return barrio;
	}

	public void setBarrio(String barrio) {
		this.barrio = barrio;
	}
	
	//La lista es solo consultable
	
	public List<airbnb> getLocalizaciones() {
		return new ArrayList<airbnb>(this.localizaciones);
	}
	
	//Constructor: devuelve la longitud de la lista
	
	public Integer numeroBarrios() {
		
		return this.getLocalizaciones().size();
		
	}
	

	//toString, hashCode, equals
	
	/*
	public String toString() {
		return this.getBarrio() + " contiene (" + this.numeroBarrios() + " barrios)" ;
	}
	 */
	
	public int hashCode() {
		return Objects.hash(barrio, localizaciones);
	}

	
	public String toString() {
		return "ListaAirbnb [barrio=" + barrio + ", localizaciones=" + localizaciones + "]";
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		ListaAirbnb other = (ListaAirbnb) obj;
		return Objects.equals(barrio, other.barrio) && Objects.equals(localizaciones, other.localizaciones);
	}
	
	//Obtener si existe un barrio
	
	public Boolean existeBarrio(airbnb a) {
		return this.localizaciones.contains(a);
	}
	
	//Obtener si existen un conjunto de barrios
	
	public  Boolean existeBarrios(Collection<airbnb> a) {
		return this.localizaciones.containsAll(a);
	}
	
	//Obtener el número de veces que se registra el barrio.
	
	public Integer numeroDeRegistrosBarrios(String barrio) {
		int cont = 0;
		
		for (airbnb a : this.localizaciones) {
			if (a.getNeighborhood() == barrio) {
				cont ++;
			}
		}
		return cont;
	}
	
	//Filtramos por el barrio dado como parámetro y devuelve una lista con con los objetos filtrados por el barrio recibido.
	
	public List<airbnb> filtroPorBarrio(String barrio){
		List<airbnb> res = new ArrayList<airbnb>();
		
		for (airbnb a : this.localizaciones) {
			if (a.getNeighborhood() == barrio) {
				res.add(a);
			}
		}
		
		return res;
	}
	
	//Map donde asocia a cada barrio sus objetos airbnb asociados en una lista.
	
	public Map<String, List<airbnb>> agruparPorBarrios(){
		
		Map<String, List<airbnb>> res = new HashMap<String, List<airbnb>>();
		
		for ( airbnb a : this.localizaciones) {
			if (res.containsKey(a.getNeighborhood())) {
				
				res.get(a.getNeighborhood()).add(a);
				
			}else {
				List<airbnb> lista = new ArrayList<airbnb>();
				lista.add(a);
				res.put(a.getNeighborhood(), lista);
			}
		}
		return res;
	}
	
	//Map donde asocia a cada barrio el conteo de las veces que aparece.
	
	public Map<String, Integer> conteoDeBarrios(){
		
		Map<String, Integer> res = new HashMap<String, Integer>();
		
		
		for ( airbnb a : this.localizaciones) {
			if (res.containsKey(a.getNeighborhood())) {
				
				int cont = res.get(a.getNeighborhood());
				
				cont++;
				
				res.put(a.getNeighborhood(), cont);
				
			}else {
				
				res.put(a.getNeighborhood(), 1);
			}
		}
		return res;
		
	}
	
	// ###############################   ENTREGA 3   #########################################
	
	
	//Obtener el número de veces que se registra el barrio.
	
	public Integer numeroDeRegistrosBarriosS(String barrio) {
		Long res = this.localizaciones.stream()
				.filter(x -> x.getNeighborhood().equals(barrio))
				.count();

		return res.intValue();
				
	}
	
	//Filtramos por el barrio dado como parámetro y devuelve una lista con con los objetos filtrados por el barrio recibido.
	
	public List<airbnb> filtroPorBarrioS(String barrio){
		return this.localizaciones.stream()
				.filter(x -> x.getNeighborhood().equals(barrio))
				.collect(Collectors.toList());
	}
	
	//Map donde asocia a cada barrio sus objetos airbnb asociados en una lista.
	
	public Map<String, List<airbnb>> agruparPorBarriosS(){
		return this.localizaciones.stream()
				.collect(Collectors.groupingBy(airbnb::getNeighborhood));
	}
	
	//Map donde asocia a cada barrio el conteo de las veces que aparece.
	
	public Map<String, Long> conteoDeBarriosS(){
		
		return this.localizaciones.stream()
				.collect(Collectors.groupingBy(airbnb::getNeighborhood, Collectors.counting()));
	}
	
}



















