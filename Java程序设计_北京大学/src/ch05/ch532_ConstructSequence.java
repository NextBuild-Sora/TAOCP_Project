

// 第5章 深入理解JAVA语言
// 5.3 对象构造与初始化

// 532 构造方法的执行过程————示例
//• 简单地说：
//先父类构造，再本类成员赋值，最后执行构造方法中的语句。



package ch05;

public class ch532_ConstructSequence 
{

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Person p = new Student("李明", 18, "北大");
	}

}

class Person
{
	String name="未命名";	//step 2
	int age = -1;
	Person(String name, int age){
		super(); 	//step 1
		//step 3
		System.out.println("开始构造Person(),此时this.name= "+this.name + " ,this.age= "+this.age);
		this.name=name; this.age=age;
		System.out.println( "Person()构造完成，此时this.name= " + this.name + " , this.age= " + this.age );
	}
}

class Student extends Person
{
	String school="未定学校"; 	//step2
	Student( String name, int age, String school ){
		super( name, age ); 	//step 1
		//step 3
		System.out.println("开始构造Student(),此时this.name= " +this.name+ " ,this.age= " +this.age+ " ,this.school= " +this.school );
		this.school = school;
		System.out.println( "Student()构造完成,此时this.name= " +this.name+ " ,this.age= " +this.age+ " ,this.school= " +this.school );
	}
}





