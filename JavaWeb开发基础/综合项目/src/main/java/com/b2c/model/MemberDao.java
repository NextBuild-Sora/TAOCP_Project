package com.b2c.model;

import java.util.List;

import com.b2c.common.Member;

public class MemberDao {
	/**
	 * 注册，注意积分和级别的确定；密码需要通过加密算法处理后保存。
	 * @param member
	 * @return
	 */
	public int	add(Member member)	throws Exception{
		return 0;
	}
	
	/**
	 * 登录，验证用户的合法性。同时注意密码需要通过加密算法处理然后匹配。
	 * @param username
	 * @param password
	 * @return
	 */
	public boolean	validate(String username,String password){
		return false;
	}
	
	/**
	 * 信息修改。
	 * @param member
	 * @return
	 */
	public int	update(Member member)	{
		return 0;
	}
	
	/**
	 * 重置密码，将某个用户的密码重置为新密码。
	 * @param username
	 * @param password
	 * @return
	 */
	public int	resetPassword(String username,String password)	{
		return 0;
	}
	
	/**
	 * 根据ID查询会员
	 * @param id
	 * @return
	 */
	public Member	findById(Integer id)	{
		return null;
	}
	
	/**
	 * 根据查询条件分页查询会员
	 * @param sqlCause
	 * @param startindex
	 * @param size
	 * @return
	 */
	public List<Member>	findList(String sqlCause,int startindex,int size)	{
		return null;
	}
	
	/**
	 * 根据查询条件获取记录数
	 * @param sqlCause
	 * @return
	 */
	public int	findCount(String sqlCause){
		return 0;
	}
		
	/**
	 * 根据ID删除会员
	 * @param id
	 * @return
	 */
	public int	delete(Integer id)	{
		return 0;
	}

}
