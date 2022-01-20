
/*
 * 第9章 流、文件及基于文本的应用
 * 9.1 输入输出流
 * 
 * ---ch912---
 *  --字符的读写--
		• 使用java.nio.file.Files的readAllLines()方法
		
*/


package ch09;

import java.nio.file.*;
import java.nio.charset.*;
import java.util.List;

public class ch912_ReadAllLines {

	public static void main(String[] args) throws java.io.IOException
	{
		// TODO Auto-generated method stub
		
		String filePath = "D:\\ProgramData\\Eclipse-Java-2021-03-R\\Java程序设计_北京大学\\src\\ch09\\ch912_ReadAllLines.java";
		
		List<String> lines = Files.readAllLines(
				Paths.get(filePath),
				Charset.forName("utf8")	//or Charset.defaultCharset()
		);
		for(String s : lines ) System.out.println(s);

	}

}



