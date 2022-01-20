

/*
 * 第9章 流、文件及基于文本的应用
 * 9.1 输入输出流
 * 
 * ---ch913---
 *  --对象的读写--
		
*/


package ch09;

import java.io.*;

class Person implements Serializable	//对象实现 Serializable(序列化) 接口
{
	String name;
	int age;
	Person(String name, int age){
		this.name = name;
		this.age = age;
	}
	public String toString() {
		return name + "(" + age + ")";
	}

}

public class ch913_SerializeDemo {
	
	public static void main(String[] args) 
	throws IOException
	{
		// TODO Auto-generated method stub
		Person [] ps = {
				new Person("Li", 18),
				new Person("Wang", 19)
		};
		String fileName = "s.temp";

		//对象的读写
		ObjectOutputStream output = new ObjectOutputStream(new FileOutputStream(fileName));
		for(Person p:ps) output.writeObject(p);
		output.close();
		
		ObjectInputStream input = new ObjectInputStream(
				new FileInputStream(fileName));
		Person p = null;
		try {
			while((p=(Person)input.readObject()) != null) {
				System.out.println(p);
			}
		}catch(ClassNotFoundException ex) {}
		catch(EOFException eofex) {}
		input.close();

	}

}
