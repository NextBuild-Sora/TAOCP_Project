

/*
 * 第7章 工具类及常用算法
 • 7.3 集合
 	---ch735---
 	--Map --
 	Map：
	• Map是键-值对的集合。
	*其中可以取到entrySet()、keySet()、values()、 
	  *Map.Entry是一个嵌套接口。
	• Map类的重要实现。
	*HashMap类. 
	  *TreeMap类：用红黑树的算法.

*/


package ch07;

import java.util.*;
public class ch735_TestMap {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//Map<String, String> map = new HashMap<String, String>();

		Map<String, String> map = new TreeMap<String, String>();
		
		map.put("b", "Brazil");
		map.put("r", "Russia");
		map.put("i", "India");
		map.put("c", "China");
		map.put("k", "South Africa");
		//map.put(new String("c"), "China2");
		//map.put(new String("b"), "Brazil3");
		
		System.out.println( map.get("c") );
		
		for( String key : map.keySet() )
			System.out.println( key + ": " + map.get(key) );
		
		System.out.println();
		
		for( String value : map.values())
			System.out.println(value);
		
		System.out.println();
		
		for( Map.Entry<String, String> entry:map.entrySet() )
			System.out.println( entry.getKey() + ": " + entry.getValue() );
		
		System.out.println();
		
		Iterator it = map.entrySet().iterator();
		while(it.hasNext()) {
			Map.Entry<String, String> entry = ( Map.Entry<String, String> )it.next();
			System.out.println( entry.getKey() + ": " + entry.getValue());
		}
	}

}

