package test01;

import java.util.Scanner;

public class BaekJoon_2480 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();

		if (a == b && b == c) {
			System.out.println(10000 + 1000 * a);
		}
		else if ((a == b && b != c)) {
			System.out.println(1000+100*a);
		}
		else if ((b == c && a != b)) {
			System.out.println(1000+100*b);
		}
		else if ((a == c && a != b)) {
			System.out.println(1000+100*c);
		}
		else {
			if (a>=b && a>=c) {
				System.out.println(100*a);
			}
			else if (b >= a && b >= c){
				System.out.println(100*b);
			}
			else {
				System.out.println(100*c);
			}
		}

		sc.close();

	}

}
