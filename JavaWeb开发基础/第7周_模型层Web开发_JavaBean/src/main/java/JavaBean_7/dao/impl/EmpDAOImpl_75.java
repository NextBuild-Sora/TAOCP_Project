

/*
 * 
 * 7.5 项目实战——JSP+DAO实现员工信息
 * --  5. 真是主题实现类——EmpDAOImpl_75.java --
 * 
 */



package JavaBean_7.dao.impl;

import java.sql.*;
import java.text.*;
import java.util.*;

import JavaBean_7.dao.IEmpDAO_75;
import JavaBean_7.vo.Emp_75;

public class EmpDAOImpl_75 implements IEmpDAO_75 {
	private Connection conn = null;
	private PreparedStatement pstmt = null;
	public EmpDAOImpl_75(Connection conn) {
		super();
		this.conn = conn;
	}
	
	public boolean doCreate(Emp_75 emp) throws Exception{	//员工信息添加操作
		boolean flag = false;
		String sql = "INSERT INTO emp(empno, ename) VALUES(?,?)";
		this.pstmt = this.conn.prepareStatement(sql);
		this.pstmt.setInt(1, emp.getEmpno());
		this.pstmt.setString(2, emp.getEname());
//		this.pstmt.setString(3, emp_75.getJob());
//		System.out.println(emp_75.getHiredate());
		DateFormat df = new SimpleDateFormat("yyyy-MM-dd");
//		java.util.Date date = df.parse(emp_75.getHiredate());
//		this.pstmt.setDate(4, new java.sql.Date(date.getTime()));
//		this.pstmt.setFloat(5, emp_75.getSal());
		if(this.pstmt.executeUpdate()>0) {
			flag = true;
		}
		this.pstmt.close();
		return flag;
	}
	
	public List<Emp_75> findAll(String keyWord) throws Exception{	//按条件查询所有员工信息
		List<Emp_75> all = new ArrayList<Emp_75>();
		String sql = "SELECT * FROM emp_75 WHRER eanme like ? OR job like ?";
		this.pstmt = this.conn.prepareStatement(sql);
		this.pstmt.setString(1, "%"+keyWord+"%");
		this.pstmt.setString(2, "%"+keyWord+"%");
		ResultSet rs = this.pstmt.executeQuery();
		Emp_75 emp = null;
		
		while(rs.next()) {
			emp = new Emp_75();
			emp.setEmpon(rs.getInt(1));
			emp.setEname(rs.getString(2));
//			emp.setJob(rs.getString(3));
//			emp.setHiredate(rs.getDate(4).toString());
//			emp.setSal(rs.getFloat(5));
			all.add(emp);
		}
		return all;
	}
	public Emp_75 findById(int empno) throws Exception{	//按员工编号查询员工信息
		Emp_75 emp = null;
		String sql = "SELECT * FROM emp_75 WHERE emapno=?";
		this.pstmt = this.conn.prepareStatement(sql);
		this.pstmt.setInt(1, empno);
		ResultSet rs = this.pstmt.executeQuery();
		if(rs.next()) {
			emp = new Emp_75();
			emp.setEmpon(rs.getInt(1));
			emp.setEname(rs.getString(2));
//			emp.setJob(rs.getString(3));
//			emp.setHiredate(rs.getDate(4).toString());
//			emp.setSal(rs.getFloat(5))
		}
		
		return emp;
	}
	
	
//	@Override
//	public boolean doCreate(Emp_75 emp) throws Exception {
//		// TODO 自动生成的方法存根
//		return false;
//	}
//	@Override
//	public List<Emp_75> findAll(String keyWord) throws Exception {
//		// TODO 自动生成的方法存根
//		return null;
//	}
//	@Override
//	public Emp_75 findById(int empno) throws Exception {
//		// TODO 自动生成的方法存根
//		return null;
//	}
	

}
