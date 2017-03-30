#CSS

###一,书写规范

#####css代码的三种书写方式
主要有三种:1代码段中定义,2在头部定义,3单独的css文件.后面两种主要是为了代码的复用.写在不同位置的css代码有细微的区别
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="/css/somefile.css"><!-- 引用一个外部的css文件 -->
    <style>        /* 在头部定义css */
        .test{
            color:  black;
            font-size: 36px;
        }
    </style>
</head>
<body>
    <div class="test">
        引用头部中定义的css函数,可以在文件中任意位置引用
    </div>
    <div style="background-color: red">
        直接在代码中用style属性编写,只在本段代码容器中生效
    </div>
    <div class="test">
        引用头部中定义的css函数,可以在文件中任意位置引用
    </div>
</body>
</html>
```
#####css选择器
1. class选择器, 在头部用.word定义一个css样式.在代码段中用class属性引用.  

```
.test{
    color:  red;
}
<div class="test">

</div>
```
2. 标签选择器, 将默认的html标签样式改为自定义样式.例如修改a标签,

```
<style>
	a{
	    color:  red;
	}
</style>
<a>a标签是什么颜色</a>
```
<style>
	a{
	    color:  red;
	}
</style>
> <a>a标签是什么颜色</a>

>>>PS:input标签可以通过input[type='text']{}对不同的input类型进行自定义

3. id选择器,通过id属性修改css样式

```
<style>
	#i1{
	    color:  blue;
	}
</style>
<a>i1是什么颜色</a>
```
<style>
	#i1{
	    color:  blue;
	}
</style>
> <a id="i1">i1是什么颜色</a>

4. 层级选择器,通过每层标签定义单独的样式,就算其他地方class同名也不会引用.

```
<style>
    .test1{
        color: blue;
    }
    .test1 p .test2{
        color: red;
    }
</style>
<div class="test1">
    选中test1的blue
    <p>
        选中test1的blue
            <span class="test2">
                span选中test2
            </span>
    </p>
</div>
<span class="test2">span没选中test2</span>
```

> <style>
    .test1{
        color: blue;
    }
    .test1 p .test2{
        color: red;
    }
</style>
<div class="test1">
    选中test1的blue
    <p>
        选中test1的blue
            <span class="test2">
                span选中test2
            </span>
    </p>
</div>
<span class="test2">span没选中test2</span>

>>层级选择器中class,id,标签选择器都可以作为路径.

5. 组合选择器, 同时定义多个属性相同的选择器用逗号(,)分割

```
.test1, .test1 p .test2{
    color: red;
}
```

###二,常用CSS样式

#####display

定义标签类型:

none:隐藏  
block:将标签定义为块级标签  
inline:将标签定义为内联标签  
```
<div style="display: none; background-color: black">
    none被隐藏
</div>
<span style="display: block; ; background-color: red">
    span是内联标签
</span>
<div style="display: inline; background-color: yellow">
    div是块级标签
</div>
```


#####背景background
css: [点击](http://www.w3school.com.cn/css/css_background.asp)  
css3:[点击](http://www.w3school.com.cn/css3/css3_background.asp)

```
.b1{
	background-repeat: norepeat;/*图片不重复或者在那个方向上重复repeat, repeat-x,repeat-y*/
	height: 800px;  #高
	width: 600px;   #宽
	color: red;
	background-image: url("http://website/url"); #背景图
	background-position: 0 0;/* 图片蒙板移动*/
}
```
#####链接a: 系列

鼠标选中框. text-decoration去除下划线

a:link 链接未点击上去时候  
a:visited 链接已经点击过的  
a:hover 鼠标放在链接上未点击  
a:active 是介于hover visited 之间的一个状态，可以说是链接被按下时候的状态  

```
<style type="text/css">
.m a:link, a:visited {
  border-style: solid;
  border-width: 5px;
  border-color: transparent;
  }
.m a:hover {
  border-color: gray;
  text-decoration:none
  }
</style>
<div class="m">
    <a href="#">AAA</a>
</div>
<a href="#">BBB</a>
```

> <style type="text/css">
.m a:link, a:visited {
  border-style: solid;
  border-width: 5px;
  border-color: transparent;
  }
.m a:hover {
  border-color: gray;
  text-decoration:none
  }
</style>
<div class="m">
    <a href="#">AAA</a>
</div>
<a href="#">BBB</a>

#####cursor鼠标样式

常用样式: pointer,help,wait,move,crosshair

```
<span style="cursor: pointer; ; background-color: red">
    鼠标cursor: pointer
</span>
<span style="cursor: url(images/favicon2.ico),auto; ; background-color: yellow">
    鼠标cursor: 自定义
</span>
```

><span style="cursor: pointer; ; background-color: red">
    鼠标cursor: pointer
</span>
<span style="cursor: url(images/favicon2.ico),auto; ; background-color: yellow">
    鼠标cursor: 自定义
</span>

#####边框border  
文档: [点击](http://www.w3school.com.cn/css/css_border.asp)
1. 框体border-style

```
.aside {border-style: solid dotted dashed double;}
<p class="aside">111</p>
```
> <style>
> .aside {border-style: solid dotted dashed double;}
> </style>
> <p class="aside">111</p>

上面这条规则为类名为 aside 的段落定义了四种边框样式：实线上边框、点线右边框、虚线下边框和一个双线左边框.我们又看到了这里的值采用了 top-right-bottom-left 的顺序，讨论用多个值设置不同内边距时也见过这个顺序。

2. border-width 为边框指定宽度

```
.allside {border-style: solid; border-width: 5px;}
```

也可以按照 top-right-bottom-left 的顺序设置元素的各边边框  
```
.allside {border-style: solid; border-width: 15px 5px 15px 5px;}
```
上面的例子也可以简写为（这样写法称为值复制,第一个是上下,第二个左右）  
```
.allside {border-style: solid; border-width: 15px 5px;}
```
>>PS:边框样式为 none，即边框根本不存在，那么边框就不可能有宽度，因此边框宽度自动设置为 0

3. border-color 边框颜色,和上面的差不多的设置规则,有一个特殊属性transparent透明边框

4. padding 内边距和margin 外边距
框的最内部分是实际的内容，直接包围内容的是内边距。内边距呈现了元素的背景。内边距的边缘是边框。边框以外是外边距，外边距默认是透明的，因此不会遮挡其后的任何元素也适合框的一些属性值.

内边距: [点击](http://www.w3school.com.cn/css/css_padding.asp) 简单说就是把边框从内像外撑大  
外边距: [点击](http://www.w3school.com.cn/css/css_margin.asp) 简单说就是把边框从外像内变小

![框图](http://7xread.com1.z0.glb.clouddn.com/9d0fd2cf-865e-4046-9b3b-71038f07bc46)


#####定位position
div、h1 或 p 元素常常被称为块级元素(块级标签)。这意味着这些元素显示为一块内容，即“块框”。与之相反，span 和 strong 等元素称为“行内元素”(内联标签)，这是因为它们的内容显示在行中.即“行内框”
position:有4个属性

- static: 元素框正常生成。块级元素生成一个矩形框，作为文档流的一部分，行内元素则会创建一个或多个行框，置于其父元素中。(默认)  
- relative: 元素框偏移某个距离。元素仍保持其未定位前的形状，它原本所占的空间仍保留。(相对)  
```
<style type="text/css">
h2.pos_left
{
position:relative;
left:-20px
}
h2.pos_right
{
position:relative;
left:20px
}
</style>
<h2>这是位于正常位置的标题</h2>
<h2 class="pos_left">这个标题相对于其正常位置向左移动</h2>
<h2 class="pos_right">这个标题相对于其正常位置向右移动</h2>
<p>相对定位会按照元素的原始位置对该元素进行移动。</p>
<p>样式 "left:-20px" 从元素的原始左侧位置减去 20 像素。</p>
<p>样式 "left:20px" 向元素的原始左侧位置增加 20 像素。</p>
```
<style type="text/css">
h2.pos_left
{
position:relative;
left:-20px
}
h2.pos_right
{
position:relative;
left:20px
}
</style>
><h2>这是位于正常位置的标题</h2>
<h2 class="pos_left">这个标题相对于其正常位置向左移动</h2>
<h2 class="pos_right">这个标题相对于其正常位置向右移动</h2>
<p>相对定位会按照元素的原始位置对该元素进行移动。</p>
<p>样式 "left:-20px" 从元素的原始左侧位置减去 20 像素。</p>
<p>样式 "left:20px" 向元素的原始左侧位置增加 20 像素。</p>


- absolute: 元素框从文档流完全删除，并相对于其包含块定位。包含块可能是文档中的另一个元素或者是初始包含块。元素原先在正常文档流中所占的空间会关闭，就好像元素原来不存在一样。元素定位后生成一个块级框，而不论原来它在正常流中生成何种类型的框。(绝对)  
```
<h2 style="position: absolute;left: 150px;top: 5600px; color: red">这是带有绝对定位的标题,是针对父框体,一般是整个页面</h2>
```
<p style="position: absolute;left: 150px;top: 5600px; color: red">这是带有绝对定位的标题,是针对父框体,一般是整个页面</p>
如果想要将absolute限制在一个框体内,父框体就要用relative,下面这段代码就可以尝试去除relative,定位两个字就会飘到整个页面的底部
```
<div style="position:relative;background-color: yellow; height: 100px;width: 100px;">
    <p style="position: absolute;left: 30px;bottom: 30px; color: red">定位</p>
</div>
```
><div style="position:relative;background-color: yellow; height: 100px;width: 100px;">
    <p style="position: absolute;left: 30px;bottom: 30px; color: red">定位</p>
</div>


- fixed: 元素框的表现类似于将 position 设置为 absolute，不过其包含块是视窗本身。(固定)  
```
<div style="position: fixed; top: 40px; right: 20px">
    fixed是相对于客户端窗口固定定位
</div>
<div style="background-color: green;height: 5000px"></div>
```

#####层级 z-index
不同页面的层级,数值越大的越上层,例如配合fixed做一个要求登录的窗口

```
<div style="z-index:11;background-color:red ;  position: fixed; top:0px; left: 0px; bottom: 0px; right: 0px;opacity: 0.9">
    <h2 style="position: absolute;left: 50%;top: 45%; color:white">第1层红</h2>
</div>
<div style="z-index:10;background-color:black ; position: fixed; top:0px; left: 0px; bottom: 0px; right: 0px"">
    <h2 style="position: absolute;left: 50%;top: 50%; color:white">第2层黑</h2>
</div>
```

<div></div>
------






##### 浮动 float
浮动是针对父框体对框体进行定位,

>>父框体没有定义height,当子框体使用float时父框体就不会根据子框体增长(设置的背景色也不会生效),需要在子框体中定义一个clear:both的属性()

```
<div  style="width: 200px;background-color: black">
    <div style="background-color: red;float:left;width: 80%">float的both</div>
    <div style="clear:both;"></div>
</div>
<div style="width: 200px;background-color: black">
    <div style="background-color: red;float:left;width: 20%">float1</div>
    <div style="background-color: yellow;float:left;width: 30%">float2</div>
    <div style="background-color: blue;float:right;width: 30%">float3</div>
    <!--<div style="clear:both;"></div>-->
</div>
```

><div  style="width: 200px;background-color: black">
    <div style="background-color: red;float:left;width: 80%">浮动的</div>
    <div style="clear:both;"></div>
</div>
> <div style="width: 200px;background-color: black">
    <div style="background-color: red;float:left;width: 30%">浮动的</div>
    <div style="background-color: yellow;float:left;width: 30%">浮动的</div>
    <div style="background-color: blue;float:right;width: 30%">浮动的</div>
</div>    

<div></div>
------


#####透明度opacity
从0-1表示百分比  
```
<div style="opacity: 0.4;background-color:red ; height: 100px;width: 100px;float: left;">
    透明度
</div>
<div style="background-color:red ; height: 100px;width: 100px;float: left;">
    无透明度
</div>
```
> <div style="opacity: 0.4;background-color:red ; height: 100px;width: 100px;float: left;">
    透明度
</div>
<div style="background-color:red ; height: 100px;width: 100px;float: left;">
    无透明度
</div>