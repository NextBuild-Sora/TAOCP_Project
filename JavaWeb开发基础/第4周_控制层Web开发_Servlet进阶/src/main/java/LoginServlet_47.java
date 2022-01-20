
/*
 * 
 * --4.7 项目实战——信息管理系统登录注销功能实现--
 *
 */


//import java.io.IOException;
//import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
//import javax.servlet.http.HttpServlet;
//import javax.servlet.http.HttpServletRequest;
//import javax.servlet.http.HttpServletResponse;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;



/**
 * Servlet implementation class LoginServlet_47
 */
@WebServlet("/LoginServlet_47")
public class LoginServlet_47 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public LoginServlet_47() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		this.doPost(request, response);
		
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
//		doGet(request, response);
		
		response.setContentType("text/html;charset=UTF-8");
		request.setCharacterEncoding("UTF-8");
		PrintWriter out = response.getWriter();
		out.println("<HTML>");
		out.println(" <HTML><TITLE>A Servlet</TITLE></HEAD> ");
		out.println(" <BODY> ");
		String msg = "";
		String username = request.getParameter("username");
		String password = request.getParameter("password");
		HttpSession session = request.getSession();
		//如果参数任意一个为空则失败
		if(username == null || username.equals("") || password == null || password.equals("")) {
			msg = "用户名或密码为空，请<a href=login_47.html>重新登录</a>";
		}
		//如果用户名和密码不正确，也失败。这里规定用户名=admin，密码=123
		else if(!username.equals("admin") || !password.equals("123")) {
			msg = "用户名或密码错误，请<a href=login_47.html>重新登录</a>";
		}
		 //登录成功，则打印登录成功信息
		else {
			session.setAttribute("userid", username);
			response.setHeader("refresh", "2;URL=WelcomeServlet");	//定时跳转
			String s1 = "<h3>用户登录成功，两秒后跳转到欢迎页面!</h3><br>";
			String s2 = "<h3>如果没有跳转，请按<a href='WelcomeServlet_47'>这里</a></h3>";
			msg = s1+s2;
		}
		out.println(msg);
		out.println("</BODY>");
		out.println("</HTML>");
		out.flush();
		out.close();
		
	}

}




