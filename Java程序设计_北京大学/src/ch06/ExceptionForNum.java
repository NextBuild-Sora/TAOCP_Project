
/*

第6章 异常处理
• 本章介绍Java语言中的异常处理。
• 6.1 异常处理
	--- ch610 ---
*/


package ch06;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class ExceptionForNum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			BufferedReader in = new BufferedReader( 
					new InputStreamReader( System.in ));
			System.out.print("Please inuput a number: ");
			String s = in.readLine();
			int n = Integer.parseInt(s);
		}catch( IOException ex) {
			ex.printStackTrace();
		}

	}

}

