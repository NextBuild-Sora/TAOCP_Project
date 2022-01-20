
/*
 * 第8周 MVC分层Web开发
 * --8.4 项目实战——基于MVC的信息管理系统--
 * --过滤器——拦截非法用户--
 * 
 */



package MVC.mvcdemo.filter;

import java.io.IOException;
import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.annotation.WebFilter;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebFilter("/*")
public class LoginFilter_84 implements Filter {
	
	public LoginFilter_84() {
		//
	}
	
	@Override
	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
			throws IOException, ServletException {
		// TODO 自动生成的方法存根
		HttpServletRequest req = (HttpServletRequest) request;
		HttpServletRequest rep = (HttpServletRequest) response;
		
		//获取上下文路径,如“/InfoManagerDemo”
		String ctxPath = request.getServletContext().getContextPath();
		//获取上下文路径,如“/InfoManagerDemo”
		String url = req.getRequestURI();
		//获取请求的对象,如“LoginServlet”
		String subUrl = url.substring(ctxPath.length()+1);
		
		  //将请求LoginServlet和login.jsp不进行拦截过滤
		if(subUrl.indexOf("LoginServlet_84") > -1 || subUrl.indexOf("login_84.jsp") > -1) {
			chain.doFilter(request, response);
		}
		else {
			//如果有session，表示已经登录，则通过，否则跳转至登录页面
			if(req.getSession().getAttribute("info")!=null) {
				chain.doFilter(request, response);
			}else {
				((HttpServletResponse) rep).sendRedirect("login_84.jsp");
			}
		}
		
	}
	
	public void init(FilterConfig fConfig) throws ServletException{
		
	}
	
	public void destroy() {
		//
	}
	
}

