
/*
 * 第8周 MVC分层Web开发
 * 8.2 MVC设计模式应用
 * --1.定义vo类，vo类定义了数据的属性，及相应的setter，getter方法。--
 * --定义User类 ：User.java --
 * 
 */


package MVC.mvcdemo.vo;

/**
 * 
 * 定义用户类
 */
public class User_82 {
	private String userid;	// 用户ID
	private String name;	// 用户名
	private String password;	 // 密码
	
	public String getUserid() {
		return userid;
	}
	public void setUserid(String userid) {
		this.userid = userid;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
}

