

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
 * Servlet implementation class WelcomeServlet_47
 */
@WebServlet("/WelcomeServlet_47")
public class WelcomeServlet_47 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public WelcomeServlet_47() {
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
		response.setContentType("text/html;charset=UTF-8");
		PrintWriter out = response.getWriter();
		HttpSession session = request.getSession();
		out.println("<HTML>");
		out.println(" <HEAD><TITLE>欢迎！</TITLE></HEAD> ");
		out.println(" <BODY> ");
		if(session.getAttribute("userid")!=null)
			out.println("<h3>欢迎"+session.getAttribute("userid")+"光临本系统,<a href='LogoutServlet_47'>注销</a>!</h3>");
		else {
			//out.println("<h3>请先进行系统的<a href='login.html'>登录</a>!</h3>");
           //response.setHeader("refresh","1;URL=login.html");//客户端跳转，定时刷新
           //response.sendRedirect("login.html");//客户端跳转，即刻跳转
			request.getRequestDispatcher("Login_47.html").forward(request, response); 	//服务器端跳转
		}
		out.println("</BODY>");
		out.println("</HTML>");
	}

}


