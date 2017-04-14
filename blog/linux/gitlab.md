gitlab and gitlab-ci
=
中文文档: [点击链接](https://docs.gitlab.com.cn/ce/README.html)  

源码安装需要的环境

```
yum update -y
yum groupinstall "Development tools" -y
yum install gcc autoconf cmake unzip vim libcurl-devel zlib-devel curl-devel expat-devel gettext-devel openssl-devel perl-devel nodejs libicu-devel  wget curl -y
tar zxvf git-2.7.4.tar.gz
```

git
=====
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

ruby
=====

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

go
=====

```
wget https://storage.googleapis.com/golang/go1.8.linux-amd64.tar.gz
tar -C /usr/local -xzf go1.8.linux-amd64.tar.gz
export GOROOT=$HOME/go
export PATH=$PATH:/usr/local/go/bin
echo 'export GOROOT=$HOME/go' >> /etc/profile 
echo 'export PATH=$PATH:/usr/local/go/bin' >> /etc/profile 

```


YUM安装和汉化
=====

按照文档操作就可以了
安装文档: [点击链接](https://gitlab.com/gitlab-org/gitlab-ce/blob/master/doc/install/installation.md)  
汉化文档: [点击链接](https://gitlab.com/xhang/gitlab)


runner
=====


```
1.添加 Runner 安装源
curl -L https://packages.gitlab.com/install/repositories/runner/gitlab-ci-multi-runner/script.rpm.sh | sudo bash
yum install gitlab-ci-multi-runner

2 注册


[root@localhost ~]# gitlab-ci-multi-runner register
Running in system-mode.                            
                                                   
Please enter the gitlab-ci coordinator URL (e.g. https://gitlab.com/):
http://gitlab.home.com/ci
Please enter the gitlab-ci token for this runner:
i6Q_gr3htrKpTvzmjsmF
Please enter the gitlab-ci description for this runner:
[localhost.localdomain]: test #gitlab上标识runner机器。
Please enter the gitlab-ci tags for this runner (comma separated):
test,note 				#分支名
Whether to run untagged builds [true/false]:
[false]: false
Whether to lock Runner to current project [true/false]:
[false]: false
Registering runner... succeeded                     runner=i6Q_gr3h
Please enter the executor: shell, ssh, docker-ssh+machine, kubernetes, docker, docker-ssh, parallels, virtualbox, docker+machine:
shell
Runner registered successfully. Feel free to start it, but if it's running already the config should be automatically reloaded! 
```

项目的runner信息查看


![](http://7xread.com1.z0.glb.clouddn.com/20feaf74-417d-4ec9-a225-a59105930418)



在gitlab新建一个分支添加
```
.gitlab-ci.yml

stages:
  - deploy
deploy_staging:
  stage: deploy
  script:
    - echo "Deploy to staging server"  #这里用脚本好操作一些。。
    - cd /data/phptest
    - git checkout test
    - git pull
  only:
  - test
```

先到runner机器上git clone 这个分支并把/data/phptest权限给用户gitlab-runner
这样每次push就会自动发布到runner机器上（注意权限问题）


>>PS: gitlab整套工具还可以做一些自动化测试的工作，需要按照需求做一些调整，这只是一个简单的例子


