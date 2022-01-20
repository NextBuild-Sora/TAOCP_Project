
/* 第9讲 流、文件及基于文本的应用
 *  9.3 正则表达式
 *  
 *  ---ch930---
 *  
 *  -- Pattern类 --
 *  • java.util.regex包
 *   *主要的类 Pattern类， Matcher类
 *  • 应用之一：分割
 *  	*如： 对以逗号和/或空格分隔的输入字符串进行切分.
 * 
 */


package ch09;


import java.util.regex.*;

public class ch930_RegexSplitter {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		Pattern p = Pattern.compile("[, \\s]+");
		String[] result = 
				p.split( "one,two, three   four ,  five ");
		for(int i=0; i<result.length; i++)
			System.out.println(result[i]);

	}

}



