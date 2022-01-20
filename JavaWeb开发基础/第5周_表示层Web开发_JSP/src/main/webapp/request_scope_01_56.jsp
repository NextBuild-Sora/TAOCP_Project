<%@ page language="java" contentType="text/html; charset=GBK"
    pageEncoding="GBK"%>
<%@ page import="java.util.*" %>
<!DOCTYPE html>
<html>

<!-- request·¶Î§ÊôÐÔ

	1. ÉèÖÃºÍ»ñÈ¡request·¶Î§ÊôÐÔ¡ª¡ª·þÎñÆ÷¶ËÌø×ª

	request_scope_01.jsp£ºÉèÖÃrequest·¶Î§µÄÊôÐÔ£¬·þÎñÆ÷¶ËÌø×ª£¬ÄÜ¹»»ñÈ¡ÊôÐÔ
		
-->

<head>
<meta charset="ISO-8859-1">
<title>ÉèÖÃrequest·¶Î§ÊôÐÔ¡ª¡ªforwardÌø×ª</title>
</head>
<body>

<% 	// ÉèÖÃÊôÐÔ
	request.setAttribute("name", "ÀîÃ÷");
	request.setAttribute("birthday", new Date());
%>
<jsp:forward page="request_scope_02_56.jsp"/>

</body>
</html>


