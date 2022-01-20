<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.util.*" %>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>输出Map集合</title>
</head>
<body>

<%
	//实例化Map对象
	Map map = new HashMap();
	//向集合中增加内容
	map.put("id", "中国大学慕课");
	map.put("site", "www");
	map.put("email", "2021@zgdxmk.com.cn");
	request.setAttribute("info", map);
%>
<h3>KEY为*: ${info["id"] }</h3>
<h3>	${info.site }</h3>		 <!-- []和.两种写法都可以-->
<h3>	${info["email"]}</h3>
</body>
</html>

