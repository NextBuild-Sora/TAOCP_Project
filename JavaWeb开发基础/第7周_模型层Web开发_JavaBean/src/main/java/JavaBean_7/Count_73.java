
/*
 * 
 * 第7周 模型层Web开发——JavaBean
 * 
 * 7.3 JavaBean的保存范围
 * 
 * 
 */


package JavaBean_7;

public class Count_73 {
	private int count;
	public Count_73() {
		System.out.println("=== 一个新的Count对象产生 ===");
	}
	public int getCount() {
		return ++this.count;
	}
}


