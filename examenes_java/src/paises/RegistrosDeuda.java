package paises;

import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.SortedMap;
import java.util.SortedSet;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class RegistrosDeuda {
	List<RegistroDeuda> registros = new LinkedList<RegistroDeuda>();
	
	// CONSTRUCTOR 
	
	public RegistrosDeuda(Stream<RegistroDeuda> registro) {
		this.registros = registro.collect(Collectors.toList());
	}
	
	// MÉTODOS
	
	public SortedSet<String> getNombrePaisesEmpiezanCon(String s){
		return registros.stream()
				.filter(r -> r.getNombrePais().toLowerCase().startsWith(s.toLowerCase()))
				.map(RegistroDeuda::getNombrePais)
				.collect(Collectors.toCollection(TreeSet::new));
	}
	
	public String getPaisMasDeudaPerCapita(List<String> paises, Integer anyo) {
		return registros.stream()
				.filter(r -> paises.contains(r.getNombrePais()) && anyo == r.getFecha().getYear())
				.max(Comparator.comparing(RegistroDeuda::getDeudaPerCapita))
				.map(RegistroDeuda::getNombrePais)
				.orElse(null);
	}
	
	/*
	public SortedMap<String, List<RegistroDeuda>> getRegistrosPorPaisEnOrdenCronologico(){
		return registros.stream()
				.collect(Collectors.groupingBy(RegistroDeuda::getNombrePais,
						TreeMap::new, 
						Collectors.collectingAndThen(Collectors.toList(),
								lista -> lista.stream().sorted(Comparator.reverseOrder()).collect(Collectors.toList()))));
	}
	*/
	
	public SortedMap<String, Double> getPorcentajeCambioDeudaTotalPorPaises(){
		
	}
	
	
}
