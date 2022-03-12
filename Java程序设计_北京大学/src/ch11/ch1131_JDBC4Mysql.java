

/*
 * 11.3 数据库编程
 * 
 * ---ch1131---
 * --示例1--
 * 
 */



package ch11;

import java.sql.*;

public class ch1131_JDBC4Mysql {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		// 驱动程序名
		String driver = "com.mysql.jdbc.Driver";
		
		// URL指向要访问的数据库名 
		String url = "jdbx:mysql://127.0.0.1:3306/mysql";
		
		// MySQL配置时的用户名
		String user = "root";
		
		// MySQL配置时的密码 
		String password = " ";
		try {
			// 加载驱动程序
			Class.forName(driver);
			
			// 连续数据库
			Connection conn = DriverManager.getConnection(url, user, password);
			if (!conn.isClosed()) System.out.println("Succeeded connection to the Database!（成功连接到数据库）");
			
			// statement用来执行SQL语句 
			Statement statement = conn.createStatement();
			
			// 要执行的SQL语句
			String sql = "select * from db limit 10 ";
			
			// 结果集
			ResultSet rs = statement.executeQuery(sql);
			
			while (rs.next()) {
				String name = rs.getString("Host");
				System.out.println(rs.getString("DB") + "\t" + name);
			}
			rs.close();
			conn.close();
			
		} catch(ClassNotFoundException e) {
			System.out.println("Sorry,can`t find the Driver!（找不到驱动）");
			e.printStackTrace();
		} catch(SQLException e) {
			e.printStackTrace();
		} catch(Exception e) {
			e.printStackTrace();
		}

	}

}



