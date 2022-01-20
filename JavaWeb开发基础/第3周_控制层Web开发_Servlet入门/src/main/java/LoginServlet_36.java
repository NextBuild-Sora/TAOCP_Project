
/*
 * 
 * 3.6 项目实战——信息管理系统登录功能实现
 * 
 * 
 * */


import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class LoginServlet_36
 */
public class LoginServlet_36 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public LoginServlet_36() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		response.setContentType("text/heml;charset=UTF-8");
		response.setCharacterEncoding("UTF-8");
		//接受提交过来的用户名和密码
		String username = request.getParameter("username");
		String password = request.getParameter("password");
		
		if(username.equals("javaweb") && password.equals("abc123") ) {
			response.getWriter().write("welcome, "+username);
		}else {
			response.getWriter().write("sorry,用户名或密码错误(wrong).");
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
