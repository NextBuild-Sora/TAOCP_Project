
/*
 * 
 * 第9周 EL和JSTL
 * --9.1 EL表达式语言--
 * --在MVC中应用表达式语言--
 * --2. ELServlet.java——定义Servlet保存单个部门信息，传递request属性给JSP--
 * 
 */


package com.org.servlet;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.org.vo.Dept_91;

/**
 * Servlet implementation class ELServlet_91
 */
@WebServlet("/ELServlet_91")
public class ELServlet_91 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public ELServlet_91() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		Dept_91 dept = new Dept_91();
		dept.setDeptno(10);
		dept.setDname("信息技术学院");
		dept.setLoc("广州市海珠区");
		request.setAttribute("deptinfo", dept);
		
		request.getRequestDispatcher("dept_info_91.jsp").forward(request, response);
		
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
//		doGet(request, response);
		this.doGet(request, response);
		
	}

}
