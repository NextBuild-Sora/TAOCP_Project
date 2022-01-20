<%@ page language="java" contentType="text/html; charset=GBK"
    pageEncoding="GBK"%>
<%@ page import="java.util.*" %>
<!DOCTYPE html>
<html>

<!-- 
	.
-->

<head>
<meta charset="ISO-8859-1">
<title>»ñÈ¡  ·¶Î§ÊôÐÔ</title>
</head>
<body>

<%
	String username = (String)application.getAttribute("name");
	Date userbirthday = (Date)application.getAttribute("birthday");
%>
<h2>ÐÕÃû£º<%=username %></h2>
<h2>ÉúÈÕ£º<%=userbirthday %></h2>

</body>
</html>


