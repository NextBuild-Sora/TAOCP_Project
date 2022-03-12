

/* 12 怎么写好程序
 * 
 * 4.反射
 * 
 * ---ch1243---
 * 
 * --动态创建对象--
		• 由Class来创建相关的实例、调用相关的方法
		
	-示例3-
		• 应用示例:加了反射功能的
		
		
 */



package ch12;


import java.io.*;
import java.net.*;
import java.util.*;

interface Servlet{
	void init();
	void service( String params, byte [] requestBuffer, OutputStream output );	
}

public class ch1243_HTTPServer {

	private static Map<String, Servlet> servletCache=new HashMap<>();
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int port;
		ServerSocket serverSocket;
		
		try {
			port = Integer.parseInt(args[0]);
		} catch(Exception e) {
			port = 8080; 	//
		}
		
		try {
			serverSocket = new ServerSocket(port);
			System.out.println("http server is lsitenning : " + port);
			
			//
			while (true) {
				try {
					//
					final Socket socket = serverSocket.accept();
					System.out.println("client from: " + socket.getInetAddress() + ":" + socket.getPort());
					
					service(socket);
				} catch(Exception e) {
					e.printStackTrace();
				}
			}
		} catch(Exception e) {
			e.printStackTrace();
		}

	}
	
	public static void service(Socket socket) throws Exception {
	
		InputStream socketIn = socket.getInputStream();
		Thread.sleep(500);
		//
		int size = socketIn.available();
		byte[] requestBuffer = new byte[size];
		socketIn.read(requestBuffer);
		String request = new String(requestBuffer);
		System.out.println(request);
		
		//
		String firstLineOfRequest = request.substring(0, request.indexOf("\r\n"));
		String[] parts = firstLineOfRequest.split(" ");
		String uri = parts[1];	//
		if("/".equals(uri)) uri = "index.html"; 	//
		
		// 
		if(uri.indexOf("servlet") != -1) {
			doServletService(socket, uri, requestBuffer);
			
		}else{
			//
			doFileResponse(socket, uri);
		}
		
	}
	
	static void doServletService(Socket socket, String uri, byte [] requestBuffer)
		throws IOException, InterruptedException, IllegalAccessException,
		ClassNotFoundException, InstantiationException
	{
		//
		String servletName = null;
		String params = null;
		if(uri.indexOf("?") != -1) {
			servletName = uri.substring(
					uri.indexOf("servlet/") + 8, uri.indexOf("?"));
			params = uri.substring(uri.indexOf("?") + 1);
		}else {
			servletName = uri.substring(uri.indexOf("servlet/") + 8 );
		}
		
		//
		Servlet servlet = (Servlet)servletCache.get(servletName);
		
		//
		if(servlet == null) {
			servlet = (Servlet)Class.forName(servletName).newInstance();
			servlet.init(); 	//
			servletCache.put(servletName, servlet);
		}
		
		//
		servlet.service(params, requestBuffer, socket.getOutputStream());
		
		Thread.sleep(1000);
		socket.close();
		
	}
	
	static void doFileResponse(Socket socket, String uri) 
		throws IOException, InterruptedException{
		uri = "rooot/" + uri; 	//
		
		String contentType;
		if (uri.indexOf("html") != -1) contentType = "text/html";
		else if (uri.indexOf("jpg") != -1 || uri.indexOf("jpeg") != -1) contentType = "image/jpeg";
		else if (uri.indexOf("gif") != -1) contentType = "image/gif";
		else contentType = "application/octet-stream";
		
		//
		String responseFirstLine = "HTTP/1.1 200 OK\r\n";
		String responseHeader = "Content-Type:" + contentType + "\r\n\r\n";
		InputStream in = new FileInputStream(uri);
		
		OutputStream socketOut = socket.getOutputStream();
		socketOut.write(responseFirstLine.getBytes());
		socketOut.write(responseHeader.getBytes());
		
		//
		int len = 0;
		byte[] buffer = new byte[1024];
		while ((len = in.read(buffer)) != -1)
			socketOut.write(buffer, 0, len);
		
		Thread.sleep(1000);
		socket.close();
		
	}

}



