

/*
 * 第11讲 网络、多媒体和数据库编程
 * 11.1 网络编程
 * 
 * ---ch1114---
 * -- 实现多线程服务器程序 --
 * -服务端-
 * 
 */



package ch11;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.io.*;
import java.net.*;

public class ch1114_ChatServer extends JFrame implements Runnable {

	JTextField txtInput = new JTextField("please input here(  ) ", 20);
	JButton btnSend = new JButton("Send(  )");
	JList<String> lstMsg = new JList<>();
	DefaultListModel<String> lstMsgModel = new DefaultListModel<>();
	
	public ch1114_ChatServer() {
		try {
			init();
				ServerListen();
		}
		catch(Exception e ) {
			e.printStackTrace();
		}
	}
	
	private void init() throws Exception {
		getContentPane().add(
				new JScrollPane(lstMsg), BorderLayout.CENTER);
			JPanel pnlFoot = new JPanel();
			pnlFoot.add(txtInput);
			pnlFoot.add(btnSend);
		getContentPane().add(pnlFoot, BorderLayout.SOUTH);
		
		lstMsg.setModel(lstMsgModel);
			btnSend.addActionListener((e)->{
				broadcastMsg( this.txtInput.getText() );
			});
			
			this.setSize(400, 300);
			this.setDefaultCloseOperation(EXIT_ON_CLOSE);
			this.setVisible(true);
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SwingUtilities.invokeLater(()->{
			new ch1114_ChatServer();
		});
	}
	
	public void processMsg( String str ) {
		SwingUtilities.invokeLater( ()->{
			lstMsgModel.addElement(str);
		} );
		
		broadcastMsg(str);
	}
	
	public void broadcastMsg( String str ) {
		try { 
			for(Connection client : clients) {
				client.sendMsg(str);
				} 
			} catch(Exception e) {
				e.printStackTrace();
			}	
	}
	
	void btnSend_actionPerformed(ActionEvent e) {
		broadcastMsg( this.txtInput.getText() );
	}
	
	public final static int DEFAULT_PORT = 6543;
	protected ServerSocket listen_socket;
	Thread thread;
	java.util.Vector<Connection> clients = new java.util.Vector<>();
	
	public void ServerListen() {
		try {
			listen_socket = new ServerSocket(DEFAULT_PORT);
			
		} catch (IOException e) {
			e.printStackTrace();
		}
		processMsg("Server: listening on port (  )" + DEFAULT_PORT);
		thread = new Thread(this);
		thread.start();
	}
	
	public void run() {
		try {
			while(true) {
				Socket client_socket = listen_socket.accept();
				Connection c = new Connection(client_socket, this);
				clients.add( c );
				processMsg( "One Client Comes in(  ) " );
			}
		} catch(IOException e) {
			e.printStackTrace();
		}
	}
}


class Connection extends Thread{
	protected Socket client;
	protected BufferedReader in;
	protected PrintWriter out;
	ch1114_ChatServer server;
	
	public Connection(Socket client_socket, CharServer server_frame) {
		client = client_socket;
		server = server_frame;
		try {
			in = new BufferedReader(new InputStreamReader(client.getInputStream()));
			out = new java.io.PrintWriter(client.getOutputStream());
			
		} catch(IOException e) {
			try {
				client.close();
			}
			catch(IOException e2) {
				;
			}
			e.printStackTrace();
			return;
		}
		this.start();
		
	}
	
	public void run() {
		try {
			for(;;) {
				String line = receiveMsg();
				server.processMsg(line);
				if (line == null) break;
			}
		}
		catch (IOException e) {
			e.printStackTrace();
		}
		finally {
			try {
				client.close();
			}
			catch (IOException e2) {
				;
			}
		}
		
	}
	
	public void sendMsg(String msg) throws IOException {
		out.println( msg );
		out.flush();
	}
	
	public String receiveMsg() throws IOException {
		try {
			String msg = in.readLine();
			return msg;
		} catch(IOException e) {
			e.printStackTrace();
		}
		return "";
	}
		
}




