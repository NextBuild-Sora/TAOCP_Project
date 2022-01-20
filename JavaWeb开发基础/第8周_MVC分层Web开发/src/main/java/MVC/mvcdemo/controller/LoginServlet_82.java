

/*
 * 第8周 MVC分层Web开发
 * 
 * 8.2 MVC设计模式应用
 * 
 * --  7 .定义Servlet： --
 * -- LoginServlet.java --
 * 
 */


package MVC.mvcdemo.controller;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import MVC.mvcdemo.factory.DAOFactory_82;
import MVC.mvcdemo.vo.User_82;


/**
 * Servlet implementation class LoginServlet_82
 */
@WebServlet("/LoginServlet_82")
public class LoginServlet_82 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public LoginServlet_82() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		
		String path = "login_82.jsp";
		String userid = request.getParameter("userid");		// 接收userid的内容
		String userpass = request.getParameter("userpass"); 	// 接收userpass的内容
		List<String>info = new ArrayList<String>(); 	 // 保存返回信息
		// 判断输入为空的情况
		if (userid == null || "".equals(userid)) {
			info.add("用户ID不能为空");
		}
		if (userpass == null || "".equals(userpass)) {
			info.add("密码不能为空");
		}
		// 用户名密码验证通过
		if (info.size() == 0) {
			User_82 user = new User_82();	// 实例化vo
			user.setUserid(userid);		// 设置userid
			user.setPassword(userpass);		// 设置userpass
			try {
				if(DAOFactory_82.getIUserDAOInstance().findLogin(user)) { 	 // 验证通过
					info.add("通过验证"+user.getName()+"已登录");
				}else {
					info.add("登陆失败");
				}
			}catch(Exception e) {
				e.printStackTrace();
			}
		}
		request.setAttribute("info", info);
		request.getRequestDispatcher(path).forward(request, response); 	// 跳转
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		this.doGet(request, response); 	// 调用doGet操作
	}

}
