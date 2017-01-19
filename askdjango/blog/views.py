from django.http import HttpResponse
from django.shortcuts import render

def post_list(request):
    return HttpResponse("""
<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<title>장고 블로그</title>
<style>
body {
    background-color: pink;
}
</style>
</head>
<body>
    안녕. 장고야. 넌 참 아름답구나.
</body>
</html>
""")
