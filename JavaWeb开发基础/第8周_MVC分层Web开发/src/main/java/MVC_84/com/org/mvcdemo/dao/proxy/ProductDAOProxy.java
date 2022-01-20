package MVC_84.com.org.mvcdemo.dao.proxy ;
import java.util.ArrayList;

import MVC_84.com.org.mvcdemo.dao.IProductDAO;
import MVC_84.com.org.mvcdemo.dao.impl.ProductDAOImpl;
import MVC_84.com.org.mvcdemo.dbc.DatabaseConnection;
import MVC_84.com.org.mvcdemo.vo.Product;
public class ProductDAOProxy implements IProductDAO {
	private DatabaseConnection dbc = null ;
	private IProductDAO dao = null ;
	public ProductDAOProxy(){
		try{
			this.dbc = new DatabaseConnection() ;
		}catch(Exception e){
			e.printStackTrace() ;
		}
		this.dao = new ProductDAOImpl(dbc.getConnection()) ;
	}
	
	public ArrayList<Product> findProduct(int startindex,int recordnum) throws Exception{
		ArrayList<Product> productList;
		try{
			productList = this.dao.findProduct(startindex,recordnum) ;	
		}catch(Exception e){
			throw e ;
		}finally{
			this.dbc.close() ;
		}
		return productList ;
	}
	
	public ArrayList<Product> findProduct(String name,int startindex,int recordnum) throws Exception{
		ArrayList<Product> productList;
		try{
			productList = this.dao.findProduct(name,startindex,recordnum) ;	
		}catch(Exception e){
			throw e ;
		}finally{
			this.dbc.close() ;
		}
		return productList ;
	}

	@Override
	public Product findProductByID(int pid) throws Exception {
		// TODO Auto-generated method stub
		Product p;
		try{
			p = this.dao.findProductByID(pid) ;	
		}catch(Exception e){
			throw e ;
		}finally{
			this.dbc.close() ;
		}
		return p ;
	}

	@Override
	public int getCount() throws Exception {
		// TODO Auto-generated method stub
		int count;
		try{
			count = this.dao.getCount() ;	
		}catch(Exception e){
			throw e ;
		}finally{
			this.dbc.close() ;
		}
		return count ;
	}

	@Override
	public int getCount(String name) throws Exception {
		// TODO Auto-generated method stub
		int count;
		try{
			count = this.dao.getCount(name) ;	
		}catch(Exception e){
			throw e ;
		}finally{
			this.dbc.close() ;
		}
		return count ;
	}
	
	@Override
	public int addProduct(Product p) throws Exception {
		// TODO Auto-generated method stub
		int ret;
		try{
			ret = this.dao.addProduct(p) ;	
		}catch(Exception e){
			throw e ;
		}finally{
			this.dbc.close() ;
		}
		return ret ;
	}

	@Override
	public int updateProduct(Product p) throws Exception {
		// TODO Auto-generated method stub
		int ret;
		try{
			ret = this.dao.updateProduct(p) ;	
		}catch(Exception e){
			throw e ;
		}finally{
			this.dbc.close() ;
		}
		return ret ;
	}

	@Override
	public int deleteProduct(int pid) throws Exception {
		// TODO Auto-generated method stub
		int ret;
		try{
			ret = this.dao.deleteProduct(pid) ;	
		}catch(Exception e){
			throw e ;
		}finally{
			this.dbc.close() ;
		}
		return ret ;
	}
	
	
} 