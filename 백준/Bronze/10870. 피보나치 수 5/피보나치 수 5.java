import java.util.Arrays;
import java.util.Scanner;

public class Main {

	/* f0  f1  f2  f3  f4  f5
	 * 0   1   1   2   3   5*/
	public static void main(String[] args) {
		int f0 = 0;
		int f1 = 1;
		int f2 = 0;
		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		if(n == 0) {
			System.out.println(0);
		}
		else if(n == 1) {
			System.out.println(1);
		}
		else {
			for(int i = 1; i<n; i++) {
				f2 = f1 + f0;
				f0 = f1;
				f1 = f2;
			}
			System.out.println(f2);
		}
	}

}
