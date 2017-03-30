#HTML
超级文本标记语言是标准通用标记语言下的一个应用,也是一种规范,一种标准,它通过标记符号来标记要显示的网页中的各个部分.结构包括“头”部分（英语：Head）,和“主体”部分（英语：Body）,其中“头”部提供关于网页的信息,“主体”部分提供网页的具体内容。  
html详细文档: [点击](http://www.runoob.com/html/html-tutorial.html)

###书写规范
```
<!DOCTYPE html> 				#申明html版本
<html lang="en"> 				#申明语言
	<head>						#head申明网页信息
	    <meta charset="UTF-8">	#申明编码meta标签可以定义很多其他属性
	    <title>html入门</title>
	    <link rel="shortcut icon" href="images/favicon2.ico" type="image/x-icon">				
	    						#icon
	    <style></style>			#css代码或者文件引用
	    <script></script>		#js代码或者文件引用
	</head>
	
	<body>						#页面代码
		Some html code!
	</body>
</html>
```

###head头部内使用的标签

#####meta标签  
HTML文档的元数据。元数据不会显示在客户端，但是会被浏览器解析。META元素通常用于指定网页的描述，关键词，文件的最后修改时间，作者及其他元数据。  
meta标签文档:[点击](http://www.w3school.com.cn/tags/tag_meta.asp)
```
<meta charset="UTF-8">
```


#####title标签  
定义网站标题
```
<title>html入门</title>
```

#####link标签  
<link> 标签定义文档与外部资源的关系,通常用于引用icon和css  
link标签文档:[点击](http://www.w3school.com.cn/tags/tag_link.asp)
```
<link rel="shortcut icon" href="images/favicon2.ico" type="image/x-icon">
<link rel="stylesheet" type="text/css" href="/html/csstest1.css" >
```

#####style和script标签  
可在head定义也可以写在body中style用于定义CSS代码,script用于定义JS代码.后面css和js中详细说.


###body中的标签分类  


1. 块级标签  
块级标签:总是在新行上开始；高度，行高以及顶和底边距都可控制；宽度缺省是它的容器的100%，除非设定一个宽度。display:block就是将元素显示为块级元素。  

```
    <div></div>
    <p></p>
    <h1></h1>
    <form></form>
    <ul></ul>
    <li></li>
```



2. 内联标签
内联标签:和其他元素都在一行上；高，行高及顶和底边距不可改变；宽度就是它的文字或图片的宽度，不可改变。display:inline就是将元素显示为行内元素.  

```
    <span></span>
    <a></a>
    <label></label> 
    <input> <img> 
    <strong></strong> 
    <em></em>
```

###body中的常用标签  

#####p和br标签  
p: 会自动在其前后创建一些空白。浏览器会自动添加这些空间，您也可以在样式表中规定。  
br: 换行
```
<p>p标签一般用在段落中,表示一个段落的开始和结束</p>
<p>br标签则是在<br/>语句中的<br/>任意<br/>位置换行</p>
```
> <p>p标签一般用在段落中,表示一个段落的开始和结束</p>
> <p>br标签则是在<br/>语句中的<br/>任意<br/>位置换行</p>

#####a标签  

相当于head中的link标签,但是会跳转页面而不是引用,主要作用有两个  

1. 定义超链接.最重要的属性是 href 属性，它指示链接的目标  

```
<a href="http://www.baidu.com" target="_blank">baidu</a>
```
> <a href="http://www.baidu.com" target="_blank">baidu</a>



2. 锚点,href跳转到页面中的对应#id处  

```
	<p>
    <a href="#C4">查看 Chapter 4。</a>
    </p>
    
    <h2>Chapter 1</h2>
    <p>This chapter explains ba bla bla</p>
    
    <h2>Chapter 2</h2>
    <p>This chapter explains ba bla bla</p>
    
    <h2>Chapter 3</h2>
    <p>This chapter explains ba bla bla</p>
    
    <h2><a name="C4">Chapter 4</a></h2>
    <p>This chapter explains ba bla bla</p>
```
> <p>
> <a href="#C4">查看 Chapter 4。</a>
> </p>
> <h2>Chapter 1</h2>
> <p>This chapter explains ba bla bla</p>
> <h2>Chapter 2</h2>
> <p>This chapter explains ba bla bla</p>
> <h2>Chapter 3</h2>
> <p>This chapter explains ba bla bla</p>
> <h2><a name="C4">Chapter 4</a></h2>
> <p>This chapter explains ba bla bla</p>

#####img标签  
相当于head中的link标签引用图片的功能,主要有两个属:src定义图片来源,title定义图片名称  
```
<img title="百度首页图" src="https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/bd_logo1_31bdc765.png" style="height: 50px;width: 50px"/>
```
> <img title="百度首页图" src="https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/bd_logo1_31bdc765.png" style="height: 50px;width: 50px"/>


#####h系列标签
标题从h1-h6从大到小.  
```
<h1>h1</h1>
<h2>h2</h2>
<h3>h3</h3>
...
<h6>h6</h6>
```
> <h1>h1</h1>
> <h2>h2</h2>
> <h3>h3</h3>
> ...
> <h6>h6</h6>


#####select系列标签
select 可创建单选或多选菜单。selected定义默认选项,size属性定义可见的内容长度,multiple定义是否多选,optgroup label选项分组,可以用value定义返回值.

单选:
```
<select size="1"> #单选
	    <option>北京</option>
	    <option>上海</option>
	    <option>广州</option>
	    <option selected="selected">成都</option> #默认
</select>
```
> <select size="1">
>    <option>北京</option>
>    <option>上海</option>
>    <option>广州</option>
>    <option selected="selected">成都</option>
> </select>


多选:
```
<select size="3" multiple="multiple"> #多选
	    <option>北京</option>
	    <option>上海</option>
	    <option>广州</option>
	    <option>成都</option>
</select>
```
> <select size="3" multiple="multiple">
>    <option>北京</option>
>    <option>上海</option>
>    <option>广州</option>
>    <option>成都</option>
> </select>


分组:
```
<select size="6"> #分组
	    <optgroup label="直辖市">
	        <option>北京</option>
	        <option>上海</option>
	    </optgroup>
	    <optgroup label="省会">
	        <option>成都</option>
	        <option>广州</option>
	    </optgroup>
</select>
```
> <select size="6">
>    <optgroup label="直辖市">
>        <option>北京</option>
>        <option>上海</option>
>    </optgroup>
>    <optgroup label="省会">
>        <option>成都</option>
>        <option>广州</option>
>    </optgroup>
> </select>




#####input系列标签


1. 复选框
checked 属性设置默认选中
```
<input type="checkbox" checked="checked" />
<input type="checkbox" />
```
> <input type="checkbox" checked="checked" />
> <input type="checkbox" />


2. 单选框:name属性相同时多个中只能选一个,value,checked

```
<p><input name="gender" type="radio" value="m"/></p>
<p><input name="gender" type="radio" value="f" /></p>
```
> <p><input name="gender" type="radio" value="m" checked="checked" /></p>
> <p><input name="gender" type="radio" value="f"/></p>


3. 文本输入框,value属性设置默认值

```
<input type="text" value="默认值"/>
```
> <input type="text" value="默认值"/>

```
<textarea>textarea</textarea>
```
> <textarea>textarea</textarea>


4. 密码框:隐藏输入的文本

```
<input type="password" />
```
> <input type="password" />

5. 文件选择框

> <input type="file" />


6. 提交按钮

button 只是一个按钮不会提交表单,需要绑定事件(所触发的行为).  
submit 提交表单按钮,触发后会默认提交表单(即使绑定了事件也会触发表单的提交) value按钮上的文字

```
<input type="button" value="btn" />
<input type="submit" value="提交"/>
```
<input type="button" value="btn" />
<input type="submit" value="提交"/>


#####form标签
标签用于为用户输入创建 HTML 表单,action规定当提交表单时向何处发送表单数据,method规定用于发送 form-data 的 HTTP 方法(get,post)。name属性,将数据以字典方式提交
```
<form action="http://127.0.0.1:8000/">
    <div>
        用户:<input name="user_name" type="text" />
    </div>
	<div>
        密码:<input name="password" type="password" />
    </div>
    <input type="submit" value="登录"/>
</form>
```

> <form action="http://127.0.0.1:8000/">
    <div>
        用户:<input name="user_name" type="text" />
    </div>
	<div>
        密码:<input name="password" type="password" />
    </div>
    <input type="submit" value="登录"/>
> </form>

![](http://7xread.com1.z0.glb.clouddn.com/02223d0c-8141-41d2-b972-68d8ecaaedea)


###label标签
点击文本跳转到对应选择框,使用id关联

```
<label for="lb01">婚否</label>
<input id="lb01" type="checkbox" />
```
<label for="lb01">婚否</label>
<input id="lb01" type="checkbox" />

###ul系列标签

```
        <ul>
            <li>无序</li>
            <li>无序</li>
            <li>无序</li>
        </ul>
        <ol>
            <li>有序</li>
            <li>有序</li>
            <li>有序</li>
        </ol>

        <dl>
            <dt>标题</dt>
            <dd>内容</dd>
            <dd>内容</dd>
            <dd>内容</dd>
        </dl>
```
> <ul>
    <li>无序</li>
    <li>无序</li>
    <li>无序</li>
</ul>
> <ol>
    <li>有序</li>
    <li>有序</li>
    <li>有序</li>
</ol>
> <dl>
    <dt>标题</dt>
    <dd>内容</dd>
    <dd>内容</dd>
    <dd>内容</dd>
</dl>


###tab系列标签
展示表格的标签,tr代表一行,th标题的列和td内容行表示列
colspan属性定义占用行方向多少格(占用多少列), rowspan列方向上占用多少格(占用多少行)

```
> <table border="1">
       <tr>
            <th>
                第一列
            </th>
            <th>
                第二列
            </th>
            <th>
                第三列
            </th>
        </tr>
        <tr>
            <td colspan="2">111,222</td>
            <td>333</td>
        </tr>
        <tr>
            <td rowspan="2">111,111</td>
            <td>222</td>
            <td>333</td>
        </tr>
        <tr>
            <td>222</td>
            <td>333</td>
        </tr>
</table>
```


> <table border="1">
        <tr>
            <th>
                第一列
            </th>
            <th>
                第二列
            </th>
            <th>
                第三列
            </th>
        </tr>
        <tr>
            <td colspan="2">111,222</td>
            <td>333</td>
        </tr>
        <tr>
            <td rowspan="2">111,111</td>
            <td>222</td>
            <td>333</td>
        </tr>
        <tr>
            <td>222</td>
            <td>333</td>
        </tr>
</table>

###fieldset系列标签
无什么用
```
<fieldset>
    <legend>登录</legend>
    <p>用户</p>
    <p>密码</p>
</fieldset>
```

> <fieldset>
    <legend>登录</legend>
    <p>用户</p>
    <p>密码</p>
</fieldset>

###html中的常用属性
所有的标签都可以定义的属性  
id,不提交的数据,一般用id,用于html代码关联.  
name,提交数据时用来标识数据,在input radio中有特殊作用  
value,一般为设置标签的默认文本,input radio中配合name提交数据  
style,定义css样式  
class,引用代码  



###html中的常用符号  

```
&lt;	<	小于号或显示标记
&gt;	>	大于号或显示标记
&amp;	&	可用于显示其它特殊字符
&quot;	“	引号
&reg;	®	已注册
&copy;	©	版权
&trade;	™	商标
&ensp;	 	半个空白位
&emsp;	 	一个空白位
&nbsp;		不断行的空白
```
符号代码大全: [点击](http://www.cnblogs.com/web-d/archive/2010/04/16/1713298.html)









