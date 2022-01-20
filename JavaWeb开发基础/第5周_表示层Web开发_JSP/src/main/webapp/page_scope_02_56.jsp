<%@ page language="java" contentType="text/html; charset=GBK"
    pageEncoding="GBK"%>
<%@ page import="java.util.*" %>
<!DOCTYPE html>
<html>

<!-- page·¶Î§ÊôÐÔ
	2. ÔÚÒ»¸öJSPÎÄ¼þÖÐÉèÖÃpageÊôÐÔ£¬ÔÚÁíÍâÒ»¸öJSPÎÄ¼þÖÐ»ñÈ¡¸ÃÊôÐÔ¡£
	page_scope_02.jsp£ºÉèÖÃpageÊôÐÔ.
-->

<head>
<meta charset="ISO-8859-1">
<title>pageÊôÐÔ·¶Î§</title>
</head>
<body>

<%
	//ÉèÖÃÊôÐÔ
	pageContext.setAttribute("name", "ÀîÃ÷");
	pageContext.setAttribute("birthday", new Date());
%>
<jsp:forward page="page_scope_03_56.jsp"/>

</body>
</html>


