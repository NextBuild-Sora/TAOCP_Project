
/*
 * 
 * 8.3 过滤器
 * --一个简单的过滤器--
 * 
 */


import java.io.IOException;
import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.annotation.WebFilter;
import javax.servlet.annotation.WebInitParam;


@WebFilter(urlPatterns= {"/*"}, initParams = {@WebInitParam(name="ref",value="Web")})
public class SimpleFiter_83 implements Filter{
	public SimpleFiter_83() {

	}
	
	public void init(FilterConfig filterConfig) throws ServletException{
//		System.out.println("过滤器初始化");
		
		// 接收初始化的参数
		String initParam = filterConfig.getInitParameter("ref");
		System.out.println("** 过滤器初始化，初始化参数=" + initParam);

	}
	
	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
		System.out.println("执行doFilter()方法之前");
		chain.doFilter(request, response);
		System.out.println("执行doFilte()方法之后");
	}
	
	public void destroy() {
		System.out.println("过滤器销毁");
	}

}


