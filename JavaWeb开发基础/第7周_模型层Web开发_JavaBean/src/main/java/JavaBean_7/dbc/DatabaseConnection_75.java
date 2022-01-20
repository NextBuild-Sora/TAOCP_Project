
/*
 * 
 * 7.5 项目实战——JSP+DAO实现员工信息
 * --3. 数据库链接类——DatabaseConnection.java--
 *  
 */


package JavaBean_7.dbc;

import java.sql.*;

public class DatabaseConnection_75 {
	private static final String DBDRIVER = "com.mysql.cj.jdbc.Driver";
	private static final String DBURL = "com.mysql.cj.jdbc.Driver";
	private static final String DBUSER = "root";
	private static final String DBPASSWORD = "123456";
	private Connection conn = null;
	public DatabaseConnection_75() throws Exception{
		try {
			Class.forName(DBDRIVER);
			this.conn = DriverManager.getConnection(DBURL, DBUSER, DBPASSWORD);
		}catch(Exception e ) {
			throw e;
		}
	}
	public Connection getConnection() {
		return this.conn;
	}
	public void close() throws Exception{
		if(this.conn!=null) {
			try {
				this.conn.close();
			}catch(Exception e) {
				throw e;
			}
		}
	}
}
