package MVC_84.com.org.mvcdemo.filter;

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

/**
 * Servlet Filter implementation class LoginFilter
 */
@WebFilter("/*")
public class LoginFilter implements Filter {

    /**
     * Default constructor. 
     */
    public LoginFilter() {
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see Filter#destroy()
	 */
	public void destroy() {
		// TODO Auto-generated method stub
	}

	/**
	 * @see Filter#doFilter(ServletRequest, ServletResponse, FilterChain)
	 */
	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
		// TODO Auto-generated method stub
		// place your code here
		HttpServletRequest req = (HttpServletRequest)request;
		HttpServletResponse rep = (HttpServletResponse)response;
		
		//获取上下文路径,如“/InfoManagerDemo”
		String ctxPath = request.getServletContext().getContextPath();
		//获取请求的地址路径,如“/InfoManagerDemo/LoginServlet”
		String url = req.getRequestURI();
		//获取请求的对象,如“LoginServlet”
        String subUrl = url.substring(ctxPath.length() + 1);
		
        //将请求LoginServlet和login.jsp不进行拦截过滤
		if(subUrl.indexOf("LoginServlet") > -1 || subUrl.indexOf("login.jsp") > -1) {
			chain.doFilter(request, response);
		}
		else {
			//如果有session，表示已经登录，则通过，否则跳转至登录页面
			if(req.getSession().getAttribute("info") != null) {
				chain.doFilter(request, response);
			}else {
				rep.sendRedirect("login.jsp");
			}
		}
	}

	/**
	 * @see Filter#init(FilterConfig)
	 */
	public void init(FilterConfig fConfig) throws ServletException {
		// TODO Auto-generated method stub
	}

}
