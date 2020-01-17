package project1;

import java.util.Scanner;
public class S22011 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int num = 0;
		int count = 0;
		num = scan.nextInt();
		String[] studentAns = new String[num];
		String[] teacherAns = new String[num];
		
		for (int i=0; i<num; i++){
			studentAns[i] = scan.next();
		}
		for (int j=0; j<num; j++){
			teacherAns[j] = scan.next();
		}
		
		for (int l=0; l<num; l++){
			if (studentAns[l].equals(teacherAns[l])){
				count++;
			}
		}
		
		System.out.println(count);

	}

}
