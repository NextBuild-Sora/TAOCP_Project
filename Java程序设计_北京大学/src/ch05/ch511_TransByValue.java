
// 第5章 深入理解JAVA语言
// 5.1 变量及其传递
// 511 字段变量与局部变量————示例
//  变量的传递




package ch05;

public class ch511_TransByValue {
		
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int a = 0;
		modify (a); System.out.println(a);	//result: 0
		
		int []b = new int [1];
		modify(b);
		System.out.println(b[0]);	//result: 1
	}
	
	public static void modify (int a) {
		a++;
	}
	
	public static void modify (int[] b) {
		b[0] ++;
		b = new int[5];
	}

}



