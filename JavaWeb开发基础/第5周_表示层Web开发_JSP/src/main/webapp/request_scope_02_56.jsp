<%@ page language="java" contentType="text/html; charset=GBK"
    pageEncoding="GBK"%>
<%@ page import="java.util.*" %>
<!DOCTYPE html>
<html>

<!-- 
	request_scope_02.jsp£ºÈ¡µÃrequest·¶Î§µÄÊôÐÔ.
-->

<head>
<meta charset="ISO-8859-1">
<title>»ñÈ¡request·¶Î§ÊôÐÔ</title>
</head>
<body>

<%
	String username = (String)request.getAttribute("name");
	Date userbirthday = (Date)request.getAttribute("birthday");
%>
<h2>ÐÕÃû£º<%=username %></h2>
<h2>ÉúÈÕ£º<%=userbirthday %></h2>

</body>
</html>


