
/* 第9讲 流、文件及基于文本的应用
 *  9.3 正则表达式
 *
 * ---ch932---
 * 
 * 	--Matcher类--
 * 	• 应用之三：查找替换
 */



package ch09;

import java.util.regex.*;

public class ch932_RegexReplacement {

	public static void main(String[] args)
	throws Exception {
		// TODO Auto-generated method stub
		Pattern pattern = Pattern.compile("cat");
		Matcher matcher = pattern.matcher("one cat, two cats in the yard");
		StringBuffer sb = new StringBuffer();
		while(matcher.find()) {
			matcher.appendReplacement(sb, "big $0");
		}
		matcher.appendTail(sb);
		System.out.println(sb.toString());

	}

}


