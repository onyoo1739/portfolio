class TV
{
	private String company;
	private int year; 
	private int inch;
	
	public String TV() {}
	public TV(String company, int year, int inch)
	{
		this.company = company;
		this.year = year;
		this. inch = inch;
	}
	public void show()
	{
		System.out.printf("%s에서 만드는 %d년형 %d인치 TV",company,year,inch);
	}
}
public class printTv {
	public static void main(String [] args)
	{
		TV myTV = new TV("LG", 2017, 32);
		myTV.show();
	}
}
