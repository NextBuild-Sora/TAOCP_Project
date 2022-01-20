

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class MemberDeleteServlet_64
 */
public class MemberDeleteServlet_64 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public MemberDeleteServlet_64() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html; charset=utf-8");
		
		String username = request.getParameter("usernaem");
	
		try {
			//第一步：装置驱动
		Class.forName("com.mysql.cj.jbdc.Driver");
		//2:建立连接
		Connection con =  DriverManager.getConnection("jdbc:mysql://localhost:3306/demo?serverTimezone=UTC","root","123456");
		
		//3 构建查询对象
		String sql = "delete  from member where username = ? ";
		PreparedStatement pst = con.prepareStatement(sql);
		pst.setString(1, username);
		
		int i= pst.executeUpdate();
		
		PrintWriter pw = response.getWriter();
		pw.write("信息删除成功，请点击查看：<a href='SimpleQueryServlet_63'>查看所有</a>");
		
		//5 关闭连接 
		con.close();
		
		}catch(Exception ex) {
			ex.printStackTrace();
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
