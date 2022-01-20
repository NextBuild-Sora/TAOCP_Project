<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	isErrorPage="true"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>出错页面</title>
</head>
<body>
系统出现异常<br>
<%
//有时候可能出现无法跳转错误页，有可能是Tomcat将error.jsp也认为是出现了错误，从而无法显示，此时可加入以下语句，设置200的状态码，表示本页没有错误可以正确显示
//response.setStatus(200);
%>
<%=exception.getMessage() %>
</body>
</html>

