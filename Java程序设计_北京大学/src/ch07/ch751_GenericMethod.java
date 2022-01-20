

/*
 * 第7章 工具类及常用算法
 * 7.5 泛型
 * 	---ch751---
 * 	--自定义泛型方法--
 * 	*针对不同的类有相同的处理办法，但这些类之间不一定有继承关系。
 *  *注意：<>要写到方法名字的前面.
*/


package ch07;

import java.util.*;

public class ch751_GenericMethod {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Date date = BeanUtil.<Date>getInstance("java.utli.Date");
		System.out.println(date);

	}

}

class BeanUtil{
	public static <T> T getInstance( String clzName ) {
		try
		{
			Class c = Class.forName(clzName);
			return (T) c.newInstance();
		}
		catch (ClassNotFoundException ex) {}
		catch ( InstantiationException ex ) {}
		catch ( IllegalAccessException ex ) {}
		return null;
	}
}
