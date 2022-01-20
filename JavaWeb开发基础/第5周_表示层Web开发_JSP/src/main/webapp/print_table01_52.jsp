<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>九九乘法表——使用out.println()输出</title>
</head>

<body>

<%
	int rows = 10;
	int cols = 10;
	out.println("<table border=\"1\" width=\"100%\">");
	for (int x=0; x<rows;x++){
		out.println("<tr>");
		for( int y=0; y<cols; y++){
			out.println("<td>"+ (x*y) + "</td>");
		}
		out.println("</tr>");
	}
	out.println("</table>");
%>
	
</body>

</html>


