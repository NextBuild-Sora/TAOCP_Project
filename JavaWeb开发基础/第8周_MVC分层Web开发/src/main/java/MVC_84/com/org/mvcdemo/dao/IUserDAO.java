package MVC_84.com.org.mvcdemo.dao;

import MVC_84.com.org.mvcdemo.vo.User;

public interface IUserDAO {
	//用户登录验证
	public boolean findLogin(User user) throws Exception;
}
