<%@ page language="java" contentType="text/html; charset=GBK"
    pageEncoding="GBK"%>
<%@ page import="java.util.*" %>
<!DOCTYPE html>
<html>

<!-- page·¶Î§ÊôÐÔ
	1. ÔÚÒ»¸öJSPÎÄ¼þÖÐÉèÖÃpageÊôÐÔ£¬È»ºóÖ±½ÓÔÚ±¾Ò³ÃæÖÐÈ¡³öÊôÐÔ¡£
	page_scope_01.jsp £ºÉèÖÃºÍ»ñÈ¡page·¶Î§µÄÊôÐÔ 	
-->

<head>
<meta charset="ISO-8859-1">
<title>pageÊôÐÔ·¶Î§</title>
</head>
<body>

<%
	pageContext.setAttribute("name", "ÀîÃ÷");
	pageContext.setAttribute("birthday", new Date());
%>
<%
	String username = (String)pageContext.getAttribute("name");
	Date userbirthday = (Date)pageContext.getAttribute("birthday");
%>
<h2>ÐÕÃû£º<%=username %></h2>
<h2>ÉúÈÕ£º<%=userbirthday %></h2>
</body>
</html>


