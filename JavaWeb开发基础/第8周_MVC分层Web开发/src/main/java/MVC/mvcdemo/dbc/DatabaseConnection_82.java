
/*
 * 第8周 MVC分层Web开发
 * 
 * 8.2 MVC设计模式应用
 * 
 * --2. 定义数据库连接类，这个类只负责连接数据库：--
 * --定义DataBaseConnection类--
 * 
 */


package MVC.mvcdemo.dbc;

import java.sql.*;

/**
 * 
 * 连接数据库
 *
 */
public class DatabaseConnection_82 {
	private static final String DBDRIVER = "org.gjt.mm.mysql.Driver";	// 定义数据库驱动程序
	private static final String DBURL = "jdbc:mysql://localhost:3306/usr"; 	// 数据库连接地址
	private static final String DBUSER = "root";	// 数据库连接用户名
	private static final String DBPASSWORD = "mysqladmin";	 // 数据库连接密码
	
	private Connection conn = null;	 // 声明数据库连接对象
	
	public DatabaseConnection_82() throws Exception{	// 构造函数
		try {
			Class.forName(DBDRIVER);	// 加载驱动程序
			this.conn = DriverManager.getConnection(DBURL, DBUSER, DBPASSWORD);	// 取得数据库连接
		}catch(Exception e) {
			throw e;
		}
	}
	
	public Connection getConnerction() {	// 取得数据库连接
		return this.conn;
	}
	
	public void close() throws Exception{	 // 关闭数据库操作
		if (this.conn != null) {	// 避免NullPointerException
			try {
				this.conn.close();	// 关闭数据库
			}catch(Exception e) {
				throw e;	// 抛出异常
			}
		}
	}
}


