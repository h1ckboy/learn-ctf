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