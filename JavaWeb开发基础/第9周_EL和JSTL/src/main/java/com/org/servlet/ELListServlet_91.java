
/* 
 * 第9周 EL和JSTL
 * --9.1 EL表达式语言--
 * --在MVC中应用表达式语言--
 * --4. ELListServlet.java——定义Servlet保存多个部门信息到集合中，传递集合给JSP--
 * 
 */ 


package com.org.servlet;

import java.util.* ;
import com.org.vo.* ;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


/**
 * Servlet implementation class ELListServlet_91
 */
@WebServlet("/ELListServlet_91")
public class ELListServlet_91 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public ELListServlet_91() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		List<Dept_91> all = new ArrayList<Dept_91>();	// 实例化List接口
		
		Dept_91 dept = null;	// 定义Dept对象
		dept = new Dept_91();	// 实例化VO对象
		dept.setDeptno(10);		// 设置deptno属性
		dept.setDname("信息技术学院") ;		// 设置dname属性
		dept.setLoc("广州市海珠区") ;		// 设置loc属性
		all.add(dept) ;			// 向集合中增加dept属性
		
		dept = new Dept_91();	// 重新实例化VO对象
		dept.setDeptno(20) ;		// 设置deptno属性
		dept.setDname("艺术设计学院") ;		// 设置dname属性
		dept.setLoc("广州市海珠区") ;		// 设置loc属性
		all.add(dept) ;			// 向集合中增加dept属性
		request.setAttribute("alldept",all) ;	// 设置request属性
		
		// 通过服务器跳转传递request属性
		request.getRequestDispatcher("dept_list_91.jsp").forward(request, response);
		
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		this.doGet(request, response);
		
	}

}
