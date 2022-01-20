
/*
 * 
 * 7.5 项目实战——JSP+DAO实现员工信息
 * -- 7. DAO工厂类——DAOFactory --
 * 
 */

package JavaBean_7.factory;

import JavaBean_7.dao.IEmpDAO_75;
import  JavaBean_7.dao.proxy.IEmpDAOProxy_75;

public class DAOFactory_75 {
	public static IEmpDAO_75 getIEmpDAOInstance() throws Exception{
		return new IEmpDAOProxy_75();
	}
}


