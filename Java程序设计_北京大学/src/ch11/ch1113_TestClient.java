

/*
 * 第11讲 网络、多媒体和数据库编程
 * 11.1 网络编程
 * 
 * ---ch1113---
 * -- 实现底层网络通信 --
 * -客户端-
 * 
 */


package ch11;

import java.net.*;
import java.io.*;

public class ch1113_TestClient {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			Socket s1 = new Socket("127.0.0.1", 8888);
			InputStream is = s1.getInputStream();
			DataInputStream dis = new DataInputStream(is);
			System.out.println(dis.readUTF());
			dis.close();
			s1.close();
		} catch(ConnectException connExc) {
			System.err.println("服务器连接失败！");
		} catch(IOException e) {
			
		}
	}

}

