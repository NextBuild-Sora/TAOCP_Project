

/*
 * 第9章 流、文件及基于文本的应用
 * 9.1 输入输出流
 * 
 * ---ch911---
 *  --字符的读写--
		• 字符的读写
		常见的编码
		• UTF-8, ASCII, GB2312, 默认编码
		
*/


package ch09;

import java.io.*;

public class ch911_CopyFileAddLineNumber {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String infname = "CopyFileAddLineNumber.java";
		String outfname = "CopyFileAddLineNumber.txt";
		if( args.length >= 1 ) infname = args[0];
		if( args.length >= 2 ) outfname = args[1];
		
		try {
			File fin = new File(infname);
			File fout = new File(outfname);
			
			BufferedReader in = new BufferedReader(new FileReader(fin));
			PrintWriter out = new PrintWriter(new FileWriter(fout));
			
			int cnt = 0;	//	行号
			String s = in.readLine();
			while(s != null) {
				cnt++;
				s = deleteComments(s);
				out.println(cnt + ":\t" + s);	//写出
				s = in.readLine();
			}
			in.close();		// 关闭缓冲读入流及文件读入流的连接.
			out.close();
		}catch(FileNotFoundException e1) {
			System.err.println("Fiel not found!(文件未找到)");
		}catch(IOException e2) {
			e2.printStackTrace();
		}

	}
	
	static String deleteComments(String s)	//去掉以//开始的注释
	{
		if( s==null ) return s;
		int pos = s.indexOf("//");
		if( pos<0 ) return s;
		return s.substring(0, pos);
		
	}

}
