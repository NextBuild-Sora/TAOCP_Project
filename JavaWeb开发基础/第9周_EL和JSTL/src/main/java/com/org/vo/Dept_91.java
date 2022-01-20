
/*
 * 
 * 第9周 EL和JSTL
 * --9.1 EL表达式语言--
 * --在MVC中应用表达式语言--
 * --1. Dept.java——在MVC中定义表达式语言--
 * 
 */


package com.org.vo;

public class Dept_91 {
	private int deptno;
	private String dname;
	private String loc;
	
	public void setDeptno(int deptno) {
		this.deptno = deptno;
	}
	
	public void setDname(String dname) {
		this.dname = dname;
	}
	
	public void setLoc(String loc) {
		this.loc = loc;
	}
	
	public int getDeptno() {
		return this.deptno;
	}
	public String getDname() {
		return this.dname;
	}
	public String getLoc() {
		return this.loc;
	}
}
