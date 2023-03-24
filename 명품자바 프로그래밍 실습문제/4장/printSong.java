class Song
{
	private String title, artist, country;
	private int year;
	
	public String Song() {}
	
	public Song(String title, String artist, int year, String country)
	{
		this.title = title;
		this.artist = artist;
		this.year= year;
		this.country = country;
	}
	public void show()
	{
		System.out.printf("%d년 %s국적의 %s가 부른 %s", year, country, artist, title);
	}
}


public class printSong {

	public static void main(String[] args) 
	{
		Song song = new Song("Dancing Queen", "ABBA", 1978,"스웨덴");
		song.show();
	}

}
