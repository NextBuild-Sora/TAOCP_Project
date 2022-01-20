<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>

<!--5.2 JSP注释及脚本 -->
<!-- 脚本 -->

<body>

<%
	int x=10;
%>
<%!
	String s="hello";
	public int add(int x, int y){
		return x+y;
	}
%>
<%!
	class Person{
	private String name;
	public String getName(){
		return name;
	}
}
%>

</body>
</html>