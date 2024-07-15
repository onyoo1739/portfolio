import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    int N =s.nextInt(), m=s.nextInt(), M=s.nextInt(), T=s.nextInt(),R=s.nextInt();
    int cnt=0,P=m;
    if(Math.abs(M-m)<T){
      System.out.println(-1);
      return;
    }
    for(int i=0;i<N;cnt++){
      if(P+T<=M){
        P+=T;
        i++;
      }
      else{
        if (P-R>m){
          P-=R;
        }
        else{P=m;}
        }
    }
    System.out.println(cnt);
    s.close();
  }
}
