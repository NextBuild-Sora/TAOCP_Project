
/*
 * --第4周--
 * --4.5 Servlet之间实现数据共享--
 * 
 */


import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

/**
 * Servlet implementation class Servlet1_45
 */
@WebServlet("/Servlet1_45")
public class Servlet1_45 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Servlet1_45() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) 
			throws ServletException, IOException {
		// TODO Auto-generated method stub
		//同一用户不同页面的数据共享。
		//获取session
//		HttpSession session = request.getSession();
		//设置金额
//		session.setAttribute("account", 1000);
		
//		response.getWriter().write("you account is "+session.getAttribute("account").toString());
		
		
		//不同用户页面的数据共享。
//		getServletContext().setAttribute("wash", 1000);
//		response.getWriter().write("servlet1:wash "+getServletContext().getAttribute("wash").toString());
		
		
		//服务器转发
		request.setAttribute("info", "卷发");
		request.getRequestDispatcher("Servlet2_45").forward(request, response);
		
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) 
			throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
