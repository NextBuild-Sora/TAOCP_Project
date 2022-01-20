


/*
第6章 异常处理
• 本章介绍Java语言中的异常处理。
• 6.3 断言及程序的测试
	--- ch630 ---
	断言（assertion)
*/



package ch06;

public class Assertion {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		assert hypotenuse(3, 4) == 5 : "算法不正确";
	}
	static double hypotenuse( double x, double y ) {
		return Math.sqrt(x*x + y*y + 1);
	}

}

