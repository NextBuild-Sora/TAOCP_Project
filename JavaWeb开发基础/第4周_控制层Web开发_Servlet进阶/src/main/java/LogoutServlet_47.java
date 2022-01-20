
/*
 * 
 * --4.7 项目实战——信息管理系统登录注销功能实现--
 *
 */



//import java.io.IOException;
//import javax.servlet.ServletException;
//import javax.servlet.annotation.WebServlet;
//import javax.servlet.http.HttpServlet;
//import javax.servlet.http.HttpServletRequest;
//import javax.servlet.http.HttpServletResponse;

import java.io.*;
import javax.servlet.*;
import javax.servlet.annotation.*;
import javax.servlet.http.*;


/**
 * Servlet implementation class LogoutServlet_47
 */
@WebServlet("/LogoutServlet_47")
public class LogoutServlet_47 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public LogoutServlet_47() {
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
		// response.setContentType("text/html;charset=UTF-8");
	    // PrintWriter out = response.getWriter();//实现请求转发即服务器端跳转，跳转HTML页面如果中文乱码,尝试去掉此行代码
		HttpSession session = request.getSession();
		session.invalidate(); 	//session失效
		// response.setHeader("refresh","2;URL=login.html");//客户端跳转，定时刷新
	    // response.sendRedirect("login_47.html");//客户端跳转，即刻跳转
	    request.getRequestDispatcher("login_47.html").forward(request, response);
	    /*
	    out.println("<HTML>");
        out.println("  <HEAD><TITLE>注销！</TITLE></HEAD>");
        out.println("<h3>您已成功退出本系统，两秒后跳转到首页！</h3><br>");
        out.println("<h3>如果没有跳转，请按<a href='login_47.html'>这里</a></h3>");
        out.println("</BODY>");
        out.println("</HTML>");
        */
		
	      
	}

}
