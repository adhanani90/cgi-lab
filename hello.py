#!/usr/bin/env python3

import cgi, os, json
 

environmentData = os.environ


jsonData = json.loads('{}')
queryData = "No query data"
userAgent = "No user agent"
for key, value in environmentData.items():
    jsonData[key] = value
    if key == 'QUERY_STRING':
        queryData = value
    elif key == "HTTP_USER_AGENT":
        userAgent = value
        
    
            
    




print("Content-type: text/html")

print("<html>")
print("<head>")
print("<title>CGI Test</title>")
print("</head>")
print("<body>")
print(f"<p>As a json file : {jsonData}</p>")
print(f"<p>query string : {queryData}</p>")
print(f"<p>user agent : {userAgent}</p>")
print("</body>")
print("</html>")
