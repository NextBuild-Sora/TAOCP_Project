package com.b2c.util;

import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.SQLException;
import javax.naming.Context;
import javax.naming.InitialContext;

public class ConnectionUtil
{
	private static DataSource ds=null;
	static{
		try{ 
			Context initCtx = new InitialContext();
			Context envCtx = (Context)initCtx.lookup("java:comp/env");
			ds = (DataSource)envCtx.lookup("jdbc/WroxTC6");
		}
		catch(Exception ex)
		{
			throw new RuntimeException(ex);  
		}
	}
	public static Connection getConnection() throws SQLException 
	{
		Connection conn = ds.getConnection();
		return conn;
	}
	
	public static void returnConnection(Connection conn)
	{
		try {
			conn.close();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
}