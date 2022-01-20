
/*
 * 第8周 MVC分层Web开发
 * 
 * 8.2 MVC设计模式应用
 * 
 * -- 5.代理（proxy）类实现：负责数据库的打开和关闭及调用真实实现类对象操作：--
 * -- 定义UserDAOProxy implements IUserDAO，UserDAOProxy.java --
 * 
 */


package MVC.mvcdemo.dao.proxy;

/**
 * 代理类，要找到真实主题
 */
import MVC.mvcdemo.dao.IUserDAO_82;
import MVC.mvcdemo.dbc.DatabaseConnection_82;
import MVC.mvcdemo.dao.impl.UserDAOImpl_82;
import MVC.mvcdemo.vo.User_82;

public class UserDAOProxy_82  implements IUserDAO_82 {	// 构造方法，实例化连接，同时实例化dao对象
	private DatabaseConnection_82 dbc = null;
	private IUserDAO_82 dao = null;
	
	public UserDAOProxy_82() {
		try {
			this.dbc = new DatabaseConnection_82();	// 连接数据库
			
		}catch(Exception e) {
			e.printStackTrace();
		}
		this.dao = new UserDAOImpl_82(dbc.getConnerction());	 // 实例化真实主题类
	}
	
	public boolean findLogin(User_82 user) throws Exception{	// 实现接口中的方法.
		boolean flag = false;	// 定义标志位
		try {
			flag = this.dao.findLogin(user);	// 调用真实主题
		}catch(Exception e) {
			throw e;	 // 向上抛出异常
		}finally {
			this.dbc.close();
		}
		return flag;	// 返回标记
	}

}
