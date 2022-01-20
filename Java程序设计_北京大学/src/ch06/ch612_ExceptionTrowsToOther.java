


/*

第6章 异常处理
• 本章介绍Java语言中的异常处理。
• 6.1 异常处理
	--- ch612 ---
	受检的异常：
		• Exception分两种
			* RuntimeException及其子类，可以不明确处理.
		  * 否则，称为受检的异常（checked Exception).
		• 受检的异常，要求明确进行语法处理。
			* 要么捕（catch）.
			  * 要么抛（throws）.
	
*/



package ch06;

import java.io.*;

public class ch612_ExceptionTrowsToOther {
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			System.out.println( "====Before====" );
			readFile();
			System.out.println("===After===");
		}catch( IOException e ) { System.out.println("异常：" + e); }
			
	}
	
	public static void readFile()throws IOException{
		FileInputStream in = new FileInputStream("ch612_myfile.txt");
		int b;
		b = in.read();
		while(b != -1 ) {
			System.out.print( (char)b );
			b = in.read();
		}
		in.close();
		
	}

}


