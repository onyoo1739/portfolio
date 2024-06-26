import java.util.Scanner;

public class Main {
  public static void print_backnum(int[] num){
    for(int j=0;j<10;j++){
      System.out.printf("%d ",num[j]);
    }
    System.out.println();
  }
  public static int judge(int[] num){
    for(int i=0;i<10;i++){
      if(num[i]==18) return 1;
    }
    return 0;
  }
  public static void main(String[] args) {

    Scanner s = new Scanner(System.in);
    int n = s.nextInt();
    int[] num = new int[10];
    for(int i=0;i<n;i++){
      int cnt=0;
      for(int j=0;j<10;j++){
        num[j]=s.nextInt();
        if(num[j]==17||num[j]==18){
        cnt++;
        }
      }
      if(cnt ==0){
        print_backnum(num);
        System.out.println("none");
        System.out.println();
      }
      else if (cnt == 1 ){
        print_backnum(num);
        if(judge(num)==1) {
          System.out.println("mack");
           System.out.println();
        }
        else if(judge(num)==0) {
          System.out.println("zack");
          System.out.println();
        }
      }
      else if(cnt >=2){
        print_backnum(num);
        System.out.println("both");
        System.out.println();
        }
      }
    s.close();
  }
}
