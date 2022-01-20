<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="JavaBean_7.*" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>JavaBean测试（7.1）</title>
</head>
<body>

<!-- 使用JSP的page指令导入JavaBean -->
<%
	SimpeBean_71 simple = new SimpeBean_71();	//声明并实例化SimpleBean对象
	simple.setName("Java");		//设置name属性
	simple.setAge(26); 		//设置age属性
%>
<h3>姓名：<%=simple.getName() %></h3> 	<!-- 输出name属性的内容 -->
<h3>年龄：<%=simple.getAge() %></h3>		<!-- 输出age属性的内容 -->

</body>
</html>
