

/*
 * 11.3 数据库编程
 * 
 * ---ch1130---
 * --示例0--
 */



package ch11;

import java.sql.*;

public class ch1130_JDBC4JavaDB {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		Class.forName("org.apache.derby.jdbc.ClinetDriver");
		Connection conn = DriverManager.getConnection("jdbc:derby://localhost:1527/sample", "app", "app");
		
		Statement stat = conn.createStatement();
		
		ResultSet rs = stat.executeQuery("select * from CUSTOMER");
		while (rs.next()) {
			System.out.println("name = " + rs.getString("NAME"));
			System.out.println( "email = " + rs.getString("EMAIL") );
		}
		
		rs.close();
		conn.close();
	}

}




