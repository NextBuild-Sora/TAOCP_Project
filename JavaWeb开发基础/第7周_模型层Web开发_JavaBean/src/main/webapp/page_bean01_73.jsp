<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>page范围的JavaBean</title>
</head>

<jsp:useBean id="cou" scope="page" class="JavaBean_7.Count_73"/>
<body>

<h3>第 <jsp:getProperty name="cou" property="count" /> 次访问</h3>
<jsp:forward page="page_bean02_73.jsp"/>
 
</body>
</html>

