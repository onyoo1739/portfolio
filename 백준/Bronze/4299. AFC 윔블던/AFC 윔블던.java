import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    int sum = s.nextInt();
    int minus = s.nextInt();
    if((sum+minus)%2!=0||sum<minus){
      System.out.println(-1);
      s.close();
      return;
    }
    int team_a =(sum+minus)/2;
    int team_b = sum-team_a;
    if(Math.abs(team_a-team_b)!=minus){
        System.out.println(-1);
    }
    if(team_a>team_b){
      System.out.printf("%d %d",team_a,team_b);
    }
    else{
      System.out.printf("%d %d",team_b,team_a);

    }
    s.close();
  }
}
