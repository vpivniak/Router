<!DOCTYPE>
<html>
<head>
    <meta charset = "utf-8">
    <title>Hello web</title>
</head>
<body>
    {% set navigation = [ "news", "category", "articles" ] %}
    {% set title = 'Hello on homepage' %}
	<h1>{{ title }}</h1>
    <ul id="navigation">
    {% for item in navigation %}
        <li><a href="{{ item }}">{{ item }}</a></li>
    {% endfor %}
    </ul>
</body>
</html>