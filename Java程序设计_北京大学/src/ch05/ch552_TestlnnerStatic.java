

// 第5章 深入理解JAVA语言
// 5.5 内部类与匿名类
/*	-552-
 
内部类的修饰符:

• static控制符
	• 用static修饰内部类 表明该内部类实际是一种外部类
		因为它与外部类的实例无关.
	有人认为static的类是嵌套类（nested class），不是内部类inner class.

• static类在使用时：
1、实例化static类时，在 new前面不需要用对象实例变量； 
  2、static类中不能访问其外部类的非static的字段及方法，既只能够访问static成员。
3、static方法中不能访问非static的域及方法，也不能够不带前缀地new 一个非
	static的内部类。

*/



package ch05;

public class ch552_TestlnnerStatic {

	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		A.B a_b = new A().new B();    //ok
		A a = new A();
		A.B ab = a.new B();
		
		Outer.Inner oi = new Outer.Inner();
		//Outer.Inner oi2 = Outer.new Inner();  //!!!error   
		//Outer.Inner oi3 = new Outer().new Inner(); //!!! error
	}

}

class A
{
	private int x;
	void m() {
		new B();
	}
	static void sm() {
		//new B(); 	//error!!!!
	}
	class B
	{
		B(){x=5;}
	}		
}

class Outer
{
	static class Inner
	{
		
	}
}





