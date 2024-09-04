import java.util.*;
import java.lang.*;
import java.io.*;

 
class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
 
        int count = 0;
        
        int N = scanner.nextInt();
        int K = scanner.nextInt();

        int[] unit = new int[N];
        for(int i = 0; i < N; i++) {
            unit[i] =  scanner.nextInt();
        }

        for(int i = N - 1; i >= 0; i--) {
            if(K / unit[i] > 0) {
                count += K / unit[i];        
                K %= unit[i]; 
            }
        }

        System.out.println(count);
    }
}