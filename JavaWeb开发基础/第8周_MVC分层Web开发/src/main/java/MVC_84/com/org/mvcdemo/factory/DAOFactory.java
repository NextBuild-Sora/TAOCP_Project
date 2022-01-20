package MVC_84.com.org.mvcdemo.factory ;

import MVC_84.com.org.mvcdemo.dao.IProductDAO;
import MVC_84.com.org.mvcdemo.dao.IUserDAO;
import MVC_84.com.org.mvcdemo.dao.proxy.ProductDAOProxy;
import MVC_84.com.org.mvcdemo.dao.proxy.UserDAOProxy;
public class DAOFactory {
	public static IUserDAO getIUserDAOInstance(){
		return new UserDAOProxy() ;
	}
	
	public static IProductDAO getIProductDAOInstance(){
		return new ProductDAOProxy() ;
	}
}