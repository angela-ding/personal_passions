package project1;

import java.util.Scanner;
public class HuffmanEncoding {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int num;
		String[] character = new String[20];
		String[] sequence = new String[20];
		String binarySequence;

		num = scan.nextInt();
		for (int i=0; i<num; i++){
			character[i] = scan.next();
			sequence[i] = scan.next();
		}
		binarySequence = scan.next();
		String charAnswer = "";
		charAnswer = getAnswer(binarySequence, character, sequence);
		System.out.println(charAnswer);
	}
	
	public static String getAnswer (String binarySequence, String[] character, String[] sequence){
		int j=0;
		String charAnswer = "";
		while(binarySequence.length()!=0){
			if (binarySequence.startsWith(sequence[j])){
				charAnswer = charAnswer + character[j];
				binarySequence = binarySequence.substring(sequence[j].length());
				j=0;
			} else{
				j++;
			}
		}
		return charAnswer;
	}

}
