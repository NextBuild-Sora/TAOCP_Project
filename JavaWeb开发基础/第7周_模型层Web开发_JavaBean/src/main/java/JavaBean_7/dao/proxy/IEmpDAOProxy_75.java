
/*
 * 
 * 7.5 项目实战——JSP+DAO实现员工信息
 * -- 6. 代理主题实现类——IEmpDAOProxy.java --
 * 
 */


package JavaBean_7.dao.proxy;

import java.util.*;

import JavaBean_7.dao.IEmpDAO_75;
import JavaBean_7.dao.impl.EmpDAOImpl_75;
import JavaBean_7.dbc.DatabaseConnection_75;
import JavaBean_7.vo.Emp_75;

public class IEmpDAOProxy_75 implements IEmpDAO_75 {
	private DatabaseConnection_75 dbc = null;
	private IEmpDAO_75 dao = null;
	public IEmpDAOProxy_75() throws Exception{
		this.dbc = new DatabaseConnection_75();
		this.dao = new EmpDAOImpl_75(this.dbc.getConnection());
	}
	public boolean doCreate(Emp_75 emp) throws Exception{
		boolean flag = false;
		try {
			if(this.dao.findById(emp.getEmpno())==null) {
				flag = this.dao.doCreate(emp);
			}
		}catch(Exception e) {
			throw e;
		}finally {
			this.dbc.close();
		}
		return flag;
	}
	public List<Emp_75> findAll(String keyWord) throws Exception{
		List<Emp_75> all = null;
		try {
			all = this.dao.findAll(keyWord);
		}catch (Exception e) {
			throw e;
		}finally {
			this.dbc.close();
		}
		return all;
	}
	public Emp_75 findById(int empno) throws Exception{
		Emp_75 emp = null;
		try {
			emp = this.dao.findById(empno);
		}catch(Exception e) {
			throw e;
		}finally {
			this.dbc.close();
		}
		return emp;
	}
	
//	@Override
//	public Emp_75 findById(int empno) throws Exception {
//		// TODO 自动生成的方法存根
//		return null;
//	}
}
