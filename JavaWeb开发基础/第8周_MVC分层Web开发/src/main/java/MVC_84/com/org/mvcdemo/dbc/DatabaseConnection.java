package MVC_84.com.org.mvcdemo.dbc;
import java.sql.*;
import javax.naming.*;
import javax.sql.DataSource;
public class DatabaseConnection {

	private static final String DSNAME="java:comp/env/jdbc/TestDB";
	private Connection conn=null;
	public DatabaseConnection() throws Exception{
		try{
			Context ctx=new InitialContext();
			DataSource ds=(DataSource)ctx.lookup(DSNAME);
			this.conn=ds.getConnection();
		}catch(Exception e){
			throw e;
		}
	}
	public Connection getConnection(){
		return this.conn;
	}
	public void close() throws Exception{
		if(this.conn!=null){
			try{
				this.conn.close();
			}catch(Exception e){
				throw e;
			}
		}
	}
}
