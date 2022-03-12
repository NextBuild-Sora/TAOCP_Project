

/*
 * 第11讲 网络、多媒体和数据库编程
 * 11.1 网络编程
 * 
 * ---ch1111---
 * -- 更复杂的网络信息获取 --
 * 	示例	• 获取股票信息
 */


package ch11;

import org.apache.http.*;
import org.apache.http.client.*;
import org.apache.http.client.fluent.*;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.net.URL;

import java.imageio.ImageIO;

public class ch1111_HttpClienStock {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		String stockCode = "sz000837";
		String str = Request.Get("http://hq.sinajs.cn/list="+stockCode)
			.execute().returnContent().asString();
		System.out.println(str);
		
		String chartType = "min";
		String imageURL = "http://image.sinajs.cn/newchart/" + chartType + "/n/" + ".gif" ;
		
		//BufferedImage img = ImageIO.read(Request.Get(imageURL)
        //        .execute().returnContent().asStream());
		BufferedImage img = ImageIO.read(new URL(imageURL));
		ImageIO.write(img, "gif", new File("d:\\aaa.gif"));
		
	}

}



