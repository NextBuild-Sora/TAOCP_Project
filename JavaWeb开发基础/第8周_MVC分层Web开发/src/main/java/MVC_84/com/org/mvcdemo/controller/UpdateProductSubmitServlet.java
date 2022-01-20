package MVC_84.com.org.mvcdemo.controller;

import java.io.IOException;
import java.util.UUID;

import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;

import MVC_84.com.org.mvcdemo.dao.IProductDAO;
import MVC_84.com.org.mvcdemo.factory.DAOFactory;
import MVC_84.com.org.mvcdemo.vo.Product;

/**
 * Servlet implementation class UpdateProductSubmitServlet
 */
@WebServlet("/UpdateProductSubmitServlet")
@MultipartConfig
public class UpdateProductSubmitServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public UpdateProductSubmitServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		request.setCharacterEncoding("UTF-8");
		String name = request.getParameter("name");
		String note = request.getParameter("note");
		String price = request.getParameter("price");
		String amount = request.getParameter("amount");
		String pid = request.getParameter("pid");
		String pic = request.getParameter("pic");
		
		//获取物理路径
		String path = getServletContext().getRealPath("/pic");		
        //获取上传的文件
        Part part = request.getPart("newpic");
       
        String newpic = null;
        if(part.getSize() != 0) {
        	String filename = part.getSubmittedFileName();
        	String str[] = filename.split("\\.");
        	String suffix = str[str.length-1];
        	UUID uuid = UUID.randomUUID();
        	newpic = uuid.toString()+"."+suffix;
        	String filePath = path + "\\" + newpic;
            //写入文件
            part.write(filePath);
        }
        
        Product p = new Product();
        p.setPid(Integer.parseInt(pid));
        p.setName(name);
        p.setNote(note);
        p.setPrice(Float.parseFloat(price));
        p.setAmount(Integer.parseInt(amount));
        
        //如果有新上传的图片，则使用新的，否则使用原来的
        if(newpic != null)
        	p.setPic(newpic);
        else
        	p.setPic(pic);
        
        try {
        	IProductDAO proxy = DAOFactory.getIProductDAOInstance();
        	proxy.updateProduct(p);
        	request.getRequestDispatcher("SearchProductServlet").forward(request,response) ;
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
