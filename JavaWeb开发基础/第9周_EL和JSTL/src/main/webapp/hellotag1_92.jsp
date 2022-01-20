<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="mytag" uri="gdqy_hello" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>9.2 自定义标签 </title>
</head>
<body>
<!-- 3. hellotag.jsp——编写JSP页面并调用自定义标签 -->
<!-- 使用映射名访问 -->

	<h1> <mytag:hello/> </h1>		<!-- 访问标签 -->
</body>
</html>

