

/* 第9讲 流、文件及基于文本的应用
 *  9.3 正则表达式
 * ---ch931---
 * 匹配
	• 应用之二：匹配验证
	• 判断一个email地址是否合法
 */


package ch09;

import java.util.regex.Pattern;

public class ch931_RegexEmailValidate {

	public static void main(String[] args) 
	throws Exception {
		// TODO Auto-generated method stub
		String pattern = "^[^@]+@[\\w]+(\\.[\\w]+)*$";
		String email = "dstang2000@263.net";
		boolean ok = Pattern.matches(pattern, email);
		System.out.println( ok );

	}

}


