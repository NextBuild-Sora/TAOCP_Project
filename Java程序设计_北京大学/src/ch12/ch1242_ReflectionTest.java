

/* 12 怎么写好程序
 * 
 * 4.反射
 * 
 * ---ch1242---
 * 
 * --动态创建对象--
		• 由Class来创建相关的实例、调用相关的方法
		-示例2-
		
 */


package ch12;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;
import java.lang.reflect.Field;


public class ch1242_ReflectionTest {

	@SuppressWarnings("unchecked")
	public static void main(String[] args) throws Exception 
	{
		// TODO Auto-generated method stub
		
		// 1. 得到该对象所对应的Class对象
		Class<DemoTest2> clazz = DemoTest2.class;
		
		// 2. 通过该Class对象得到该类的构造方法所对应的Constructor对象
		Constructor cons = clazz.getConstructor(new Class[] {String.class, String.class}); 

		// 3. 通过该Constructor对象的newInstance方法得到该类的一个实例（对象）
		DemoTest2 obj = (DemoTest2)cons.newInstance(new Object[] {"abc（计算机是怎么跑起来的）", "xyz（TCP/IP详解）"});
		
		// 4. 通过该Class对象得到该方法所对应的Method对象
		Method method = clazz.getDeclaredMethod("output", new Class[] {String.class});
		
		// 5. 通过该Method对象的invoke方法进行调用
		method.invoke(obj, new Object[] {"Java设计模式"});
		
		// 属性也类似
		Field field = clazz.getDeclaredField("x");
		field.setAccessible(true);
		field.set(obj, 6);
		
	}

}


class DemoTest2
{
	private int x = 5;
	public DemoTest2(String s1, String s2)
	{
//		System.out.println(s1);
//		System.out.println(s2);
		System.out.println("s1: " + s1);
		System.out.println("s2: " + s2);
	}
	
	void output(String str)
	{
		System.out.println("Hello: " + str);
	}
	
}


