<%@ page language="java" contentType="text/html; charset=GBK"
    pageEncoding="GBK"%>
<%@ page import="java.util.*" %>
<!DOCTYPE html>
<html>

<!--
	

-->

<head>
<meta charset="ISO-8859-1">
<title>ÉèÖÃsession·¶Î§ÊôÐÔ¡ª¡ª¡ª¡ª³¬Á´½ÓÌø×ª</title>
</head>
<body>

<% 	// ÉèÖÃÊôÐÔ
	session.setAttribute("name", "ÀîÃ÷");
	session.setAttribute("birthday", new Date());
%>
<a href="session_scope_03_56.jsp">Í¨¹ýÁ´½ÓÈ¡µÃÊôÐÔ</a>

</body>
</html>


