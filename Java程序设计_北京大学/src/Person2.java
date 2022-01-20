
//第4讲 类、包和接口
//4.2 类的继承


public class Person2 {
	
	private int age;
	public void setAge( int age ) throws Exception{
		if ( age >= 0 && age < 200 ) this.age = age;
		else throw new Exception( "invalid age" );
	}
	public int getAge(){
		return age;
	}
	
	
//	public static void main(String[] args) {
		// TODO Auto-generated method stub

//	}

}
