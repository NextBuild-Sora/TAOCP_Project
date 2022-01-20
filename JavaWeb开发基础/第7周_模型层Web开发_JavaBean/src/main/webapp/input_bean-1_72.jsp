<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>7.2 JavaBean与表单（2）</title>
</head>
<% request.setCharacterEncoding("UTF-8"); %>
<body>

<jsp:useBean id="simple" scope="page" class="JavaBean_7.SimpeBean_71"></jsp:useBean>
<jsp:setProperty property="*" name="simple"/>
<h3>姓名：<%=simple.getName() %></h3>
<h3>年龄：<%=simple.getAge() %></h3>
</body>
</html>
