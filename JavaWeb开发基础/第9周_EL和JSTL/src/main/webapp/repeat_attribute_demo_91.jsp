<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>设置指定范围属性</title>
</head>
<body>

<%
	// 注意：属性按照如下顺序查找：page->request->session->application
	pageContext.setAttribute("info","page属性范围") ;
	request.setAttribute("info","request属性范围") ;
	session.setAttribute("info","session属性范围") ;
	application.setAttribute("info","application属性范围") ;
%>
<h3>${info}</h3>

<h2>*******************************</h2> 

<h3>${pageScope.info}</h3>
<h3>${requestScope.info }</h3>
</body>

</html>

