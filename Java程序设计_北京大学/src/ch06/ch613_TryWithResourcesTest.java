

/*

第6章 异常处理
• 本章介绍Java语言中的异常处理。
• 6.1 异常处理
	--- ch613 ---
	--再谈try…with…resource--
	• try(类型 变量名 = new 类型（） ）{ 。。。 } 
	• 自动添加了finally{ 变量.close(); }
		*不论是否出现异常，都会执行.

*/


package ch06;

import java.io.*;

public class ch613_TryWithResourcesTest {

	public static void main(String[] args) 
		// TODO Auto-generated method stub
			throws IOException
		{
			String path = "d:\\ch613_aaa.txt";
			System.out.println( "读取1：" + ReadOneLine1(path));
			System.out.println( "读取2：" + ReadOneLine2(path));
			
		}
		static String ReadOneLine1(String path) {
			BufferedReader br=null;
			try {
				br = new BufferedReader(new FileReader(path));
				return br.readLine();
			}catch(IOException e) {
				e.printStackTrace();
			}finally {
				if(br != null) {
					try {
						br.close();
					}catch(IOException ex) {
						
					}
				}
			}
			return null;
		}
		static String ReadOneLine2(String path)
			throws IOException
		{
			try(BufferedReader br=new BufferedReader(new FileReader(path))){
				return br.readLine();
			}
		}

	}


	
	