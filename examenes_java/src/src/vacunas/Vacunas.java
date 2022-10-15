package vacunas;

import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class Vacunas {
	private Set<vacunado> vacunas;
	
	//Constructores
	
	public Vacunas() {
		vacunas = new HashSet<vacunado>();
	}
	
	public Vacunas(Set<vacunado> vacunas) {
		this.vacunas = new HashSet<vacunado>(vacunas);
	}
	
	public Vacunas (Stream<vacunado> vacunas) {
		this.vacunas = vacunas.collect(Collectors.toSet());
	}
	
	//M�todos
	public Boolean existeCumpleaños () {
		return vacunas.stream().anyMatch(v -> v.getFechaNacimiento().equals(v.getFechaAdministracion()));
	}
	
	public Double mediaEdad (String provincia, Boolean pauta) {
		return vacunas.stream().
				filter(v -> v.getProvincia().equals(provincia) && v.getPautaCompleta().equals(pauta)).
				mapToInt(v -> v.getEdad()).average().getAsDouble();
	}
	
	public Map<String, Set<tipoMarca>> getMarcaPorProvincia(){
		Map<String, Set<tipoMarca>> res = new HashMap<>();
		
		for (vacunado v : vacunas ) {
			if (res.containsKey(v.getProvincia())){
				res.get(v.getProvincia()).add(v.getMarca());
			}else {
				Set<tipoMarca> t = new HashSet<>();
				t.add(v.getMarca());
				res.put(v.getProvincia(), t);
			}
					
		}
		return res;
	}
	
	public List<String> nUsuariosVacunadosPorMarca(Integer n , tipoMarca marca){
		return vacunas.stream()
				.filter(v -> v.getMarca().equals(marca) && v.getPautaCompleta())
				.sorted(Comparator.comparing(vacunado::getEdad).thenComparing(vacunado::getFechaAdministracion).reversed())
				.limit(n)
				.map(vacunado::getUsuario)
				.collect(Collectors.toCollection(LinkedList::new));
	}
	
	public Map<String,Integer> masjovenVacunadoPorProvincia(){
		return vacunas.stream()
				.filter(v -> v.getPautaCompleta())
				.collect(Collectors.groupingBy(
						vacunado::getProvincia
						,Collectors.collectingAndThen(
								Collectors.minBy(Comparator.comparing(vacunado::getFechaNacimiento)
															.reversed()
															.thenComparing(Comparator.naturalOrder())), 
								minimo -> minimo.getEdad())));
	}
}
