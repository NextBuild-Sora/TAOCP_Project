package MVC_84.com.org.mvcdemo.dao.impl ;

import java.sql.* ;
import java.util.ArrayList;

import MVC_84.com.org.mvcdemo.dao.IProductDAO;
import MVC_84.com.org.mvcdemo.vo.Product;
public class ProductDAOImpl implements IProductDAO {
	private Connection conn = null ;
	private PreparedStatement pstmt = null ;
	public ProductDAOImpl(Connection conn){
		this.conn = conn ;
	}
	public ArrayList<Product> findProduct(int startindex,int recordnum) throws Exception{
		ArrayList<Product> productList = new ArrayList<Product>();
		String sql = "SELECT * FROM product limit ?,?" ;
		this.pstmt = this.conn.prepareStatement(sql) ;
		pstmt.setInt(1, startindex);
		pstmt.setInt(2, recordnum);
		ResultSet rs = this.pstmt.executeQuery() ;
		while(rs.next()){
			Product p = new Product();
			p.setPid(rs.getInt("pid"));
			p.setName(rs.getString("name")) ;
			p.setNote(rs.getString("note"));
			p.setPrice(rs.getFloat("price"));
			p.setAmount(rs.getInt("amount"));
			p.setPic(rs.getString("pic"));
			
			productList.add(p);
		}
		this.pstmt.close() ;
		return productList ;
	}
	
	public ArrayList<Product> findProduct(String name,int startindex,int recordnum) throws Exception{
		ArrayList<Product> productList = new ArrayList<Product>();
		String sql = "SELECT * FROM product where name like \"%\"?\"%\" or note like \"%\"?\"%\" limit ?,?" ;
		this.pstmt = this.conn.prepareStatement(sql) ;
		pstmt.setString(1, name);
		pstmt.setString(2, name);
		pstmt.setInt(3, startindex);
		pstmt.setInt(4, recordnum);
		ResultSet rs = this.pstmt.executeQuery() ;
		while(rs.next()){
			Product p = new Product();
			p.setPid(rs.getInt("pid"));
			p.setName(rs.getString("name")) ;
			p.setNote(rs.getString("note"));
			p.setPrice(rs.getFloat("price"));
			p.setAmount(rs.getInt("amount"));
			p.setPic(rs.getString("pic"));
			
			productList.add(p);
		}
		this.pstmt.close() ;
		return productList ;
	}
	
	@Override
	public Product findProductByID(int pid) throws Exception {
		// TODO Auto-generated method stub
		Product p = null;
		String sql = "SELECT * FROM product where pid = ?" ;
		this.pstmt = this.conn.prepareStatement(sql) ;
		pstmt.setInt(1, pid);
		ResultSet rs = this.pstmt.executeQuery();
		if(rs.next()){
			p = new Product();
			p.setPid(rs.getInt("pid"));
			p.setName(rs.getString("name"));
			p.setNote(rs.getString("note"));
			p.setPrice(rs.getFloat("price"));
			p.setAmount(rs.getInt("amount"));
			p.setPic(rs.getString("pic"));
		}
		this.pstmt.close() ;
		return p ;
	}
	
	@Override
	public int getCount() throws Exception {
		// TODO Auto-generated method stub
		String sql = "SELECT count(*) FROM product" ;
		this.pstmt = this.conn.prepareStatement(sql) ;
		ResultSet rs = this.pstmt.executeQuery() ;
		rs.next();
		int count = rs.getInt(1);
		this.pstmt.close() ;
		return count ;
	}
	@Override
	public int getCount(String name) throws Exception {
		// TODO Auto-generated method stub
		String sql = "SELECT count(*) FROM product where name like \"%\"?\"%\" or note like \"%\"?\"%\"" ;
		this.pstmt = this.conn.prepareStatement(sql) ;
		pstmt.setString(1, name);
		pstmt.setString(2, name);
		ResultSet rs = this.pstmt.executeQuery() ;
		rs.next();
		int count = rs.getInt(1);
		this.pstmt.close() ;
		return count ;
	}
	@Override
	public int addProduct(Product p) throws Exception{
		// TODO Auto-generated method stub
		String sql = "insert into product(name,note,price,amount,pic) values(?,?,?,?,?)" ;
		this.pstmt = this.conn.prepareStatement(sql) ;
		pstmt.setString(1, p.getName());
		pstmt.setString(2, p.getNote());
		pstmt.setInt(4, p.getAmount());
		pstmt.setFloat(3, p.getPrice());
		pstmt.setString(5, p.getPic());
				
		int val = this.pstmt.executeUpdate();
		this.pstmt.close() ;
		return val ;		
	}
	@Override
	public int updateProduct(Product p) throws Exception {
		// TODO Auto-generated method stub
		String sql = "update product set name=?,note=?,amount=?,price=?,pic=? where pid=?" ;
		this.pstmt = this.conn.prepareStatement(sql) ;
		pstmt.setString(1, p.getName());
		pstmt.setString(2, p.getNote());
		pstmt.setInt(3, p.getAmount());
		pstmt.setFloat(4, p.getPrice());
		pstmt.setString(5, p.getPic());
		pstmt.setInt(6, p.getPid());
		
		int val = this.pstmt.executeUpdate();
		this.pstmt.close() ;
		return val ;
	}
	
	@Override
	public int deleteProduct(int pid) throws Exception {
		// TODO Auto-generated method stub
		String sql = "delete from product where pid=?" ;
		this.pstmt = this.conn.prepareStatement(sql);
		pstmt.setInt(1, pid);
		
		int val = this.pstmt.executeUpdate();
		this.pstmt.close() ;
		return val ;
	}
} 