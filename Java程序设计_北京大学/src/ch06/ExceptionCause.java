
/*
 * 
第6章 异常处理
• 本章介绍Java语言中的异常处理。
• 6.2 自定义异常
	--- ch620 ---
	--重抛异常及异常链接--
	
*/

package ch06;

public class ExceptionCause {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}

class DataHouse{
	public static void FindData( long ID )
		throws DataHouseException
	{
		if( ID>0 && ID<1000 )
			System.out.println("id: " + ID);
		else
			throw new DataHouseExeption("cannot find the id");
	}
}

class BakATM{
	public static void GetBalancelnfo( long ID )
		throws MyAppException
	{
		try
		{
			DataHouse.FindData(ID);
		}catch (DataHouseException e) {
			tnrow new MyAppException("invalid id", e);
		}
	}
}

class DataHouseException extends Exception{
	public DataHouseException( String message ) {
		super(message);
	}
}

class MyAppException extends Exception{
	public MyAppException (String message) {
		super (message);
	}
	public MyAppException (String message, Exception cause) {
		super(message, cause);
	}
}



