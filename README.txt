This script help you to generate raw socket http payload by using hight level http library.

Example:
[SOCKET] b'POST / HTTP/1.1\r\nHost: 127.0.0.1:1337\r\nAccept: */*\r\nAccept-Encoding: gzip, deflate, br\r\nConnection: keep-alive\r\nuser-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36\r\nContent-Length: 20\r\nContent-Type: application/json\r\n\r\n'

Installation:
  pip install httpx
