<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="JavaBean_7.*" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>7.2 JavaBean与表单</title>
</head>
<% request.setCharacterEncoding("GBK"); %>
<body>

<% 
	SimpeBean_71 simple = new SimpeBean_71();
	simple.setName(request.getParameter("name"));
	simple.setAge(Integer.parseInt(request.getParameter("age")));
%>
<h3>姓名：<%=simple.getName() %></h3>
<h3>年龄：<%=simple.getAge() %></h3>
</body>
</html>
