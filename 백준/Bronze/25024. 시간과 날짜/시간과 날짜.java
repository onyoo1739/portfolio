import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    int T = s.nextInt();
    for(int i=0;i<T;i++){
      int x = s.nextInt();
      int y = s.nextInt();
      if(x>=0&&x<=23&&y>=0&&y<=59){
        System.out.printf("Yes ");
      }
      else{
        System.out.printf("No ");
      }
      if(x>=1&&x<=12&&y>=1&&y<=31){
        if((x==4||x==6||x==9||x==11)&&y>30){
            System.out.printf("No\n");
        }
        else if(x==2&&y>29){
            System.out.printf("No\n");
        }
        else{
          System.out.printf("Yes\n");
        }
      }
      else{
        System.out.printf("No\n");
      }
    }
    s.close();
  }
}
