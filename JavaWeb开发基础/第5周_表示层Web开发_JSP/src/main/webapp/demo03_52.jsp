<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>

<!--5.2 JSP注释及脚本 -->
<!-- 脚本 -->

<body>

<% String info="Hello world";
	int temp = 30;
	out.println(info);
%>
<%= temp %>


</body>
</html>