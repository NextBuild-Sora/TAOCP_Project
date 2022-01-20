<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<jsp:useBean id="simple" scope="page" class="JavaBean_7.SimpeBean_71"></jsp:useBean>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>JavaBean测试2（7.1）</title>
</head>
<body>

<!-- 使用<jsp:useBean>指令导入JavaBean -->
<%
	simple.setName("Java(2)");
	simple.setAge(26);
%>
 
<!-- <h3>姓名：<%=simple.getName() %></h3> -->
<!-- <h2>年龄：<%=simple.getAge() %></h2> -->

</body>
</html>
