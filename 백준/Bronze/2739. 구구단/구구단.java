import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n= sc.nextInt();
        for (int j =1; j<10; j++){
            System.out.printf("%d * %d = %d\n",n,j,n*j);
        }
        sc.close();
    }
}