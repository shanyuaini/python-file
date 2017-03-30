#gitlab-ci
中文文档: [点击链接](https://docs.gitlab.com.cn/ce/README.html)  
安装文档: [点击链接](https://gitlab.com/gitlab-org/gitlab-ce/blob/master/doc/install/installation.md)  
汉化文档: [点击链接](https://gitlab.com/xhang/gitlab)



```
yum update -y
yum groupinstall "Development tools" -y
yum install gcc autoconf cmake unzip vim libcurl-devel zlib-devel curl-devel expat-devel gettext-devel openssl-devel perl-devel nodejs libicu-devel  wget curl -y
tar zxvf git-2.7.4.tar.gz
```

#####git
```
yum remove git -y
mkdir /tmp/git && cd /tmp/git
curl -O --progress https://www.kernel.org/pub/software/scm/git/git-2.7.4.tar.gz
tar -xzf git-2.7.4.tar.gz
cd git-2.7.4
./configure
make prefix=/usr/local all
make prefix=/usr/local install
```

#####ruby

```
mkdir /tmp/ruby && cd /tmp/ruby
curl -O https://cache.ruby-lang.org/pub/ruby/2.4/ruby-2.4.1.tar.gz
tar xzf ruby-2.1.8.tar.gz
cd ruby-2.1.8
./configure --disable-install-rdoc
make && make install

#国内使用Ruby的Gem和Bundler必须要做的事情:
# 修改git用户gem安装源为中科大源
$  su  git
$  gem sources --add https://gems.ruby-china.org/ --remove 
# 确保git用户当前gems源为中科大源
$  gem sources -l
*** CURRENT SOURCES ***

#安装bundle包(root用户)
gem install bundler --no-ri --no-rdoc

```

#####go

```
wget https://storage.googleapis.com/golang/go1.8.linux-amd64.tar.gz
tar -C /usr/local -xzf go1.8.linux-amd64.tar.gz
export GOROOT=$HOME/go
export PATH=$PATH:/usr/local/go/bin
echo 'export GOROOT=$HOME/go' >> /etc/profile 
echo 'export PATH=$PATH:/usr/local/go/bin' >> /etc/profile 

```




