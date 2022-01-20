/*
 * 
 * 6.4 项目实战——数据更新功能实现
 * --修改、删除数据(密码修改)--
 * 
 */

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class PasswordUpdateServlet_64
 */
@WebServlet("/PasswordUpdateServlet_64")
public class PasswordUpdateServlet_64 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public PasswordUpdateServlet_64() {
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
		String newPassword = request.getParameter("password");
	
		try {
			//第一步：装置驱动
		Class.forName("com.mysql.cj.jbdc.Driver");
		//2:建立连接
		Connection con =  DriverManager.getConnection("jdbc:mysql://localhost:3306/demo?serverTimezone=UTC","root","123456");
		
		//3 构建查询对象
		String sql = "update member set password = ? where username = ? ";
		PreparedStatement pst = con.prepareStatement(sql);
		pst.setString(1, newPassword);
		pst.setString(2, username);
		
		int i= pst.executeUpdate();
		
		PrintWriter pw = response.getWriter();
		pw.write("密码修改成功");
			
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
