
/*
 * --4.4 Servlet跳转--
 * --客户端跳转：重定向--
 * --服务器端跳转：请求转发--
 * 
 * */


import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


/**
 * Servlet implementation class RequestServlet1_44
 */
@WebServlet("/RequestServlet1_44")
public class RequestServlet1_44 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public RequestServlet1_44() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		response.setContentType("text/html;charset=UTF-8");
		String type = request.getParameter("type");
		if(type.equals("request")) { 	//客户端跳转
			response.sendRedirect("RequestServlet2_44");
			request.setAttribute("type", type);
		}else {		//服务端跳转
			RequestDispatcher rd = request.getRequestDispatcher("RequestServlet2_44") ;
			request.setAttribute("type", type);
			rd.forward(request, response);
		}
		
		
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
