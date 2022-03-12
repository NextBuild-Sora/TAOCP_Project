

/*
 * 第11讲 网络、多媒体和数据库编程
 * 11.1 网络编程
 * 
 * ---ch1113---
 * -- 实现底层网络通信 --
 * -服务端-
 * 
 */


package ch11;

import java.net.*;
import java.io.*;

public class ch1113_TestServer {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		ServerSocket s = null;
		try {
			s = new ServerSocket(8888);
		} catch(IOException e) {}
		while (true) {
			try {
				Socket s1 = s.accept();
				OutputStream os = s1.getOutputStream();
				DataOutputStream dos = new DataOutputStream(os);
				dos.writeUTF("你好，( ^_^ )/~~ 拜拜！");
				dos.close();
				s1.close();
			} catch(IOException e) {}
		}
	}

}

