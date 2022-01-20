

// 第5章 深入理解JAVA语言
// 5.5 内部类与匿名类
/*	-ch554-
 
匿名类:
	• 匿名类( anonymous class)是一种特殊的内部类.
	它没有类名，在定义类的同时就生成该对象的一个实例.
	“一次性使用”的类.
	
匿名类的使用:
	• 1、不取名字，直接用其父类或接口的名字.
	• 2、类的定义的同时就创建实例，即类的定义前面有一个new.
	• 3、在构造对象时使用父类构造方法.
	

*/



package ch05;

public class ch554_TestlnnerAnonymous 
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
		return new Object() {
			public String toString() {
				return (" lnnerSize: " + size + 						// " localVar: " + localVar +   // Error! 
						" finalLocalVar: " + finalLocalVar
						);
			}
		};
		
	}
}
	






