
/*
 * 第7章 工具类及常用算法
 * 	7.4 排序与查找
   ---ch742---
   	--Collections类-- 
   		• 更一般地，使用Lambda表达式（Java8以上）。
 * 
 */


package ch07;

import java.util.*;

public class ch742_TestCollectionsSortByLambda {
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<Person_1> school = new ArrayList<>();
		school.add( new Person_1("Li", 23) );
		school.add( new Person_1("Wang", 28) );
		school.add( new Person_1("Zhang", 21) );
		school.add( new Person_1("Tang", 19) );
		school.add( new Person_1("Chen", 22));
		school.add( new Person_1("Zhao", 22) );
		System.out.println( school );
		
		Collections.sort( school, (p1, p2)->p1.age-p2.age );
		System.out.println( school );
		
		int index = Collections.binarySearch( school, new Person_1("Li", 23), (p1,p2)->p1.age-p2.age );
		
		if( index >=0 )
			System.out.println("Found（找到）: " + school.get(index));
		else
			System.out.println("Not Found（未找到）!");

	}
}
	
class Person_1
{
	String name;
	int age;
	public Person_1( String name, int age ) {
		this.name = name;
		this.age = age;
	}
	
	public String toString() {
		return name+":"+age;
	}
}
	



