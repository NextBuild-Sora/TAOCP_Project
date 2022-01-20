
/*
 * 第7章 工具类及常用算法
 * 	7.4 排序与查找
   ---ch740---
   -- Arrays类 --
    • Arrays类是用于对数组进行排序和搜索的类。
    • Arrays类提供了sort()和binarySearch() 
    • 执行binarySearch()之前应调用sort()
 * 
 */


package ch07;

import java.util.*;

public class ch740_TestArraysSort {
	
	static Random r = new Random();
	static String
	ssource = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
	static char[] src = 
			ssource.toCharArray();
	
	static String randString(int length) {
		char[] buf = new char[length];
		for(int i=0; i<length; i++) {
			int rnd = Math.abs(r.nextInt()) % src.length;
			buf[i] = src[rnd];
		}
		return new String(buf);
	}
	
	static String[] randStrings(int length, int size) {
		String[] s = new String[size];
		for(int i=0; i<size; i++)
			s[i] = randString(length);
		return s;
	}
	
	public static void print(String[] s) {
		for(int i=0; i<s.length; i++)
			System.out.println(s[i] + "");
		System.out.println();
	} 

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[] s = randStrings(4, 10);
		print(s);
		Arrays.<String>sort(s); 	//数组排序
		int loc = Arrays.<String>binarySearch(s, s[2]); 	//二分查找
		System.out.println("Location of（位置）：" + s[2] + " is（是）：" + loc);

	}

}
