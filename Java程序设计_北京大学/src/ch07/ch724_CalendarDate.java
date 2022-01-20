
/*
 * 第7章 工具类及常用算法
 • 7.2 字符串和日期
 	---ch724---
 	--日期类--
 	
 */

package ch07;

import java.util.Calendar;
import java.util.Date;
import java.text.SimpleDateFormat;
import java.util.Locale;
import static java.util.Calendar.*;

public class ch724_CalendarDate {

	public static void main(String[] args) throws java.text.ParseException
	{
		// TODO Auto-generated method stub
		Calendar calendar = Calendar.getInstance();
		calendar.roll(MONTH, 1);
		System.out.println( calendar.get(MONTH) + "月" + calendar.get(DAY_OF_MONTH)+"日" );
		
		Date date = new Date();
		SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss", Locale.CHINA);
		System.out.println( formatter.format(date) );
		
		date = new SimpleDateFormat("yyyy-MM-dd").parse("2021-05-13");
		calendar.setTime(date);
		System.out.println( calendar.getDisplayName(DAY_OF_WEEK, LONG, Locale.CHINA) );

	}

}


