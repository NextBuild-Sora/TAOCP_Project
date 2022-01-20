

/*

 * 
 * 4.1.1 获取Servlet上下文初始化参数
 *
 */


import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import javax.servlet.http.*;
import java.io.*;
import javax.servlet.*;



//@WebServlet("/GetInitParamServlet")
public class GetInitParamServlet_411 extends HttpServlet {

	String servletInitParam = null;
	String appName= null;
	public void init(ServletConfig config) throws ServletException{
		this.servletInitParam = config.getInitParameter("site");
		ServletContext context = config.getServletContext();
		context.getInitParameter("app");
	}
	
	public void doGet(HttpServletRequest req, HttpServletResponse resp) 
			throws ServletException, IOException{	
//	    resp.setCharacterEncoding("UTF-8"); //设置服务器给客户端响应的内容类型，指定编码方式解决返回给客户端中文乱码的问题.
//		req.setCharacterEncoding("UTF-8");	//解决Post请求的中文乱码问题
		
		PrintWriter out= resp.getWriter();
		out.println("<html>");
		out.println("<head><title> InitParam </title></head>");
		out.println("<body>");
		out.println("<h1>Servlet InitParam= "+this.servletInitParam+"</h1>");
		out.println("<h1>Servlet Context InitParam= "+this.appName+"</h1>");
		out.println("</body>");
		out.println("</html>");
		out.close();
	}

	public void doPost(HttpServletRequest req, HttpServletResponse resp) 
			throws ServletException, IOException {
		this.doGet(req, resp);
	}

}

