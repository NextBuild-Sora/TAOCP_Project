<%@ page language="java" contentType="text/html; charset=UTF-8"
	import="java.util.*" 
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>

<meta charset="UTF-8">
<title>8.2 MVC设计模式应用</title>
<script language="JavaScript">
	function validate(f){
		if(!(/^\w{1,15}$/.test(f.userid.value))){
			alert("用户ID必须是1~15位");
			f.userid.focus();
			return false;
		}
		if(!(/^\w{1,15}$/.test(f.userpass.value))){
			alert("密码必须是1~15位");
			f.userpass.focus();
			return false;
		}
		return true;
	}
	
</script>

</head>

<body>

<h2>用户登录</h2>
<% request.setCharacterEncoding("GBK"); %>
	<% 
	List<String> info=(List<String>)request.getAttribute("info");
	if(info != null){
		Iterator<String> iter = info.iterator();
		while(iter.hasNext()){
	%>
		<h4><%= iter.next() %></h4>
	<%
		}
	}
	%>
<form action="LoginServlet_82" method="post" onSubmit="validate(this)">
	用户ID:<input type="text" name="userid"><br>
	 密  码:<input type="password" name="userpass"><br>
	 <input type="submit value="登录">
	 <input type="reset" value="重置">
</form>
</body>
</html>







