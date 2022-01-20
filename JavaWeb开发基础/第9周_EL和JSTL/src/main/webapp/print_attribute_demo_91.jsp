<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>9.1 EL表达式语言</title>
</head>
<body>
<%
	// 假设以下的设置属性操作是在Servlet之中完成
	request.setAttribute("info", "www");	// 设置一个request属性范围
%>
<h3>${info}</h3>	
</body>
</html>

