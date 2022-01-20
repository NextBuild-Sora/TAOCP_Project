<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.sql.*" %>
<%@ page import="javax.sql.*" %>
<%@ page import="javax.naming.*" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>

<body>

<!-- 6.5 Tomcat数据库连接池 -->

<%
DataSource ds = null;
try{
	InitialContext ctx= new InitialContext();
	ds = (DataSource)ctx.lookup("java:comp/env/jdbc/TestDB");
	Connection conn = ds.getConnection();
	Statement stmt = conn.createStatement();
	String strSql = "select * from Login";
	ResultSet rs = stmt.executeQuery(strSql);
	while(rs.next()){
		out.println(rs.getString(2));
	}
}catch(Exception e){
	out.prinltn(e.getMessage());
}
%>

</body>
</html>