

/*
 * 12 怎么写好程序
 * 
 * 4.反射
 * 
 * ---ch1240---
 * 
 * -- 得到字段及方法 --
 * 	• 由Class获得该类的信息
		得到成员（字段、方法）
 * 
 */



package ch12;


import java.lang.reflect.*;

public class ch1240_ClassViewer {
	
	public static void view(Class clz) throws ClassNotFoundException{
	
		System.out.println("class name（类名字）: " + clz.getName());
		System.out.println("is interface（是否？？）: " + clz.isInterface());
		System.out.println("is primitive（是否？？）: " + clz.isPrimitive());
		System.out.println("is array（是否数组）: " + clz.isArray());
		System.out.println("super class（特级类）: " + clz.getSuperclass());
		
		Package p = clz.getPackage();
		System.out.printf("package（包） %s;%n", p.getName());
		
		int modifier = clz.getModifiers();
		System.out.printf("%s %s %s {%n", 
				Modifier.toString(modifier),
				Modifier.isInterface(modifier) ? "interface（接口）" : "class（类）",
				clz.getName()
		);
		
			//show all fields
		Field[] fields = clz.getDeclaredFields();
		for (Field field : fields) {
			System.out.printf("\t%s %s %s;%n", 
					Modifier.toString(field.getModifiers()), 
					field.getType().getName(),
					field.getName()
			);
		}
		
			//show all constructors
		Constructor[] constructors = clz.getDeclaredConstructors();
		for (Constructor constructor : constructors) {
			System.out.printf("\t%s %s( %s );%n", 
					Modifier.toString(constructor.getModifiers()),
					constructor.getName(),
						join(constructor.getParameterTypes())
			);
		}
		
			//show all methods
		Method[] methods = clz.getDeclaredMethods();
		for (Method method : methods) {
			System.out.printf("\t%s %s %s( %s ) throws（曲拐） %s;%n", 
					Modifier.toString(method.getModifiers()),
					method.getReturnType().getName(),
					method.getName(),
					join(method.getParameterTypes()),
						join(method.getExceptionTypes())
			);
		}
		System.out.println("}");
		
	}
	
	static String join( Class<?>[] ary) {
		if( ary==null) return null;
		StringBuilder sb = new StringBuilder();
		for( int i=0; i<ary.length; i++ ) {
			if( i!=0) sb.append(", " );
			sb.append( ary[i].getName() );
		}
		return sb.toString();
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			
			view( String.class );
			//view( "".getClass );

			//Class clz = Class.forName("java.lang.String");
         //view(clz);
			
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}

	}

}




