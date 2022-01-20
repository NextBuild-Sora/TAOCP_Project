

// 第5章 深入理解JAVA语言
// 5.2 多态和虚方法调用
// 520 虚方法调用示例 



package ch05;

public class TestVirtuallnvoke {
	
	static void doStuff( Shape s ) {
		s.draw();
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Circle c = new Circle();
		Triangle t = new Triangle();
		Line l = new Line();
		doStuff(c);
		doStuff(t);
		doStuff(l);

	}
	
	class Shape{
		void draw() { System.out.println("Shape Drawing");}
	}
	
	class Circle extends Shape{
		void draw() { System.out.println("Draw Circle"); }
	}

	class Triangle extends Shape{
		void draw() { System.out.println("Draw Three Lines"); }
	}
	
	class Line extends Shape{
		void draw() { System.out.println("Draw Line"); }
	}
	
}
