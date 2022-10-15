package fp.vino;

import java.util.Collection;
import java.util.Comparator;
import java.util.HashSet;
import java.util.Map;
import java.util.Optional;
import java.util.Set;
import java.util.SortedMap;
import java.util.TreeMap;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import java.util.List;

import fp.utiles.Checkers;


public class Vinos {
	private Set<Vino> vinos;
	
	public Vinos(){
		this.vinos = new HashSet<Vino>();
	}
	
	public Vinos(Stream<Vino> vinos) {
		this.vinos = vinos.collect(Collectors.toSet());
	}
	
	public void agregarVino(Vino vino) {
		vinos.add(vino);
	}
	
	public void eliminarVino(Vino vino) {
		Checkers.check("Vino inexistente" + vino, vinos.remove(vino));
	}
	
	public Integer obtenerNumeroVinos() {
		return vinos.size();
	}
	
	public Boolean contieneVino(Vino vino) {
		return vinos.contains(vino);
	}
	
	public void agregarVinos(Collection<Vino> vinos) {
		this.vinos.addAll(vinos);
	}
	
	public Boolean contieneVinos(Collection<Vino> vinos) {
		return vinos.containsAll(vinos);
	}
	
	public Integer calcularNumeroVinosPais(String pais) {
		Long res = vinos.stream()
				.filter(vino -> vino.pais().equals(pais))
				.count();
		
		return res.intValue();
	}
	
	public Integer calcularNumeroVinosDePaisConPuntuacionSuperior(String pais, Integer umbralPuntos) {
		Long res = vinos.stream()
				.filter(vino -> vino.pais().equals(pais) && vino.puntos() > umbralPuntos)
				.count();
		
		return res.intValue();
	}
	
	public Set<Vino> obtenerVinosBaratos(Double precio){
		return vinos.stream().filter(vino -> vino.precio()<precio).collect(Collectors.toSet());
	}
	
	public Boolean existeVinoDeUvaEnRegion(String uva, String region) {
		return vinos.stream()
				.filter(vino -> vino.region().equals(region))
				.anyMatch(vino -> vino.uva().equals(uva)); //anyMatch te indica si existe
	}
	
	/*
	 public Set<Vino> calcularUvasDeRegion(String region){
		return vinos.stream().filter(vino -> vino.region().equals(region)).collect(Collectors.toSet());
	}			
	*/			
	
	public Integer calcularTotalPuntosVinosDeRegion(String region) {
		return vinos.stream().filter(vino -> vino.region().equals(region)).mapToInt(Vino::puntos).sum(); 
		//con el mapToInt convertimos el Stream en un IntStream, se hacce con una referencia del tipo (Tipo :: metodo de obtencion)
		}
	
	public Double calcularMediaPuntosVinosDeUva(String uva) {
		return vinos.stream().filter(vino -> vino.uva().equals(uva)).mapToInt(Vino::puntos).average().orElse(0.0); 
		//orElse sirve por si el registro está vacío, no calcularía la media y devolvería 0.0
	}
	
	public Vino obtenerVinoMejorPuntuado() {
		return vinos.stream().max(Comparator.comparing(Vino::puntos)).get();
	}
	
	public Vino obtenerVinoMejorPuntuadoPorPais(String pais){
		return vinos.stream().filter(vino -> vino.pais().equals(pais)).max(Comparator.comparing(Vino::puntos)).get();
	}
	
	public List<Vino> obtenerNVinosRegionOrdenadosPrecio(String region, Integer n){
		return vinos.stream().filter(vino -> vino.region().equals(region)).sorted(Comparator.comparing(Vino::precio).reversed()).limit(n).collect(Collectors.toList());
	}
	
	
	public Map <String, List<Vino>> agruparVinosPorPais() {
		return vinos.stream().collect(Collectors.groupingBy(Vino::pais));
	}
	
	public Map<String, Set<String>> agruparUvasPorPais(){
		return vinos.stream().collect(Collectors.groupingBy(Vino::pais, Collectors.mapping(Vino::uva, Collectors.toSet())));
	}
	
	public Map<String, Long> calcularCalidadPrecioPorRegionMayorDe(Double umbralMínimo){
		return vinos.stream()
				.filter(vino -> vino.getCalidadPrecio() > umbralMínimo)
				.collect(Collectors.groupingBy(Vino::region, Collectors.counting()));
	}
	
	public Map<String, Optional<Vino>> calcularVinoMasCaroPorPais(){
		return vinos.stream()
				.collect(Collectors.groupingBy(
						Vino::pais,
						Collectors.maxBy(Comparator.comparing(Vino::precio)))); 							
	}
	
	public SortedMap<String, List<Vino>> calcularNMejoresVinosPorPais(Integer n){
		
		Map<String, List<Vino>> vinosPorPais= agruparVinosPorPais();
		
		SortedMap<String, List<Vino>> res = new TreeMap<>();
		for (String pais: vinosPorPais.keySet()){
			List<Vino> mejoresVinos = vinosPorPais.get(pais).stream()
					.sorted(Comparator.comparing(Vino::puntos))
					.limit(n)
					.collect(Collectors.toList());
			res.put(pais, mejoresVinos);
		}
		return res;
	}
	
	public String calcularRegionConMejoresVinos(Double umbralMínimo){
		Map<String,Long> vinosMayorCalidad = calcularCalidadPrecioPorRegionMayorDe(umbralMínimo);
		
		return vinosMayorCalidad.keySet().stream()
				.max(Comparator.comparing(r -> vinosMayorCalidad.get(r)))
				.orElse(null);
		
	}
	
}
