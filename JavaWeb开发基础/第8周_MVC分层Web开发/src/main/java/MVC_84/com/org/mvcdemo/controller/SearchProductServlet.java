package MVC_84.com.org.mvcdemo.controller;

import java.io.IOException;
import java.util.ArrayList;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import MVC_84.com.org.mvcdemo.common.Pager;
import MVC_84.com.org.mvcdemo.dao.IProductDAO;
import MVC_84.com.org.mvcdemo.factory.DAOFactory;
import MVC_84.com.org.mvcdemo.vo.Product;

/**
 * Servlet implementation class SearchProductServlet
 */
@WebServlet("/SearchProductServlet")
public class SearchProductServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public SearchProductServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		request.setCharacterEncoding("utf-8");
		
		//获取可能传送过来的查询条件和页码，但不一定会传送过来。
		//比如在点击左边菜单的“查询产品"时，是没有传送查询条件和页码的，所以后面代码中要判断是否有这些数据
		String search_name = request.getParameter("search_name");
		String currentPage = request.getParameter("currentPage");
		//判断是否接收到页码，如果没有，则默认设置为第一页
		int iCurrentPage = currentPage==null?1:Integer.parseInt(currentPage);
		Pager pager = null;
		ArrayList<Product> productList = null;
		
		try {
			IProductDAO proxy = DAOFactory.getIProductDAOInstance();
			//如果没有查询条件提交上来，则查询全部，否则基于条件查询
			if(search_name == null) {
				int count = proxy.getCount();
				pager = new Pager(iCurrentPage,count,5);//构建pager对象，设置当前页、总记录数、每页显示条数
				productList = DAOFactory.getIProductDAOInstance().findProduct(pager.getStartResults(),pager.getPageSize());
			}else {
				int count = proxy.getCount(search_name);
				pager = new Pager(iCurrentPage,count,5);
				productList = DAOFactory.getIProductDAOInstance().findProduct(search_name,pager.getStartResults(),pager.getPageSize());
			}
			
			//如果有条件，则将条件设置到请求中，传送至jsp页面中，保证jsp的页面在刷新后，查询条件的值一直保留在文本框。
			if(search_name != null) {
				request.setAttribute("search_name", search_name);
			}
			//将Pager对象和查询出的结果设置到请求中，传送至jsp页面
			request.setAttribute("pager", pager);
			request.setAttribute("productList", productList);
			request.getRequestDispatcher("product.jsp").forward(request,response) ;
		}catch(Exception ex) {
			ex.printStackTrace();
		}		
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
