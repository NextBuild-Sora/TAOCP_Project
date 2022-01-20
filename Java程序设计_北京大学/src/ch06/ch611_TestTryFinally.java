

/*

第6章 异常处理
• 本章介绍Java语言中的异常处理。
• 6.1 异常处理
	--- ch611 ---
	多异常的处理.
		子类异常要排在父类异常的前面.
	
*/



package ch06;

public class ch611_TestTryFinally {
	
	public static String output = "";
	
	public static void foo(int i) {
		try {
			if (i == 1) {
				throw new Exception();
			}
			
			output += "1";
		}catch(Exception e) {
			output += "2";
			return;
		}finally{	//无论是否有异常都要执行.
			output += "3";
		}
		
		output += "4";
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//foo(0);
		//System.out.println(output);
		foo(1);
		System.out.println(output);
			
	}

}


