
/*
 * 
 * 7.5 项目实战——JSP+DAO实现员工信息
 * --4. 定义DAO操作标准——IEmpDAO.java--
 */


package JavaBean_7.dao;

import java.util.List;
import JavaBean_7.vo.*;

public interface IEmpDAO_75 {
	public boolean doCreate(Emp_75 emp) throws Exception; 	//员工信息添加操作
	public List<Emp_75>findAll(String keyWord) throws Exception; 	//按条件查询所有员工信息
	public Emp_75 findById(int empno) throws Exception; 	//按员工编号查询员工信息

}
