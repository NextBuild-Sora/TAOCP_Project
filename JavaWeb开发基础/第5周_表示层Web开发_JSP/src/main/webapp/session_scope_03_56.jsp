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
<title>»ñÈ¡session·¶Î§ÊôÐÔ</title>
</head>
<body>

<%
	String username = (String)session.getAttribute("name");
	Date userbirthday = (Date)session.getAttribute("birthday");
%>
<h2>ÐÕÃû£º<%=username %></h2>
<h2>ÉúÈÕ£º<%=userbirthday %></h2>

</body>
</html>


