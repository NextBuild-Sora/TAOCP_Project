package MVC_84.com.org.mvcdemo.dao;

import java.util.ArrayList;

import MVC_84.com.org.mvcdemo.vo.Product;

public interface IProductDAO {
	//获取某页所有产品信息
	public ArrayList<Product> findProduct(int startindex,int recordnum) throws Exception;
	//根据产品名称获取某页产品信息
	public ArrayList<Product> findProduct(String name,int startindex,int recordnum) throws Exception;
	//根据产品id获取产品信息
	public Product findProductByID(int pid) throws Exception;
	
	//获取所有产品信息的数目（分页用）
	public int getCount() throws Exception;
	//根据产品名称获取产品信息的数目（分页用）
	public int getCount(String name) throws Exception;
	//新增产品信息
	public int addProduct(Product p) throws Exception;
	//修改产品信息
	public int updateProduct(Product p) throws Exception;	
	//删除产品信息
	public int deleteProduct(int pid) throws Exception;
}
