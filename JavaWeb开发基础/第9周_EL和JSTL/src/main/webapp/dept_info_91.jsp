<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>使用表达式语言获取单个部门信息</title>
</head>
<body>

<!-- 

 * 
 * 第9周 EL和JSTL
 * --9.1 EL表达式语言--
 * --在MVC中应用表达式语言--
 * --3. dept_info.jsp——接收request属性并输出--
 * 
 
 -->
 
 <h3>编号 ${deptinfo.deptno} </h3>
 <h3>名称 ${deptinfo.dname} </h3>
 <h3>位置 ${deptinfo.loc} </h3>
 
</body>
</html>