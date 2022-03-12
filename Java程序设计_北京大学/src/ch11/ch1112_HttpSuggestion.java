

/*
 * 第11讲 网络、多媒体和数据库编程
 * 11.1 网络编程
 * 
 * ---ch1112---
 * -- 应用示例• 获取建议词（suggestion) --
 * • 要点
	网络信息获取
	字符串处理及正则表达式
	界面、布局、事件
	线程
	• 小技巧： 在浏览器中按F12可以查看网络通信的过程
 
 */



package ch11;

//import javadoc.org.apache.hc.client5.http.*;
//import javadoc.org.apache.hc.client5.http.client.*;
//import javadoc.org.apache.hc.client5.http.client.fluent.*;

import org.apache.http.*;
import org.apache.http.client.*;
import org.apache.http.client.fluent.*;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;

import java.awt.*;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import javax.swing.JFrame;
import javax.swing.JList;
import javax.swing.JScrollPane;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;

public class ch1112_HttpSuggestion extends JFrame {

	JTextField txtInput = new JTextField();
	JList<String> lsitSuggestion = new JList<>();
	
	public ch1112_HttpSuggestion() {
		super("auto suggestion(  )");
		getContentPane().add(BorderLayout.NORTH, txtInput);
		getContentPane().add(BorderLayout.CENTER,
				new JScrollPane(lstSuggestion));
		setSize(400, 300);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setVisible(true);
		
		txtInput.addKeyListener(new KeyAdapter() {
			@Override
			public void keyPressed(KeyEvent arg0) {
				new Thread( ()->{
					try {
						String word = txtInput.getText();
						String[] suggestion = fetchSuggestion(word);
						SwingUtilities.invokeLater( ()->{
							lstSuggestion.removeAll();
							lstSuggestion.setListData(suggestion);
							lstSuggestion.updateUI();
						} );
					}catch(Exception ex) {
						ex.printStackTrace();
					}
				} ).start();
			}
		});
		
		lstSuggestion.addListSelectionListener( e->{
			txtInput.setText(lstSuggestion.getSelectedValue());
		} );
		
	}
	
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		SwingUtilities.invokeLater( ()->{
			new ch1112_HttpSuggestion();
		} );
		
	}

	public static String[] fetchSuggestion(String word)
		throws UnsupportedEncodingException, ClientProtocolException,
		IOException {
	if(word == null || word.length() == 0)
		return new String[0];
	
	String url = "http://suggestion.baidu.com/su?wd="
			+ URLEncoder.encode(word, "utf-8");
	url += "&rnd=" + Math.random();
	
	String content = Request.Get(url)
			.addHeader("cookie", "BDUSS=Aadasdfsfee").execute()
			.returnContent().asString();
		
	System.out.println(content);
	// window.baidu.sug({q:"人",p:false,s:["人体艺术","人体艺术图片","人人网","人体艺术摄影","人民币对美元汇率","人体","人人贷","人人影视"]});

	String[] sug = content.replaceAll(".*,s:\\[([^\\]]*)\\].*" , "$1")
			.replaceAll("\"", "").split(",");
	return sug;
	
	}
	
}


