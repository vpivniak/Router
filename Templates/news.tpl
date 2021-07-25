<!DOCTYPE>
<html>
<head>
    <meta charset = "utf-8">
    <title>News</title>
</head>
<body>
    {% set articles = [ 'Alien found', 'Trump eat house', 'People on Mars' ] %}
    <h1>Сегодняшние новости</h1>
    <ul id="news">
	    {% for item in articles %}
	    	<li><a href="{{ item }}">{{ item }}</a></li>
	    {% endfor %}
	</ul>
</body>
</html>