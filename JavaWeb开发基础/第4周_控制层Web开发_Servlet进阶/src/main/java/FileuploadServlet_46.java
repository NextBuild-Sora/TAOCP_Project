
/*
 *
 * --4.6 Servlet 3.0文件上传下载--
 * 
 * --实现文件上传功能的Servlet类--
 * 
 */


import java.io.File;
import java.io.IOException;
import java.net.URLEncoder;

import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;



/**
 * Servlet implementation class FileuploadServlet_46
 */
@WebServlet("/FileuploadServlet_46")
@MultipartConfig
public class FileuploadServlet_46 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public FileuploadServlet_46() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) 
			throws ServletException, IOException {
		// TODO Auto-generated method stub
		request.setCharacterEncoding("UTF-8");
		response.setContentType("text/html;charset=UTF-8");
		//创建目录
		File path = new File("d:\\tmp");
		//getServletContext().getRealPath("")获取上下文真实路径
		//如果文件要保存在当前上下文的image目录下可以这样设置
		//	File path=new File(this.getServletContext().getRealPath("/image"));
		if(!path.exists()) {
			path.mkdir();
		}
		//获取文件
		Part part = request.getPart("uploadfile");
		//获取文件名称
		String header = part.getHeader("content-disposition");
		String filename = getFileName(header);
		// 获取文件名称
		// String filename = part.getSubmittedFileName();
		//低版本的服务器可能不支持此方法，就用上面的方法获取文件名
		
		String filePath = path.getPath() + "\\" + filename;
		// 写入文件
		part.write(filePath);
		// 对文件名称进行URL编码
		String urlname = URLEncoder.encode(filename,"UTF-8");
		
		response.getWriter().write("<h2>文件上传成功，请点击如下链接下载查看</h2>");
		
		response.getWriter().write("<a href='DownloadfileServlet?file=" + urlname + "'>" + filename + "</a>");
			
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
		
	}
	
	public String getFileName(String header) {
		/**
		 * String[] tempArr1 = header.split(";");代码执行完之后，在不同的浏览器下，tempArr1数组里面的内容稍有区别
		 * 火狐或者google浏览器下：tempArr1={form-data,name="file",filename="snmp4j--api.zip"}
		 * IE浏览器下：tempArr1={form-data,name="file",filename="E:\snmp4j--api.zip"}
		 */
		String[] tempArr1 = header.split(";");
		/**
		 * 火狐或者google浏览器下：tempArr2={filename,"snmp4j--api.zip"}
		 * IE浏览器下：tempArr2={filename,"E:\snmp4j--api.zip"}
		 */
		String[] tempArr2 = tempArr1[2].split("=");
		// 获取文件名，兼容各种浏览器的写法
		String fileName = tempArr2[1].substring(tempArr2[1].lastIndexOf("\\") + 1).replaceAll("\"", "");
		return fileName;
	}

}


