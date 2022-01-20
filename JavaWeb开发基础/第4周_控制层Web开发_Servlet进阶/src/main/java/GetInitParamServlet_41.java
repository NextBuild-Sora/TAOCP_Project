

/*

 * 
 * 4.1 获取Servlet初始化参数信息
 * */


import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import javax.servlet.http.*;
import java.io.*;
import javax.servlet.*;



@WebServlet("/GetInitParamServlet")
public class GetInitParamServlet_41 extends HttpServlet {
//	private static final long serialVersionUID = 1L;
//  
//    public GetInitParamServlet_41() {
//        super();
//        // TODO Auto-generated constructor stub
//    }

//	protected void doGet(HttpServletRequest request, HttpServletResponse response) 
//    	throws ServletException, IOException {
		// TODO Auto-generated method stub
//		response.getWriter().append("Served at: ").append(request.getContextPath());
    

	String servletInitParam = null;
	public void init(ServletConfig config) throws ServletException{
		this.servletInitParam = config.getInitParameter("site");
	}
	
	public void doGet(HttpServletRequest req, HttpServletResponse resp) 
			throws ServletException, IOException{	
	    resp.setCharacterEncoding("UTF-8"); //设置服务器给客户端响应的内容类型，指定编码方式解决返回给客户端中文乱码的问题.
		req.setCharacterEncoding("UTF-8");	//解决Post请求的中文乱码问题
		
		PrintWriter out= resp.getWriter();
		out.println("<html>");
		out.println("<head><title> InitParam </title></head>");
		out.println("<body>");
		out.println("<h1>Servlet InitParam="+this.servletInitParam+"</h1>");
		out.println("</body>");
		out.println("</html>");
		out.close();
	}

//	protected void doPost(HttpServletRequest request, HttpServletResponse response) 
//			throws ServletException, IOException {
		// TODO Auto-generated method stub
//		doGet(request, response);
	

	public void doPost(HttpServletRequest req, HttpServletResponse resp) 
			throws ServletException, IOException {
		this.doGet(req, resp);
	}

}

