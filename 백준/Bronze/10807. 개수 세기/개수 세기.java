import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n= sc.nextInt();
        int Array [] = new int[n];
        int cnt=0;
        for (int i =0; i<n ; i++){
            Array[i] = sc.nextInt();
        }
        int v = sc.nextInt();

        for(int i =0; i<n; i++){
            if(Array[i]==v){
                cnt++;
            }
        }
        System.out.println(cnt);
        sc.close();
    }
}