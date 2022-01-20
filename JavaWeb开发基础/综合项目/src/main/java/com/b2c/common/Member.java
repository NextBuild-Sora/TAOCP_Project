package com.b2c.common;

public class Member {
	private Integer	id	;
	private String	email	;
	private String	nick	;
	private String	password	;
	private Integer	credit	;
	private Integer	layerid	;
	private MemberLayer	layer	;//关联到级别表
	public Integer getId() {
		return id;
	}
	public void setId(Integer id) {
		this.id = id;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public String getNick() {
		return nick;
	}
	public void setNick(String nick) {
		this.nick = nick;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	public Integer getCredit() {
		return credit;
	}
	public void setCredit(Integer credit) {
		this.credit = credit;
	}
	public Integer getLayerid() {
		return layerid;
	}
	public void setLayerid(Integer layerid) {
		this.layerid = layerid;
	}
	public MemberLayer getLayer() {
		return layer;
	}
	public void setLayer(MemberLayer layer) {
		this.layer = layer;
	}
	public Member(Integer id, String email, String nick, String password,
			Integer credit, Integer layerid, MemberLayer layer) {
		super();
		this.id = id;
		this.email = email;
		this.nick = nick;
		this.password = password;
		this.credit = credit;
		this.layerid = layerid;
		this.layer = layer;
	}
	
	

}
