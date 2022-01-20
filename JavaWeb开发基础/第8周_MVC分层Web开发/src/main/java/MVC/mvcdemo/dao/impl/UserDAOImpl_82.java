

/*
 * 第8周 MVC分层Web开发
 * 
 * 8.2 MVC设计模式应用
 * 
 * -- 4. 定义DAO实现类，实现接口中定义的方法--
 * -- 定义UserDAOImpl类， UserDAOImpl.java --
 * 
 */

package MVC.mvcdemo.dao.impl;

import java.sql.*;
import MVC.mvcdemo.dao.IUserDAO_82;
import MVC.mvcdemo.vo.User_82;

/**
 * 
 * DAO实现类，实现方法，但不负责数据库的具体连接
 *
 */
public class UserDAOImpl_82 {
	private Connection conn = null; 	// 定义数据库的连接对象
	private PreparedStatement pstmt = null; 	//定义数据库操作对象
	
	public UserDAOImpl_82(Connection conn) { 	//构造方法，设置数据库连接
		this.conn = conn;
	}
	
	/**
	 * 具体操作方法：查询
	 */
	public boolean findLogin(User_82 user) throws Exception{
		boolean flag = false; 	//定义标志位
		try {
			String sql = "SELECT name_82 FROM users WHERE userid + ? AND password + ?";
			this.pstmt = this.conn.prepareStatement(sql);	// 实例化操作
			this.pstmt.setString(1, user.getUserid());	 // 设置用户id
			this.pstmt.setString(2, user.getPassword());	// 设置password
			ResultSet rs = this.pstmt.executeQuery(); 	// 取得查询结果
			if(rs.next()) {
				user.setName(rs.getString(1));	// 取得姓名 
				flag = true;
			}
		}catch (Exception e) {
			throw e;
		}
		return flag;
	}

}

