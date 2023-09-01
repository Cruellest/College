
import java.util.Scanner;
class poligono{
	
	private String nome;
	private int numero;
	public poligono(String nome, int numero) {
		super();
		this.nome = nome;
		this.numero = numero;
	}
	public String getNome() {
		return nome;
	}
	public int getNumero() {
		return numero;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public void setNumero(int numero) {
		this.numero = numero;
	}
	
}

 class Quadrado extends poligono{
	 
	private double lado;
	public Quadrado(String nome,int numero,double lado) {
		super(nome, numero);
		this.lado = lado;	
	}

	public double getLado() {
		return lado;
	}

	public void setLado(double lado) {
		this.lado = lado;
	}
	
	public double calcularArea() {
		return (lado*lado);
	}

	@Override
	public String toString() {
		return String.format("%s tem %d lados e area= %.1f",getNome(),getNumero(),calcularArea());
	}
		
	
 }
 
 
 public class Main {

		public static void main(String[] args) {

			Scanner scan = new Scanner(System.in);
				
			String nome = scan.next();
			int numero = scan.nextInt();
			double teste = scan.nextDouble();
			
			Quadrado q1= new Quadrado(nome,numero,teste);
			
			System.out.println(q1);
			
			q1.setLado(scan.nextDouble());

			System.out.println(q1);

		}

	}