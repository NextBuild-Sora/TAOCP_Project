<%@ page language="java" contentType="text/html; charset=GBK"
    pageEncoding="GBK"%>
<%@ page import="java.util.*" %>
<!DOCTYPE html>
<html>

<!-- page·¶Î§ÊôÐÔ
	page_scope_03.jsp£ºÈ¡µÃpage·¶Î§µÄÊôÐÔ£¨ÎÞ·¨È¡µ½
-->

<head>
<meta charset="ISO-8859-1">
<title>pageÊôÐÔ·¶Î§</title>
</head>
<body>

<%
	String username = (String)pageContext.getAttribute("name");
	Date userbirthday = (Date)pageContext.getAttribute("birthday");
%>

<h2>ÐÕÃû£º<%=username %></h2>
<h2>ÉúÈÕ£º<%=userbirthday %></h2>
</body>

</html>



