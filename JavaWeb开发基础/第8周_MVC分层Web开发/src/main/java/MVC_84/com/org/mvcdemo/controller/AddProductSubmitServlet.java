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
 * Servlet implementation class AddProductSubmitServlet
 */
@WebServlet("/AddProductSubmitServlet")
@MultipartConfig
public class AddProductSubmitServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public AddProductSubmitServlet() {
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
		String pic = null;
		//获取/pic的物理路径
		String path = getServletContext().getRealPath("/pic");		
        //获取文件
        Part part = request.getPart("pic");
        //判断是否有上传文件
        if(part.getSize() != 0) {
        	String filename = part.getSubmittedFileName();
        	String str[] = filename.split("\\.");
        	//获取文件的扩展名,如png\jpg等
        	String suffix = str[str.length-1];
        	//生成唯一编码，使用唯一编码作为上传图片的名称，避免重复
        	UUID uuid = UUID.randomUUID();
        	pic = uuid.toString()+"."+suffix;
        	String filePath = path + "\\" + pic;
            //写入文件
            part.write(filePath);
        }
        
        Product p = new Product();
        p.setName(name);
        p.setNote(note);
        p.setPrice(Float.parseFloat(price));
        p.setAmount(Integer.parseInt(amount));
        p.setPic(pic);
        
        try {
        	IProductDAO proxy = DAOFactory.getIProductDAOInstance();
        	proxy.addProduct(p);
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
