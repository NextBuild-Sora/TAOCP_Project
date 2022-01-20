

/*
 * 第9章 流、文件及基于文本的应用
 * 9.1 输入输出流
 * 
 * ---ch910---
 *  --常见内容的读写--
		• 常见的内容
		二进制
		文本
		对象
		• 二进制流的读写
		
*/

package ch09;

import java.io.*;

public class ch910_Dump {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			dump( new FileInputStream("aaa.bmp"), 
				new FileOutputStream("bbb.bmp")	);
		}
		catch(FileNotFoundException fex)
		{
			fex.printStackTrace();
		}
		catch(IOException ioe)
		{
			ioe.printStackTrace();
		}

	}

	public static void dump(InputStream src, OutputStream dest)
	throws IOException
	{
		InputStream input = new BufferedInputStream(src);
		OutputStream output = new BufferedOutputStream(dest);
		byte[] data = new byte[1024];
		int length = -1;
		while((length = input.read(data))!= -1) {
			output.write(data, 0, length);
		}
		input.close();
		output.close();
	}
	
}


