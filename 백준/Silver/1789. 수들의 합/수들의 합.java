import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        long S = scanner.nextLong();

        // 유튜브 프리미ㅏ엄???
        // 55 : 1~10까지 합
        // 54
        // x 2 3 4 5 6 7 8 9 10
        // 52
        // 1 2 x 4 5 6 7 8 9 10
        // 23
        // 1 2 3 4 6 7 

        long sum = 0;
        int i = 1;
        while(sum < S) {
            sum += i;
            i++;
            // System.out.println(sum);
        }

        
        if(sum == S) {
            System.out.println(i - 1); //i가 1 증가하고 끝나기때문에 1을 지움
            // System.out.println("같음");
        }
        if(sum != S) {
            for(int j = 1; j < i - 2; j++) {
                long s = sum - j;
                if(s == S) {
                    break;
                    
                }
                else {
                    sum += j;
                }
            }
            System.out.println(i - 2);
            // System.out.println("다름");
        }
        
    }
}