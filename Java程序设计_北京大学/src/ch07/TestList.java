

/*
 * 第7章 工具类及常用算法
 • 7.3 集合
 	---ch731---
 	--增强的for语句--
 	• 在JDK1.5以后，增强的for语句(enhanced for)或叫for-each.
for( Element e : list ) doSomething(e);
	 for (Photo photo : album){
	 System.out.println( photo.toString() );
 }

*/



package ch07;

import java.util.*;

public class TestList {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<Photo> album = new LinkedList<>();
		
		album.add(new Photo("one", new Date(), "classromm"));
		album.add(new Photo("two", new Date(),"library"));
		album.add(new Photo("three", new Date(), "gym"));
		album.add(new Photo("three", new Date(), "dorm"));
		
		Iterator<Photo> iterator = album.iterator();
		while(iterator.hasNext()) {
			Photo photo = iterator.next();
			System.out.println(photo.toString());
		}
		
		for(Photo photo : album) {
			System.out.println(photo);
		}
		

	}

}

class Photo{
	String title;
	Date date;
	String memo;
	Photo(String title, Date date, String memo){
		this.title = title;
		this.date = date;
		this.memo = memo;
	}
	@Override
	public String toString() {
		return title + "(" + date + ")" + memo;
	}
}
