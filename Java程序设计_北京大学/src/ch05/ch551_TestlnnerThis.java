

// 第5章 深入理解JAVA语言
// 5.5 内部类与匿名类
/*	-551-
 
在内部类中使用外部类的成员:
• 内部类中可以直接访问外部类的字段及方法
即使private也可以
• 如果内部类中有与外部类同名的字段或方法，则可以用
外部类名.this.字段及方法

*/



package ch05;

public class ch551_TestlnnerThis {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		A a = new A();
		A.B b = a.new B();
			b.mb(333);
	}

}

class A
{
	private int s=111;
	
	public class B{
		private int s=222;
	public void mb(int s) {
		System.out.println(s);		// 局部变量s
		System.out.println(this.s); 	// 内部类对象的属性s
		System.out.println(A.this.s); 	// 外层类对象属性s
		
		}
	}

}





