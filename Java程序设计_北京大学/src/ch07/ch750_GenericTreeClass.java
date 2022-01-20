

/*
 * 第7章 工具类及常用算法
 * 7.5 泛型
 * 	---ch750---
 * 	--自定义泛型类--
 * 	*针对不同的类有相同的处理办法，但这些类之间不一定有继承关系。
 * 
 * */


package ch07;

import java.util.*;

public class ch750_GenericTreeClass {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TNode<String> t = new TNode<>("Roo（陋）");
		t.add("左边"); t.add("中间"); t.add("Right（正好）");
		t.getChild(0).add("aaa");
		t.getChild(0).add("bbb");
		t.traverse();

	}

}

class TNode<T>
{
	private T value;
	private ArrayList<TNode<T>> children = new ArrayList<>();
	
	TNode(T v){ this.value = v;}
	public T getValue() { return this.value; }
	public void add(T v) {
		TNode<T> child = new TNode<>(v);
		this.children.add(child);
	}
	public TNode<T> getChild(int i){
		if ( (i<0) || (i>this.children.size()) ) return null;
		return (TNode<T>)this.children.get(i);
	}
	
	//移动
	public void traverse() {
		System.out.println(this.value);
		for (TNode child : this.children)
			child.traverse();
		
	}
}
