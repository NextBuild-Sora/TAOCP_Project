

/*
 * 第9章 流、文件及基于文本的应用
 * 9.2 文件及目录
 * 
 * ---ch920---
 *  --  --
 *  • 示例:列出所有文件 ListAllFiles.java 
		*String[] list() 是关键.
		*使用递归.
		
*/



package ch09;

import java.io.*;

public class ch920_ListAllFiles {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		ListFiles( new File("D:\\ProgramData\\Eclipse-Java-2021-03-R\\Java程序设计_北京大学\\src\\ch09") );
		ListFiles( new File("D:\\ProgramData\\Eclipse-Java-2021-03-R") );

	}
	
	public static void ListFiles( File dir ) {
		if( !dir.exists() || ! dir.isDirectory() ) return ;
		
		String [] files = dir.list();
		for( int i=0; i<files.length; i++) {
			File file = new File( dir, files[i] );
			if( file.isFile() ) {
				System.out.println(
						dir + "\\" + file.getName() + "\t" + file.length() );
			}else {
				System.out.println(
						dir + "\\" + file.getName() + "\t<dir>" );
				ListFiles( file ); 		//对于子目录,进行递归调用
			}
		}
	}

}

