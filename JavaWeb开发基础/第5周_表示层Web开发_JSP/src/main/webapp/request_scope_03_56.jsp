<%@ page language="java" contentType="text/html; charset=GBK"
    pageEncoding="GBK"%>
<%@ page import="java.util.*" %>
<!DOCTYPE html>
<html>

<!-- 2. ÉèÖÃºÍ»ñÈ¡request·¶Î§ÊôÐÔ¡ª¡ª¿Í»§¶ËÌø×ª.

	request_scope_03.jsp£ºÉèÖÃrequest·¶Î§ÊôÐÔ£¬³¬Á´½ÓÌø×ª£¬ÎÞ·¨»ñÈ¡ÊôÐÔ.	
-->

<head>
<meta charset="ISO-8859-1">
<title>ÉèÖÃrequest·¶Î§ÊôÐÔ¡ª¡ª¡ª¡ª³¬Á´½ÓÌø×ª</title>
</head>
<body>

<% 	// ÉèÖÃÊôÐÔ
	request.setAttribute("name", "ÀîÃ÷");
	request.setAttribute("birthday", new Date());
%>
<a href="request_scope_02_56.jsp">Í¨¹ýÁ´½ÓÈ¡µÃÊôÐÔ</a>

</body>
</html>


