

/* 第9讲 流、文件及基于文本的应用
 *  9.3 正则表达式
 *
 * ---ch933---
 * 
 * 	--应用举例--
 * 	 • 示例: 从网页内容中找到链接的网址.
 */


package ch09;

import java.util.regex.*;

public class ch933_RegexHref {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String patternString = 
				"\\s*(href|src)\\s*=\\s*(\"([^\"]*\")|(\'[^\']*\')|([^\'\">\\s]+))"; 
		
		String text = 
				"<a href=\"http://aaa.htm\">bbb</a> <img src=\"http://bb.com/pic.jpg\">";
		
		Pattern pattern = Pattern.compile(patternString, 
				Pattern.CASE_INSENSITIVE);
		Matcher matcher = pattern.matcher(text);
		StringBuffer buffer = new StringBuffer();
		
		while(matcher.find()) {
			//整个捕获，相当于goup(0)
			buffer.append(" 获捕到" + matcher.group());
			//捕获中的一部分(第2对圆括号对应的，即是网址)
			buffer.append(" 其中网址为" + matcher.group(2));
			buffer.append("\r\n");
		}
		
		System.out.println(buffer.toString());

	}

}


