
/*
 * 第7章 工具类及常用算法
 * 	7.4 排序与查找
   ---ch741---
   	--Collections类-- 
   		• 此类完全由在 collection 上进行操作静态方法组成. 
   		• 如sort, binarySearch, reverse等。
   
 * 
 */


package ch07;

import java.util.*;

public class ch741_TestCollectionsSort {
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<Person> school = new ArrayList<>();
		school.add( new Person("Li", 23) );
		school.add( new Person("Wang", 28) );
		school.add( new Person("Zhang", 21) );
		school.add( new Person("Tang", 19) );
		school.add( new Person("Chen", 22));
		school.add( new Person("Zhao", 22) );
		System.out.println( school );
		
		Collections.sort( school, new PersonComparator() );
		System.out.println( school );
		
		int index = Collections.binarySearch( school, new Person("Li", 23), new PersonComparator() );
		
		if( index >=0 )
			System.out.println("Found（找到）: " + school.get(index));
		else
			System.out.println("Not Found（未找到）!");

	}
}
	
class Person
{
	String name;
	int age;
	public Person( String name, int age ) {
		this.name = name;
		this.age = age;
	}
	@Override
	public String toString() {
		return name+": "+age;
	}
}
	
class PersonComparator implements Comparator
{
	public int compare( Object obj1, Object obj2 ) {
		Person p1 = (Person)obj1;
		Person p2 = (Person)obj2;
		if( p1.age > p2.age ) return 1;
		else if(p1.age<p2.age) return -1;
		return p1.name.compareTo(p2.name);
	}
}


