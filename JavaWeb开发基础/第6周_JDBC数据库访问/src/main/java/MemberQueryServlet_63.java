
/*
 * 第6周 JDBC数据库访问
 * 
 * --6.3 项目实战——数据查询功--
 * -- 3 带参数查询 --
 * 
 */



import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;


/**
 * Servlet implementation class MemberQueryServlet_63
 */
@WebServlet("/MemberQueryServlet_63")
public class MemberQueryServlet_63 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public MemberQueryServlet_63() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		response.setContentType("text/html; charset=utf-8");
		
		String username = request.getParameter("username");
		try {
			//第一步：装置驱动
		Class.forName("com.mysql.cj.jbdc.Driver");
		//2:建立连接
		Connection con =  DriverManager.getConnection("jdbc:mysql://localhost:3306/demo?serverTimezone=UTC","root","123456");
		
		//3 构建查询对象
		PreparedStatement pst = con.prepareStatement("select * from member where username=?");
		pst.setString(1, username);
		
		ResultSet rs = pst.executeQuery();
		
		//4 提取数据集
		PrintWriter pw = response.getWriter();
		pw.write("<table>");
		pw.write("<tr>");
		pw.write("<th>用户名</th>");
		pw.write("<th>姓名</th>");
		pw.write("</tr>");
		while(rs.next()) {
			pw.write("<tr>");
			pw.write("<td>"+rs.getString("username")+"</td>");
			pw.write("<td>"+rs.getString("truename")+"</td>");
			pw.write("</tr>");
		}
		pw.write("</table>");
				
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
