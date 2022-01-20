<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="GBK">
<title>动态包含操作</title>
</head>
<body>
<% 
	String username = "Java"; 	//定义一个变量
%>	
	<h1>动态包含操作</h1>
	<jsp:include page="receive_param_54.jsp">
		<jsp:param name="name" value="<%=username %>" />
		<jsp:param name="info" value="www.123.cn"/>
	</jsp:include> 	<!-- 标签指令，必须完结 -->

</body>
</html>

