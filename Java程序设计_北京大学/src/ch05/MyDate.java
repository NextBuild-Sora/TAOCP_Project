
//第5章 深入理解JAVA语言
// 5.1 变量及其传递
// 510 基本类型变量与引用型变量————示例



package ch05;

public class MyDate {
	
	private int day;
	private int month;
	private int year;
	
	public MyDate(int y, int m, int d) {
		year = y;
		month = m;
		day = d;
	}
	
	void addYear() {
		year ++;
	}
	
	public void display() {
		System.out.println(year + "---" + month + "---" + day);
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		MyDate m = new MyDate(2003, 9, 22);
		MyDate n = m;
		n.addYear();
		m.display();
		n.display();

	}

}



