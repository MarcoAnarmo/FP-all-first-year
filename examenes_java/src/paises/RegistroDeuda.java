package paises;

import java.time.LocalDate;

public class RegistroDeuda {
	// ATRIBUTOS
	
	private String nombrePais;
	private LocalDate fecha;
	private Integer deudaTotal;
	private Double deudaPorcentajePIB;
	private Integer deudaPerCapita;
	
	// C2
	
	public RegistroDeuda(String cadena) {
		String[] trozos = cadena.split(",");
		Checkers.check("", trozos.length == 5);
		
		String nombre = trozos[0].trim();
		Integer anyo = Integer.parseInt(trozos[1].trim());
		LocalDate fecha = LocalDate.of(anyo, 1, 1);
		Integer deuda = Integer.parseInt(trozos[2].trim());
		Double porcentajePIB = Double.parseDouble(trozos[3].trim());
		Integer deudaHabitante = Integer.parseInt(trozos[4].trim());
		
		Checkers.check("", fecha.compareTo(LocalDate.of(1945,1,1))>= 0);
		
		this.nombrePais=nombre;
		this.fecha = fecha;
		this.deudaTotal = deuda;
		this.deudaPorcentajePIB = porcentajePIB;
		this.deudaPerCapita = deudaHabitante;
		
	}
	
	// GETTERS & SETTERS
	
	public String getNombrePais() {
		return nombrePais;
	}

	public void setNombrePais(String nombrePais) {
		this.nombrePais = nombrePais;
	}

	public LocalDate getFecha() {
		return fecha;
	}

	public void setFecha(LocalDate fecha) {
		this.fecha = fecha;
	}

	public Integer getDeudaTotal() {
		return deudaTotal;
	}

	public void setDeudaTotal(Integer deudaTotal) {
		this.deudaTotal = deudaTotal;
	}

	public Double getDeudaPorcentajePIB() {
		return deudaPorcentajePIB;
	}

	public void setDeudaPorcentajePIB(Double deudaPorcentajePIB) {
		this.deudaPorcentajePIB = deudaPorcentajePIB;
	}

	public Integer getDeudaPerCapita() {
		return deudaPerCapita;
	}

	public void setDeudaPerCapita(Integer deudaPerCapita) {
		this.deudaPerCapita = deudaPerCapita;
	}
	
	// PROPIEDADES DERIVADAS
	
	public Integer getPoblacionAprox() {
		Double res = (getDeudaTotal().doubleValue() / getDeudaPerCapita());
		return (int) Math.ceil(res);
	}
	
	public Integer getPIBAprox() {
		Double res = (getDeudaTotal()*getDeudaPorcentajePIB()/100);
		return (int) Math.floor(res);
	}
	
	// COMPARETO
	
	public int compareTo(RegistroDeuda r) {
		int res = getNombrePais().compareTo(r.getNombrePais());
		if (res == 0) {
			res = getFecha().compareTo(r.getFecha());
		}
		return res;
	}
}
