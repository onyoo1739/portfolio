import java.util.Scanner;

class C
{
	private double x,y;
	private int radius;
	public C() {}
	public C(double x, double y, int radius)
	{
		this.x = x;
		this.y= y;
		this.radius = radius;
	}
	
	public int rd()
	{
		return radius;
	}
	
	public void show() {
		System.out.printf("가장 면적이 큰 원은 (%.1f,%.1f)%d\n", x, y, radius);
	}
	
}


public class bigCircle {

	public static void main(String[] args) 
	{
		Scanner scanner = new Scanner(System.in);
		C c [];
		c =  new C[3];
		int max =  0;
		
		for (int i =0; i<c.length;i++)
		{
			System.out.print("x, y, radius >>");
			double x = scanner.nextDouble();
			double y = scanner.nextDouble();
			int radius = scanner.nextInt();
			c[i]= new C(x,y,radius);
		}
		for (int i =0; i<c.length ; i++)
		{
			if (c[max].rd()<c[i].rd())
				max = i;
		}
		c[max].show();
		scanner.close();
		
				
	}

}
