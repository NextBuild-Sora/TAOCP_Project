<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>session范围的JavaBean</title>
</head>

<jsp:useBean id="cou" scope="session" class="JavaBean_7.Count_73"/>
<body>

<h3>第 <jsp:getProperty name="cou" property="count" />次访问</h3>


</body>
</html>


