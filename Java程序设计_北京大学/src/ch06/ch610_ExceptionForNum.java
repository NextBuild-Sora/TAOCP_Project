
/*

第6章 异常处理
• 本章介绍Java语言中的异常处理。
• 6.1 异常处理
	--- ch610 ---
*/


package ch06;

import java.io.*;
//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;


public class ch610_ExceptionForNum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		try {
			//语句组
			BufferedReader in = new BufferedReader( 
					new InputStreamReader( System.in ));
			System.out.print("Please inuput a number: ");
			String s = in.readLine();
			int n = Integer.parseInt(s);
		}catch( IOException ex) {
			//异常处理语句组
			ex.printStackTrace();
		}

	}

}

