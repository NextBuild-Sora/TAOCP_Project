
/*
 *
 * --4.6 Servlet 3.0文件上传下载--
 * 
 * --实现文件下载功能的Servle类--
 * 
 */


import java.io.FileInputStream;
import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


/**
 * Servlet implementation class DownloadfileServlet_46
 */
@WebServlet("/DownloadfileServlet_46")
public class DownloadfileServlet_46 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public DownloadfileServlet_46() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		String file = request.getParameter("file");
		
		String filepath = "D:\\tmp\\" + file;
		
		//获取当前上下文中image目录下的文件
		//String filepath=getServletContext().getRealPath("/image/")+file;
				
		// 根据文件名称获取文件的MIME类型，用于指定ContentType
		String mimetype = getServletContext().getMimeType(file);
		response.setContentType(mimetype);
		// 设定Content-disposition属性值，可以上网了解，inline表示在浏览器内部直接打开文件
		response.setHeader("Content-disposition", "inline");
		
		FileInputStream fis = new FileInputStream(filepath);
		byte[] in = new byte[1024];
		
		while (fis.read(in, 0, in.length) != -1) {
			response.getOutputStream().write(in);
		}
		response.getOutputStream().flush();
		fis.close();
		
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
