package test01;

import java.util.Scanner;

public class BaekJoon_2525 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int h = sc.nextInt();
		int m = sc.nextInt();
		int t = sc.nextInt();
		
		if ((m+t >= 60) && ((m+t)/60 + h >= 24)) {
			System.out.println((m+t)/60+h-24 + " " + (m+t)%60);
		}
		else if (m+t >= 60) {
			System.out.println((m+t)/60+h + " " + (m+t)%60);
		}
		else {
			System.out.println((m+t)/60+h + " " + (m+t));
		}
			
		sc.close();
	}

}
