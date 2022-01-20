

/*
 * 
第6章 异常处理
• 本章介绍Java语言中的异常处理。
• 6.2 自定义异常
	--- ch620 ---
	--重抛异常及异常链接--
	• 对于异常，不仅要进行捕获处理，有时候还需要将此异常进一步传递给调用者，以
便让调用者也能感受到这种异常。这时可以在catch语句块或finally语句块中采取
以下三种方式：
	• （1）将当前捕获的异常再次抛出：
	throw e;
	• （2）重新生成一个异常，并抛出，如：
	throw new Exception("some message");
	• （3）重新生成并抛出一个新异常，该异常中包含了当前异常的信息，如：
	throw new Exception("some message"，e);
	可用e.getCause() 来得到内部异常.
*/


package ch06;

public class ch620_ExceptionCause {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try
		{
			BankATM.GetBalancelnfo(12345L);
		}catch(Exception e) { 	
			System.out.println("something wrong（出问题了）: " + e);
			System.out.println("cause（原因）； " + e.getCause()); 	//用e.getCause() 来得到内部异常.
		}

	}

}

class DataHouse{
	public static void FindData( long ID )
		throws DataHouseException
	{
		if( ID>0 && ID<1000 )
			System.out.println("id: " + ID);
		else
			throw new DataHouseException("cannot find the id（找不到ID）"); 	//(2)重新生成一个异常，并抛出.
	}
}

class BankATM{
	public static void GetBalancelnfo( long ID )
		throws MyAppException
	{
		try
		{
			DataHouse.FindData(ID);
		}catch (DataHouseException e) {
			throw new MyAppException("invalid id（无效的ID）", e); 	//(3)重新生成并抛出一个新异常，该异常中包含了当前异常的信息.
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



