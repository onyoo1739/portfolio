import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n= sc.nextInt();
        int long_ = n/4;
        for (int i =0; i<long_;i++){
            System.out.print("long ");
        }
        System.out.print("int");
        sc.close();
    }
}