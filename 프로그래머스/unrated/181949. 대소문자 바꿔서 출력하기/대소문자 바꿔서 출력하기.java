import java.util.Scanner;
import static java.lang.Character.*;
public class Solution {
     public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String newA="";
        for (int i = 0; i <a.length() ; i++) {
            char c = a.charAt(i);
            if(isUpperCase(c)){
                c= toLowerCase(c);
                newA+=c;
            }else{
                c=toUpperCase(c);
                newA+=c;
            }

        }
        System.out.println(newA);
    }
}