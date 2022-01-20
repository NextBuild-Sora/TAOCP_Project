<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>

<!--5.2 JSP注释及脚本 -->
<!-- 注释 -->

<body>
	<%
		int x=10;
		String info = "hello";
		out.println("<h2>x="+x+"</h2>");
		out.println("<h2>info="+info+"</h2>");
		
	%>>


</body>
</html>