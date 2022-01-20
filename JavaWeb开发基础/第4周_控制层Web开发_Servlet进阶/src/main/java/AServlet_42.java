
/*
 * 第4周 控制层Web开发——Servlet进阶
 * 
 * 4.2 会话跟踪技术（上）——Cookie
 * 
 * Cookie 第一例：创建一个随机数以Cookie的形式保存在客户端.
 * 
 */


import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.UUID;
import javax.servlet.http.Cookie;

/**
 * Servlet implementation class AServlet_42
 */
@WebServlet("/AServlet_42")
public class AServlet_42 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public AServlet_42() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
//		response.getWriter().append("Served at: ").append(request.getContextPath());
		
		response.setContentType("text/html;charset=utf-8");
		
		String id = UUID.randomUUID().toString();
		Cookie cookie = new Cookie("id", id);
		cookie.setMaxAge(60*60); 	//持久cookie（设定有效期）
		response.addCookie(cookie);
		PrintWriter out = response.getWriter();
		out.println("send id");
		out.println("<a href='BServlet'>show Cookie</a>");
		out.close();
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
