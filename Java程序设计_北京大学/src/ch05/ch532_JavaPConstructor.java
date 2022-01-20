

// 第5章 深入理解JAVA语言
// 5.3 对象构造与初始化

// 532 
//构造方法的执行过程
//• 构造方法的执行过程遵照以下步骤：
//调用本类或父类的构造方法，直至最高一层（Object） 
//	按照声明顺序执行字段的初始化赋值
//执行构造函数中的各语句
//• 简单地说：
//先父类构造，再本类成员赋值，最后执行构造方法中的语句。

//• 演示：JavaPConstructor



package ch05;

public class ch532_JavaPConstructor {

//	public static void main(String[] args) {
		// TODO Auto-generated method stub

//	}
	
	int a = 2000;
	ch532_JavaPConstructor(){
		this.a = 3000;
	}
}


