<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<div class="col-md-12 navbar-inverse">
				<div>
					<div class="navbar-header">
						<a class="navbar-brand" href="#">信息管理系统</a>
					</div>
					<div style="float: right; margin-top: 20px; text-align: center;"">
						<font color="red"><%= session.getAttribute("info") %></font>
						<a href="LoginOutServlet">安全退出</a>
					</div>
				</div>
</div>