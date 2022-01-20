<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.util.*" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>输出Collection接口集合</title>
</head>
<body>

<%
	List all = new ArrayList();

	//向集合中增加内容
	all.add("ni");
	all.add("www");
	all.add("20@con");
	// 向request集合中保存
	
	request.setAttribute("allinfo",all);
%>
<h3>第一个元素：${allinfo[0] }</h3>
<h3>第二个元素：${allinfo[1] }</h3>
<h3>第三个元素：${allinof[2] }</h3>

</body>

</html>