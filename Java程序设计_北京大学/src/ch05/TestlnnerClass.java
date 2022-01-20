

// 第5章 深入理解JAVA语言
// 5.5 内部类与匿名类
/*	-550-
内部类（Inner class)
• 内部类的定义:
将类的定义class xxxx{…}置入一个类的内部即可 编译器生成xxxx$xxxx这样的class文件
内部类不能够与外部类同名
• 内部类的使用:
在封装它的类的内部使用内部类，与普通类的使用方式相同.
在其他地方使用.
	• 类名前要冠以外部类的名字。 
	• 在用new创建内部类实例时，也要在 new前面冠以对象变量。 
	• 外部对象名.new 内部类名(参数) .
• 示例 TestInnerClass.java
*/



package ch05;

public class TestlnnerClass {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Parcel p = new Parcel();
		p.testShip();
		
		Parcel.Contents c = p.new Contents(33);
		Parcel.Destination d = p.new Destination( "Haeii" );
		p.setProperty( c, d );
		p.ship();
	}

}

class Parcel{
	private Contents c;
	private Destination d;
	class Contents{
		private int i;
			Contents( int i ){ this.i = i; }
		int value() { return i; }
	}
	class Destination{
		private String label;
		Destination(String whereTo){label = whereTo;}
		String readLabel() { return label; }
	}
	void setProperty( Contents c, Destination d ) {
		this.c = c; this.d = d;
	}
	void ship() {
		System.out.println( "move " + c.value() + " to " + d.readLabel() );
	}
	public void testShip() {
		c = new Contents(22);
		d = new Destination("Beijing");
		ship();
	}
}




