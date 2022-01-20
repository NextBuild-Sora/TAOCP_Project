

/*
 * 第8讲
 * 8.5 流式操作及并行的流
 * 
 * ---ch850---
 * -- 流的并行计算 --
	• 只需将.stream().
	• 换成 . parallelStream().
	• 其他都不变，就可以实现并行计算.
	• stream就是为并行运算而生的.
	
 */


package ch08;

import java.util.*;

public class ch850_UseParallelStream {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<Integer> a = Arrays.asList(1,2,5,7,3);
		System.out.println(
				a.parallelStream() 	//并行的流式操作
				//中间的操作
					.mapToInt(i -> (int)i)
					.filter(i -> i>2)
					.map(i -> i*i)
					.sorted()
					.distinct()
					.limit(10)
				//末端的操作
					.max()
				);

	}

}


