
/*
 * 
 * 7.5 项目实战——JSP+DAO实现员工信息
 * -- 2. 定义VO类——Emp.java VO类的名称与表名一致--
 */



package JavaBean_7.vo;

import java.util.Date;;
public class Emp_75 {
	private int empno;
	private String ename;
//	private String job;
//	private Date hiredate;
//	private float sal;
	public int getEmpno() {
		return empno;
	}
	public void setEmpon(int empno) {
		this.empno = empno;
	}
	public String getEname() {
		return ename;
	}
	public void setEname(String ename) {
		this.ename = ename;
	}

}
