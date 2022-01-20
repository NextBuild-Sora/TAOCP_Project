
/*
 * 
第7章 工具类及常用算法
• 7.1 Java语言基础类
	---ch710---
	--System类--
	• 在Java中，系统属性可以通过环境变量来获得: 
		*System.getProperty(String name)方法获得特定的系统属性值.
		*System.getProperties()方法获得一个 Properties类的对象，其中包含了所有可用的系统属性信息.

*/


package ch07;

import java.util.*;

public class ch710_SystemProperties {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Properties props = System.getProperties();
		Enumeration keys = props.propertyNames();
		while(keys.hasMoreElements()) {
			String key = (String) keys.nextElement();
			System.out.println( key + "=" + props.getProperty(key));
		}

	}

}


