
/*
 * 
 * 8.3 过滤器
 * --字符编码过滤器--
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

@WebFilter(
		urlPatterns = { "/CharFilter" },
		initParams = { @WebInitParam(name="cahrset", value="UTF-8" )
		})

public class CharFilter_83 implements Filter {
	private String charSet;
	
	public void init(FilterChain fConfig) throws ServletException {
		System.out.println("***过滤器初始化***");
		this.charSet = ((FilterConfig) fConfig).getInitParameter("charset");
	}
	
	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) 
			throws IOException, ServletException {
		request.setCharacterEncoding(this.charSet);
		response.setContentType("text/heml; cahrset="+this.charSet);
		chain.doFilter(request, response);
	}
	
	public void destroy() {
		System.out.println("***过滤器销毁***");
	}
}


