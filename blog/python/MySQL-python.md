Win10 MySQL-python
=



在Windows 下调试 Python 还是挺麻烦的.通过PyCharm 来安装个MySQL-python 的库都搞了大半天.分别尝试 1.2.3,1.2.4和1.2.5都有不同的错误.需要解决的问题就是这个:“Cannot open include file: 'config-win.h': No such file or directory” while installing mysql-python"



安装步骤如下：

1. 安装 Microsoft Visual C++ Compiler Package for Python 2.7
[点击链接](http://www.microsoft.com/en-us/download/details.aspx?id=44266)  
默认安装的路径C:\Users\admin\AppData\Local\Programs\Common\Microsoft\Visual C++ for Python\

2. 安装 MySQL Connector C 6.0.2
[点击链接](https://dev.mysql.com/downloads/connector/c/6.0.html)  
也可以下载MYSQL的官方工具安装:
![](http://7xread.com1.z0.glb.clouddn.com/4ceccbff-0bbc-4ca9-b91c-05877e431df5)


3. 下载 MySQL-python 1.2.5 源码包
[点击链接](https://pypi.python.org/pypi/MySQL-python/1.2.5)


4. 解压源码包后，修改 site.cfg 文件。
实际上，如果你是在32 位系统上部署，那么通过pip install 安装MySQL-python 1.2.5 只需进行上面的依赖包安装即可。
但在 64 位环境中，就会提示“Cannot open include file: 'config-win.h'” 的错误。
原因就是 site.cfg 中写的 MySQL Connector C 为32 位版本。
原来的 site.cfg 文件内容如下：

```
# http://stackoverflow.com/questions/1972259/mysql-python-install-problem-using-virtualenv-windows-pip
# Windows connector libs for MySQL. You need a 32-bit connector for your 32-bit Python build.
connector = C:\Program Files (x86)\MySQL\MySQL Connector C 6.0.2

修改为：
connector = C:\Program Files\MySQL\MySQL Connector C 6.0.2
```

> PS: pycrypto
[点击链接](http://www.voidspace.org.uk/python/modules.shtml#pycrypto)
