

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

/**
 * Servlet implementation class Servlet3_45
 */
@WebServlet("/Servlet3_45")
public class Servlet3_45 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Servlet3_45() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		
		//同一用户不同页面的数据共享。
//		HttpSession session = request.getSession();
//		
//		if(session.getAttribute("account") != null ) {
//			response.getWriter().write("your account is "+session.getAttribute("account").toString());			
//		}else {
//			response.getWriter().write("your account is zero");
//		}
		
		
		//不同用户
		if(getServletContext().getAttribute("wash")!=null) {
			response.getWriter().write("servlet3:wash "+getServletContext().getAttribute("wash").toString());
		}else {
			response.getWriter().write("servlet3:");
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
