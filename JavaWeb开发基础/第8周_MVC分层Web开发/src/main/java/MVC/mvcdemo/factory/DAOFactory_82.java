
/*
 * 第8周 MVC分层Web开发
 * 
 * 8.2 MVC设计模式应用
 * 
 * -- 6. 工厂类的实现： 取得DAO实例 --
 * -- 定义DAOFactory类， DAOFactory.java --
 * 
 */


package MVC.mvcdemo.factory;

import MVC.mvcdemo.dao.IUserDAO_82;
import MVC.mvcdemo.dao.proxy.UserDAOProxy_82;

/**
 * 
 * 工厂类
 *
 */
public class DAOFactory_82 {
	public static IUserDAO_82 getIUserDAOInstance() {
		return new UserDAOProxy_82();
	}

}

