package vacunas;

import java.time.LocalDate;
import java.util.Objects;

public class vacunado {
	
	//Atributos
	private String usuario;
	private LocalDate fechaNacimiento;
	private String provincia;
	private tipoMarca marca ;
	private LocalDate fechaAdministracion;
	private Boolean pautaCompleta;
	
	//Constructores
	public vacunado(String usuario, LocalDate fechaNacimiento, String provincia, tipoMarca marca, LocalDate fechaAdministracion, Boolean pautaCompleta) {
		
		this.usuario = usuario;
		this.fechaNacimiento = fechaNacimiento;
		this.provincia = provincia;
		this.marca = marca;
		this.fechaAdministracion = fechaAdministracion;
		this.pautaCompleta = pautaCompleta;
	}

	@Override
	public String toString() {
		return "vacunado [usuario=" + usuario + ", fechaNacimiento=" + fechaNacimiento + ", provincia=" + provincia
				+ ", marca=" + marca + ", fechaAdministracion=" + fechaAdministracion + ", pautaCompleta="
				+ pautaCompleta + "]";
	}

	@Override
	public int hashCode() {
		return Objects.hash(fechaAdministracion, fechaNacimiento, marca, pautaCompleta, provincia, usuario);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		vacunado other = (vacunado) obj;
		return Objects.equals(fechaAdministracion, other.fechaAdministracion)
				&& Objects.equals(fechaNacimiento, other.fechaNacimiento) && marca == other.marca
				&& Objects.equals(pautaCompleta, other.pautaCompleta) && Objects.equals(provincia, other.provincia)
				&& Objects.equals(usuario, other.usuario);
	}

	public String getUsuario() {
		return usuario;
	}

	public void setUsuario(String usuario) {
		this.usuario = usuario;
	}

	public LocalDate getFechaNacimiento() {
		return fechaNacimiento;
	}

	public void setFechaNacimiento(LocalDate fechaNacimiento) {
		this.fechaNacimiento = fechaNacimiento;
	}

	public String getProvincia() {
		return provincia;
	}

	public void setProvincia(String provincia) {
		this.provincia = provincia;
	}

	public tipoMarca getMarca() {
		return marca;
	}

	public void setMarca(tipoMarca marca) {
		this.marca = marca;
	}

	public LocalDate getFechaAdministracion() {
		return fechaAdministracion;
	}

	public void setFechaAdministracion(LocalDate fechaAdministracion) {
		this.fechaAdministracion = fechaAdministracion;
	}

	public Boolean getPautaCompleta() {
		return pautaCompleta;
	}

	public void setPautaCompleta(Boolean pautaCompleta) {
		this.pautaCompleta = pautaCompleta;
	}
	
	public Integer getEdad() {
		Integer edad = LocalDate.now().getYear() - getFechaNacimiento().getYear();
		return edad;
	}
	
	
	
	
	
}
