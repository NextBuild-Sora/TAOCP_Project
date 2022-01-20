
/*
 * 
 * 7.5 项目实战——JSP+DAO实现员工信息
 * --7.5 使用连接池.
 * -3- 负责打开和关闭连接的类--
 *  
 */


package JavaBean_7.dbc;

import java.sql.*;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.sql.DataSource;

public class DatabaseConnection_3_75 {
	private static final String DSNAME = "java:comp/env/jdbc/TestDB";
	private Connection conn = null;
	public DatabaseConnection_3_75() throws Exception{
		try {		
			Context ctx = new InitialContext();
			DataSource ds = (DataSource)ctx.lookup(DSNAME);
			this.conn = ds.getConnection();
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
