
/*
 * 第4周 控制层Web开发——Servlet进阶
 * 
 * 4.2 会话跟踪技术（上）——Cookie
 * 
 * Cookie 第一例：获取客户端随着HTTP请求传递给服务器的Cookie信息.
 * 
 */


import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class BServlet
 */
@WebServlet("/BServlet_42")
public class BServlet_42 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public BServlet_42() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		response.setContentType("text/html;charset=utf-8");
		
		PrintWriter out = response.getWriter();
		Cookie[] cs = request.getCookies();
		if(cs!=null) {
			for(Cookie c:cs) {
				if(c.getName().equals("id")) {
					out.println("YOU ID IS: " + c.getValue());
				}
			}
		}
		
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
