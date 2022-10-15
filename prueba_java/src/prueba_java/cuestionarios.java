package prueba_java;
import java.time.LocalDate;

public class cuestionarios {
	      public static void main(String[] args) {
	         LocalDate f = LocalDate.of(2016, 3, 1);
	         LocalDate f1 = f.plusMonths(1);
	         System.out.println(f.getYear() + "|" + f1.getMonth() + "|" + f.getDayOfMonth());
	      }
	   }

