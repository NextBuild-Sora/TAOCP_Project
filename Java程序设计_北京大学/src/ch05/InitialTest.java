
/*
// 第5章 深入理解JAVA语言
// 5.3 对象构造与初始化
// 531 创建对象时初始化
	//	实例初始化与静态初始化————示例 
	• 实例初始化（Instance Initializers） 
	• 在类中直接写
		{ 语句…. }
	实例初始化，先于构造方法{}中的语句执行
	• 静态初始化（Static Initializers） 
		static { 语句…. }
		静态初始化，在第一次使用这个类时要执行，
		但其执行的具体时机是不确定的
	• 但是可以肯定的是：总是先于实例的初始化
*/



package ch05;

public class InitialTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new InitialTest2(6);

	}
	
	int n=10; //step2
	{
		n++;
		System.out.println("InitialTest... "+n);
	}
	
	static int x;
	static
	{
		x++;
		System.out.println("static... "+x);
	}
	
}

class InitialTest2 extends InitialTest{
	InitialTest2(int a){
		this.a=a;
		System.out.println("this.a= " + a);
	}
	
	int a;
	{
		System.out.println("InitialTest2... "+this.a);
	}
	
	static
	{
		x++;
		System.out.println("static2... "+x);
	}
}



