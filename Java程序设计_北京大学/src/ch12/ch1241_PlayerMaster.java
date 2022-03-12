

/* 12 怎么写好程序
 * 
 * 4.反射
 * 
 * ---ch1241---
 * 
 * --动态创建对象--
		• 由Class来创建相关的实例、调用相关的方法
		-示例1-
		
 */



package ch12;

interface Player{
	void play(String video);
}


public class ch1241_PlayerMaster {

	public static void main(String[] args) throws ClassNotFoundException, InstantiationException, IllegalAccessException {
		// TODO Auto-generated method stub
		
		//String playerImpl = System.getProperty("PlayerImpl");
				//类名可以从配置中来，甚至从一个目录下查找所有的文件。为了编译简单起见，这里写固定了。
		String playerImpl = "SimplePlayer";
		
		Player player = (Player) Class.forName(playerImpl).newInstance();
		
		String movie = "春秋";
		
		player.play(movie);

	}
	
	
}


class SimplePlayer implements Player{
	@Override
	public void play(String video) {
		System.out.println("正在播放" + video);
	}
}


