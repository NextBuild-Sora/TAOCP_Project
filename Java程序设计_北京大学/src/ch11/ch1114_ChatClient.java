

/*
 * 第11讲 网络、多媒体和数据库编程
 * 11.1 网络编程
 * 
 * ---ch1114---
 * -- 实现多线程服务器程序 --
 * -客户端-
 * 
 */


package ch11;

import java.awt.*;
import java.awt.event.*;
import java.applet.*;
import javax.swing.*;
import java.net.*;
import java.io.*;

public class ch1114_ChatClient extends JFrame implements Runnable {

	public ch1114_ChatClient() {
		try {
			init();
		}
		catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SwingUtilities.invokeLater( ()->{
			new ch1114_ChatClient();
		} );

	}
	
	JTextField txtInput = new JTextField("please input here(请在此输入)", 20);
	JButton btnSend = new JButton("Send");
	JButton btnStart = new JButton("Start conect to server");
	JList<String> lstMsg = new JList<>();
	DefaultListModel<String> lstMsgModel = new DefaultListModel<>();
	
	Socket sock;
	Thread thread;
	BufferedReader in;
	PrintWriter out;
	public final static int DEFAULT_PORT = 6543;
	boolean bConnected;
	
	public void startConnect() {
		bConnected = false;
		try {
			sock = new Socket("127.0.0.1", DEFAULT_PORT);
			bConnected = true;
			processMsg("Connection ok（连接OK）");
			in = new BufferedReader(
					new InputStreamReader(sock.getInputStream())
					);
			out = new java.io.PrintWriter(sock.getOutputStream());
		} catch(IOException e) { 
			e.printStackTrace(); 
			processMsg("Connection failed（连接错误）");
		}
		if(thread == null) {
			thread = new Thread(this);
			thread.start();
		}
	}
	
	public void run() {
		while(true) {
			try {
				String msg = receiveMsg();
				Thread.sleep(100L);
				if( msg != null ) {
					processMsg(msg);
				}
			}catch( IOException e ) {
				e.printStackTrace();
			}catch( InterruptedException ei ) {}
		}
	}
	
	public void sendMsg(String msg) throws IOException {
		out.println(msg);
		out.flush();
	}
	
	public String receiveMsg() throws IOException {
		try {
			String msg = in.readLine();
			return msg;
		}catch(IOException e) {
			e.printStackTrace();
		}
		return "";
	}
	
	public void processMsg(String str) {
		SwingUtilities.invokeLater( ()->{
			lstMsgModel.addElement(str);
		} );
	}
	
	private void init() throws Exception {
		JPanel pnlHead = new JPanel();
		pnlHead.add( btnStart );
	getContentPane().add(pnlHead, BorderLayout.NORTH);
	
	getContentPane().add(
			new JScrollPane(lstMsg), BorderLayout.CENTER);
		JPanel pnlFoot = new JPanel();
		pnlFoot.add(txtInput);
		pnlFoot.add(btnSend);
	getContentPane().add(pnlFoot, BorderLayout.SOUTH);
	
	lstMsg.setModel(lstMsgModel);
	
	btnSend.addActionListener(e->{
		if(txtInput.getText().length() !=0 ) {
			try {
				sendMsg( txtInput.getText() );
			}catch(IOException e2) {
				processMsg(e2.toString());
			}
		}
		
	});
	
	btnStart.addActionListener(e->{
		this.startConnect();
	});
	
	this.setSize(400, 300);
	this.setTitle("Chat Client");
	this.setDefaultCloseOperation(EXIT_ON_CLOSE);
	this.setVisible(true);
	}

}


