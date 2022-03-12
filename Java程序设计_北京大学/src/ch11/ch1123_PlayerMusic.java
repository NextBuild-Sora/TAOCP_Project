

/*
 * 11.2 多媒体编程
 *
 * ---ch1123---
 * 
 * --播放mp3示例--
 * 
 * 
 */


package ch11;


import javax.media. * ;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.io.File;


public class ch1123_PlayerMusic implements ControllerListener { // ControllerListener // 控制事件 

	private Player player;
	private boolean first, loop;
	private String path;
	private List<String> mp3List;
	private int idx = 0;
	ch1123_PlayerMusic(List<String> mp3List){
		this.mp3List = mp3List;
	}
	
	public void start() {
		try {
			File playFile = new File(mp3List.get(idx));
			player = Manager.createRealizedPlayer(playFile.toURI().toURL());
		} catch(javax.media.CannotRealizeException ex) {
			System.out.println("不能创建播放器");
		} catch(NoPlayerException ex) {
			System.out.println("不能播放文件");
		} catch(IOException ex) {
			
		}
		if(player = null) {
			return;
		}
		first = false;
		palyer.addControllerListener(this);
		palyer.prefetch();
	}
	
	public void controllerUpdate(ControllerEvent e) {
		if (e instanceof EndOfMediaEvent) {
			idx++;
			if (idx < this.mp3List.size()) {
				this.start();
			}
			return;
		}
		if(e instanceof PrefetchCompleteEvent) {
			player.start();
			return;
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<String> mp3List = new ArrayList<String>();
		mp3List.add("e:\\media\\wangfei.mp3");
		mp3List.add("e:\\media\\xxxx.mp3");
		mp3List.add("e:\\media\\yyyy.mp3");
		
		ch1123_PlayerMusic pm = new ch1123_PlayerMusic(mp3List);
		pm.start();
	}

}



