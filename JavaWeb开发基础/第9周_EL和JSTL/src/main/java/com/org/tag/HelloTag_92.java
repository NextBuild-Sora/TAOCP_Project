
/*
 * 9.2 JSP客户标签
 * --1.定义标签的操作类--
 * 
 */


package com.org.tag;

import javax.servlet.jsp.JspException;
import javax.servlet.jsp.tagext.*;

import java.io.IOException;

import javax.servlet.jsp.*;

public class HelloTag_92 extends TagSupport {
	
	public int doStartTag() throws JspException{
		JspWriter out = super.pageContext.getOut();
		try {
			out.println("<h1>Hello World</h1>");
		} catch (IOException e) {
			// TODO 自动生成的 catch 块
			e.printStackTrace();
		}
		
		return TagSupport.SKIP_BODY;
		
	}
	
}
