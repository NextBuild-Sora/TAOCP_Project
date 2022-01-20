
//第4讲 类、包和接口
//4.2 类的继承
//	Student


public class Ch04_420 {
	
	class Student extends Person	
	{
		String school;
		int score;
		
		void sayHello(Student another) {
			System.out.println("Hi! ");
			if(school == another.school)
				System.out.println("Shoolmates");
		}
		
		boolean isGoodStudent() {
			return score >= 90;
		}
		
		void sayHello() {
			super.sayHello();
			System.out.println("My school is" + school);
		}
		
		Student(String name, int age, String school){
			super(name, age);
			this.school = school;
		}
		
		Student(){}
		
		void testThisAndSuper(){
			int a;
			a = age;
			a = this.age;	//父类的字段
			a = super.age;	//父类的字段
		}
	
	}
	
		public static void main(String[] args) {
			// TODO Auto-generated method stub
			Person p = new Person( "Liming", 50 );
			Student s = new Student( "Wangqiang", 20, "PKU" );
			Person p2 = new Student( "Zhangyi", 18, "THU");
			
//			强制类型转换：
			Student s2 = (Student) p2;
//			Student s3 = (Student) p;	//runtime exception
			
			p.sayHello( s );
			
			Person [] manypeople = new Person[ 100 ];
			manypeople[0] = new Person("Li", 18);
			manypeople[1] = new Student("Wang", 18, "PKU");
			
	
		}

	}

