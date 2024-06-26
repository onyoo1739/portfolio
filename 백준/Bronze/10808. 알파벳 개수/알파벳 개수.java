import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
      Scanner s = new Scanner(System.in);
      String word;
      int[] cnt= new int[26];
      for(int i=0;i<26;i++){
        cnt[i] = 0;
      }
      word = s.nextLine();
      for(int i = 0; i < word.length(); i++){
        char c = word.charAt(i);
        cnt[c-'a']+=1;
      }
      for(int i=0;i<26;i++){
        System.out.printf("%d ",cnt[i]);
      }
      s.close();
    }
}
