

// 第5章 深入理解JAVA语言
// 5.3 对象构造与初始化
// 530 调用本类或父类的构造方法————示例 
	//this调用本类的其他构造方法。
	//super调用直接父类的构造方法.
	//this或super要放在第一条语句,且只能够有一条.
	//	在构造函数中使用this和super.


package ch05;

public class ch530_ConstructCallThisAndSuper {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Person p = new Graduate();

	}
}
	
	class Person
	{
		String name;
		int age;
		Person(){}
		Person( String name, int age ){
			this.name = name; this.age = age;
			System.out.println("In Person(String, int)");
		}
	}
	
	class Student extends Person
	{
		String school;
		Student(){
			this( null, 0, null );
			System.out.println("In Student");
		}
		Student( String name, int age, Student school ){
			super( name, age );
			this.school = school;
			System.out.println("In Student(String, int, String)");
		}
	}
	
	class Graduate extends Student
	{
		String teacher = "";
		Graduate(){
//			super();
			System.out.println("In Graduate");
		}
	}

//}



