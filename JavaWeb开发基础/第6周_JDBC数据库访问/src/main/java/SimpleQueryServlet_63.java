/*
 * 第6周 JDBC数据库访问
 * 
 * --6.3 项目实战——数据查询功--
 * 
 */



import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
//import com.mysql.cj.jdbc.Driver;

/**
 * Servlet implementation class SimpleQueryServlet_63
 */
@WebServlet("/SimpleQueryServlet_63")
public class SimpleQueryServlet_63 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public SimpleQueryServlet_63() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		
		try {
			//第一步：装置驱动
		Class.forName("com.mysql.cj.jbdc.Driver");
		//2:建立连接
		Connection con =  DriverManager.getConnection("jdbc:mysql://localhost:3306/demo","root","123456");
		
		//3:执行sql语句
		String sql = "select * from member";
		Statement st = con.createStatement();
		ResultSet rs =   st.executeQuery(sql);
		
		//4 提取数据集
		while(rs.next()) {
			System.out.println("username: "+rs.getString("username"));
			System.out.println("truename: "+rs.getString("truename"));
		}
		
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
