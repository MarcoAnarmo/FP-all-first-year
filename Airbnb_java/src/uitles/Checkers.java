package uitles;

import java.time.LocalDate;

public class Checkers {
	
	public static void check(String textoRestriccion, Boolean condicion) {
		   if (!condicion) {
		      throw new IllegalArgumentException(
			   Thread.currentThread().getStackTrace()[2].getClassName()
	 	   + "." +
			   Thread.currentThread().getStackTrace()[2].getMethodName() 
	 		   + ": " + textoRestriccion);
		   }
		}

		public static void checkNoNull(Object... parametros) {
		   for (int i = 0; i < parametros.length; i++) {
			if (parametros[i] == null) {
			   throw new IllegalArgumentException(Thread.currentThread().getStackTrace()[2].getClassName()
	 		+ "." + Thread.currentThread().getStackTrace()[2].getMethodName() + ": el parámetro " + (i + 1) + " es nulo");
			}
		   }
		}
		
		//la fecha no puede ser anterior a 2017
		public static void checkFecha(LocalDate fecha) { 
			
			if (fecha.getYear() < 17) {
				
				throw new IllegalArgumentException("La fecha no puede ser anterior a 2017");
				
			}
		}
}




