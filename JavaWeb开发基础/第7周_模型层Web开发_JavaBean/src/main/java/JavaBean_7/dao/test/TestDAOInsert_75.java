
/*
 * 
 * 7.5 
 * 
 */


package JavaBean_7.dao.test;

import JavaBean_7.factory.DAOFactory_75;
import JavaBean_7.vo.Emp_75;

public class TestDAOInsert_75 {
	public static void main(String ags[]) throws Exception{
		Emp_75 emp = null;
		for(int x=0; x<5; x++) {
			emp = new Emp_75();
			emp.setEmpon(1000 + x);
			emp.setEname("王小"+x);
//			emp.setJob("OS"+x);
//			emp.setSal(500 * x);
			DAOFactory_75.getIEmpDAOInstance();
		}
	}
}
