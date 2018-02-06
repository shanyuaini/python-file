
#privoxy + genpac + v2ray(ss)
亲测TCP BBR 配合ss或者是v2ray上油管看1080是没有丝毫问题.

##v2ray
客户端和服务端安装都很简单,就简单说一下配置
1, 服务端配置
```
{
  "log" : {
        ...                     //配置日志
  },
  "inbound": {                  //进入服务器方向的配置
    "port": 8899,               //服务器上提供客户端连接端口
    "protocol": "vmess",        //协议,支持ss
    "settings": {
      "clients": [
        {
          "id": "fcbaef0f-e3f5-4d64-a12d-0318d0804d69",     //数据加密解密密钥可自定义
          "level": 1,
          "alterId": 64
        }
      ]
    }
  },
  "outbound": {                 //服务器出口方向默认freedom,即不限制
    "protocol": "freedom",
    "settings": {}
  },
...                             //其他配置,也可不配
}

```

2, 客户端配置

```
{
  "inbound": {                  //客户端入口配置,通常
    "port": 1080,               //客户端接受其他程序转发请求的服务端口
    "protocol": "socks",        //客户端接受的协议
    "settings": {
      "auth": "noauth"          //通常为本机所以不需要验证
    }
  },
  "outbound": {                 //客户端传出方向只需要和服务端一一对应
    "protocol": "vmess",        //客户端传给服务端的加密协议
    "settings": {
      "vnext": [
        {
          "address": "xxx.xx.xx.xx",    //服务端地址
          "port": 8899,                 //服务端监听端口
          "users": [
            {
              "id": "fcbaef0f-e3f5-4d64-a12d-0318d0804d69", //服务端所需要的密钥
              "alterId": 64
            }
          ]
        }
      ]
    }
  }
}

```

##ss
安装和配置都很简单,服务端和客户端配置文件即可,服务端用ssserver 客户端用sslocal

```
pip install shadowsocks
vi /etc/shadowsocks
{
    "server":"xxx.xxx.xxx.xxx",
    "server_port":8888,
    "local_address": "127.0.0.1",
    "local_port":1080,
    "password":"passwd",
    "timeout":300,
    "method":"aes-256-cfb",
    "fast_open": true,
    "workers": 1
}
```

由于pip安装,没有启动脚本

```
#服务端类似
[Unit]
Description=Shadowsocks
After=network.target

[Service]
ExecStart=/usr/bin/python /usr/local/bin/sslocal -c /etc/shadowsocks.json

[Install]
WantedBy=multi-user.target
```

##genpac
帮助ss,v2ray客户端智能解析

```
pip install genpac
mkdir mypac && cd mypac && touch user-rules.txt
genpac --pac-proxy "SOCKS5 127.0.0.1:1080" --gfwlist-proxy="SOCKS5 127.0.0.1:1080" --output="autoproxy.pac" --gfwlist-url="https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt" --user-rule-from="user-rules.txt"
```
ubuntu设置系统代理setting-->network-->autoproxy 和浏览器中找到代理服务器配置PAC代理填入即可:

```
/home/sylar/paclist/autoproxy.pac
```

## privoxy setting
将http和https请求转换为socks5发送给客户端,chrome或其他浏览器只需要配置自动代理PAC就可以自动识别代理不需要这一步,这是为了终端和其他程序使用

```
apt install privoxy
vi /etc/privoxy/config
listen-address  localhost:8118
forward-socks5 / 127.0.0.1:1080 .
sudo /etc/init.d/privoxy start
```


bashrc 启用代理,
export http_proxy="http://127.0.0.1:8118"
export https_proxy="https://127.0.0.1:8118"