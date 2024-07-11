import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    int h= s.nextInt();
    int m = s.nextInt();
    int w= 0;
    if(h>=20&&h<=23){
      w = m+24-h;
    }
    else if (h>=0&&h<=3){
      w=m-h;
    }
    System.out.printf("%d",w);
    s.close();
  }
}
