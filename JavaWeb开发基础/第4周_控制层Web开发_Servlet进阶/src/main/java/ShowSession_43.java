

/* --JavaWeb开发基础_广东轻工职业技术学院--
* 
*  --第4周--
*  
*  --4.3 会话跟踪技术（下）——Session--
*  --Session第一例--
* 
*/



import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;
import java.util.*;
import javax.servlet.annotation.WebServlet;
//import javax.servlet.http.HttpServlet;
//import javax.servlet.http.HttpServletRequest;
//import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class SessionIdServlet_43
 */
@WebServlet("/ShowSession_43")
public class ShowSession_43 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public ShowSession_43() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
		// TODO Auto-generated method stub
		res.setContentType("text/html;charset=GBK");
		PrintWriter out = res.getWriter();
		out.println("<html>");
		out.println("<body>");
		HttpSession session = req.getSession(true);
		String name = (String)session.getAttribute("username");

//		out.println(session.getCreationTime()); 	//长整形格式
//		out.println(session.getLastAccessedTime()); //长整形格式
		out.println(new Date(session.getCreationTime())); 	//日期格式
		out.println(new Date(session.getLastAccessedTime())); 	//日期格式
		out.println("</html>");
		out.println("</body>");
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
