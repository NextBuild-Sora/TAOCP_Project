
// 第5章 深入理解JAVA语言
// 5.2 多态和虚方法调用
// 521 动态类型确定----示例 



package ch05;

public class ch521_InstanceOf {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Object[] things = new Object[3];
		things[0] = new Integer(4);
		things[1] = new Double(3.14);
		things[2] = new String("2.09");
		double s = 0;
		for( int i=0; i<things.length; i++) {
			if ( things[i] instanceof Integer )
				s += ( (Integer)things[i]).intValue();
			else if( things[i] instanceof Double )
				s += ((Double)things[i]).doubleValue();
		}
		System.out.println("sum= " + s);

	}

}



