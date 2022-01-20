

// 第5章 深入理解JAVA语言
// 5.5 内部类与匿名类
/*	-ch553-
 
局部类：
	• 在一个方法中也可以定义类，这种类称为“方法中的内部类”。 
	• 或者叫局部类（local class）。
	
使用局部类：
	• 1、同局部变量一样，方法中的内部类。
	不能够用 public,private,protected,static修饰，
	但可以被final或者abstract修饰。
	• 2、可以访问其外部类的成员。
	• 3、不能够访问该方法的局部变量，除非是final局部变量。

*/



package ch05;

public class ch553_TestlnnerMethod 
{

	public static void main(String[] args) 
	{
		Object obj = new Outer().makeThelnner(47);
		System.out.println( "Hello World!" + obj.toString() );
	}

}

class Outer
{
	private int size = 5;
	public Object makeThelnner( int localVar )
	{
		final int finalLocalVar = 99;
		class lnner{
			public String toString() {
				return (" lnnerSize: " + size + 
						// " localVar: " + localVar +   // Error! 
						" finalLocalVar: " + finalLocalVar
						);
			}
		}
		return new lnner();
		
	}
}
	






