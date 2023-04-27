import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n= sc.nextInt();
        long min =1000000;
        int max = -1000000;
        int Array [] = new int[n];
        for (int i =0; i<n;i++){
            Array[i] = sc.nextInt();
            if(max<Array[i]){
                max = Array[i];
            }
            if(min>Array[i]){
                min = Array[i];
            }
        }
        System.out.print(min +" "+ max);
        sc.close();
    }
}