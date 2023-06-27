
## 1.阅读文本内容，

## 2.常用查找flag方法，可以在Wireshark中通过查找flag关键字的各种编码形式
flag        字符串
666c6167    十六进制
ZmxhZw==    base64

## 3.可以在搜索常见TCP/IP协议，ftp,ssh,smtp,http,tls等来分析相关数据和文件内容

### 3.1 搜索ftp，看到有
ftp登录     zhangsan
RETR        Fl-g.zip,sqlmap.zip文件下载
STOR        /etc/profile文件上传


### 3.2 搜索ftp-data，将Fl-g.zip，sqlmap.zip数据从wireshark导出来

选择一项，Ctrl+F，十六进制查找：504b0304 ，(PK)右键跟踪流-TCP流, 查看原始数据，将数据另存为flag.zip，打开取药密码，无果。sqlmap.zip用同样的方法保存。
```
在线编码解码: https://the-x.cn/encodings/Base64.aspx
在线OCR: https://ocr.space/
在线MD5 Hash：http://www.ip33.com/md5.html

```

### 3.3 搜索smtp.data.fragment，分析一封邮件里面有图片 	filename="image001.png"，将图片base64数据保存到文件，通过python生产文件
```
import base64
import io
import os

current_path = os.path.dirname(__file__)

if __name__ == '__main__':
    # 打开文件
    file1 = current_path + "\\doc\\form"
    file2 = current_path + "\\doc\\later.png"
    f1 = open(file1,"rb")
    f2 = open(file2,"wb")
    # base64.encode(f1,f2)
    base64.decode(f1,f2)
    f1.close()
    f2.close()
```
发现图片貌似是一个rsa的key
在线orc获取文本，进行去空格，保存到文件private.key中
```
-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQDCm6vZmclJrVH1AAyGuCuSSZ8O+mIQiOUQCvN0HYbj8153JfSQ
LsJIhbRYS7+zZ1oXvPemWQDv/u/tzegt58q4ciNmcVnq1uKiygc6QOtvT7oiSTyO
vMX/q5iE2iClYUIHZEKX3BjjNDxrYvLQzPyGD1EY2DZIO6T45FNKYC2VDwIDAQAB
AoGAbtWUKUkx37lLfRq7B5sqjZVKdpBZe4tL0jg6cX5Djd3Uhk1inR9UXVNw4/y4
QGfzYqOn8+Cq7QSoBysHOeXSiPztW2cL09ktPgSlfTQyN6ELNGuiUOYnaTWYZpp/
QbRcZ/eHBulVQLlk5M6RVs9BLI9X08RAl7EcwumiRfWas6kCQQDvqC0dxl2wIjwN
czILcoWLig2c2u71Nev9DrWjWHU8eHDuzCJWvOUAHIrkexddWEK2VHd+F13GBCOQ
ZCM4prBjAkEAz+ENahsEjBE4+7H1HdIaw0+goe/45d6A2ewO/lYH6dDZTAzTW9z9
kzV8uz+Mmo5163/JtvwYQcKF39DJGGtqZQJBAKa18XR16fQ9TFL64EQwTQ+tYBzN
+04eTWQCmH3haeQ/0Cd9XyHBUveJ42Be8/jeDcIx7dGLxZKajHbEAfBFnAsCQGq1
AnbJ4Z6opJCGu+UP2c8SC8m0bhZJDelPRC8IKE28eB6SotgP61ZqaVmQ+HLJ1/wH
/5pfc3AmEyRdfyx6zwUCQCAH4SLJv/kprRz1a1gx8FR5tj4NeHEFFNEgq1gmiwmH
2STT5qZWzQFz8NRe+/otNOHBR2Xk4e8IS+ehIJ3TvyE=
-----END RSA PRIVATE KEY-----

```

可以计算出上面key的MD5 hash值,跟文档中的对比 MD5: 90c490781f9c320cd1ba671fcb112d1c

### 3.4 搜索tls，需要先将上面的私匙加入到wireshark进行解密

- wireshark=》编辑=》首选项=》协议=》TLS，编辑 RSA keys，点击+新建 
    http    C:/tmp/private.key

- 发现tls变成http，直接跟踪流量=》http流就可以看到具体flag啦












