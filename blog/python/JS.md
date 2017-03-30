#JavaScript Dom入门

##JavaScript 
JavaScript 是属于 web 的语言，它适用于 PC、笔记本电脑、平板电脑和移动电话。
JavaScript 被设计为向 HTML 页面增加交互性。
许多 HTML 开发者都不是程序员，但是 JavaScript 却拥有非常简单的语法。几乎每个人都有能力将小的 JavaScript 片段添加到网页中。

中文文档: [点击](http://www.w3school.com.cn/js/index.asp)

#####书写规范

```
<!-- 方式一 -->
<script type"text/javascript" src="JS文件"></script>
 
<!-- 方式二 -->
<script type"text/javascript">
    Js代码内容
</script>
```


##HTML DOM
文档对象模型（Document Object Model，DOM）是一种用于HTML和XML文档的编程接口。它给文档提供了一种结构化的表示方法，可以改变文档的内容和呈现方式。我们最为关心的是，DOM把网页和脚本以及其他的编程语言联系了起来。DOM属于浏览器，而不是JavaScript语言规范里的规定的核心内容。  
中文文档: [点击](http://www.w3school.com.cn/htmldom/index.asp)

#####选择器
类似于CSS选择器,获取的为列表
```
document.getElementById('id'); 				通过标签的ID查找
document.getElementByClassName('class');	通过标签的class查找()
document.getElementsByName('name');			通过标签的name属性查找(某些标签才可以使用)
document.getElementsByTagName('tagname');	通过标签的标签名称查找
```



--------



#####事件
当事件发生时，可以执行 JavaScript，比如当用户点击一个 HTML 元素时。如需在用户点击某个元素时执行代码，请把 JavaScript 代码添加到 HTML 事件属性中：
onclick=JavaScript

```
<h5 onclick="this.innerHTML='hello!'">请点击这段文本!</h5> 
```
> <h5 onclick="this.innerHTML='hello!'">请点击这段文本!</h5> 

事件列表:
![](http://7xread.com1.z0.glb.clouddn.com/d5454b33-d335-42ac-9b4f-54c74df93b1e)



--------



#####改造默认标签
html中一些标签有绑定一些默认事件,可以通过下面方式改造

```
<a href="www.cnblogs.com" onclick="return Changetags();">本来应该跳转</a>
<script type="text/javascript">
	function Changetags(){
		alert('修改')
		return false   //改造后事件是按照自定义默认顺序执行,返回false就不会执行默认事件
	}
</script>
```
> <a href="www.cnblogs.com" onclick="return Changetags();">本来应该跳转</a>
<script type="text/javascript">
	function Changetags(){
		alert('修改')
		return false
	}
</script>



--------



#####增加html标签

```
<div id="container"></div>
<p onclick="Addtags();">添加</p>
<script type="text/javascript">
    function Addtags() {
        //生成一个a标签对象,并设置属性
        var createtags = document.createElement('a');
        createtags.innerText = '添加红字链接'
        createtags.style.color = 'red'
        createtags.href = 'http://www.cnblogs.com';
        //将对象加到container中
        var nid = document.getElementById('container')
        nid.appendChild(createtags)
        return false;
    }
</script>
```

> <div id="container"></div>
> <p onclick="Addtags();">添加</p>
<script type="text/javascript">
    function Addtags() {
        //生成一个a标签对象,并设置属性
        var createtags = document.createElement('a');
        createtags.innerText = '添加红字链接'
        createtags.style.color = 'red'
        createtags.href = 'http://www.cnblogs.com';
        //将对象加到container中
        var nid = document.getElementById('container')
        nid.appendChild(createtags)
        return false;
    }
</script>



--------


#####修改标签属性

```
<div id="dtest" style="width: 80px;font-size: 40px" >修改属性</div>

<script type="text/javascript">
    var nid = document.getElementById("dtest");
    nid.setAttribute('name','777');
    nid.setAttribute('value','777');
    nid.className = 'dtest'
    nid.style.color = 'white';
    nid.style.backgroundColor = 'red'
    nid.style.height = '100px';
    nid.style.backgroundSize = '100px';
    nid.style.fontSize = '12px';
    console.log(nid)
</script>
```
> <div id="dtest" style="width: 80px;font-size: 40px" >修改属性</div>
<script type="text/javascript">
    var nid = document.getElementById("dtest");
    nid.setAttribute('name','777');
    nid.setAttribute('value','777');
    nid.className = 'dtest'
    nid.style.color = 'white';
    nid.style.backgroundColor = 'red'
    nid.style.height = '100px';
    nid.style.backgroundSize = '100px';
    nid.style.fontSize = '12px';
    console.log(nid)
</script>

![](http://7xread.com1.z0.glb.clouddn.com/575142df-fddf-4842-9c6c-15260fa69f5a)



--------



#####内容获取和修改
innerText代表文本
innerHTML代表html
```
var obj = document.getElementById('nid')
obj.innerText                       # 获取文本内容
obj.innerText = "hello"             # 设置文本内容
obj.innerHTML                       # 获取HTML内容
obj.innerHTML = "<h1>asd</h1>"      # 设置HTML内容
```
- 通过id,class,标签获取和修改

```
<p id="test1">test</p>
<ul>
    <li>test1</li>
    <li>test2</li>
    <li>test3</li>
</ul>
<div class="test-class">test-class1</div>
<div class="test-class">test-class2</div>
<script type="text/javascript">
    var nid = document.getElementById('test1');
    console.log(nid.innerText);
    nid.innerText = '根据id修改里文本内容';
    var tags = document.getElementsByTagName('li'); //获取到文本列表
    for(var i=0; i<tags.length; i++ ){
        var item = tags[i];                         //遍历取得每一个元素
        console.log(item.innerText);                //在终端打印文本
        item.innerText = '修改li标签文本内容';       //修改页面内容
    }
    var tc = document.getElementsByClassName('test-class');
    for(var i=0; i<tc.length; i++){
        var item1 = tc[i];
        console.log(item1.innerText);
        item1.innerText = '根据class修改里文本内容';
    }
</script>
```
![](http://7xread.com1.z0.glb.clouddn.com/6c9f59e2-d75d-40a9-9eaf-4ed601002ee1)



--------



- 通过name获取特殊标签输入的值:input

```
<form>
    <p><input name="username" type="text" value="default" /></p>
    <p><input name="pwd" type="password" value="123456" /></p>
</form>
<script type="text/javascript">
    var uname = document.getElementsByName('username')[0];
    var passwd = document.getElementsByName('pwd')[0];
    console.log(uname.innerText, passwd.innerText, uname.value, passwd.value);
</script>
```
![](http://7xread.com1.z0.glb.clouddn.com/89fae477-9031-4d5c-a513-daabf6d13c49)
-
``` 
<h3><input type="button" onclick="GetValue();" value="点击"/>触发获取输入内容</h3>
<input id="i1" type="text" />
<script type="text/javascript">
    function GetValue() {
        var obj = document.getElementById('i1')
        alert(obj.value)
        obj.value = ''
    }
</script>
```
<h3><input type="button" onclick="GetValue();" value="点击"/>触发获取输入内容</h3>
<input id="i1" type="text" />
<script type="text/javascript">
    function GetValue() {
        var obj = document.getElementById('i1')
        alert(obj.value)
        obj.value = ''
    }
</script>



--------



- innerHTML:上面两种都只能获取标签内的文本,innerHTML可以获取html源码,包括特殊符号

```
<div id="d1">
    div框       空格
    <h5>h5标签</h5>
</div>
<script type="text/javascript">
    var nid = document.getElementById('d1');
    console.log(nid.innerText)
    console.log(nid.innerHTML)
</script>
```
![](http://7xread.com1.z0.glb.clouddn.com/74aaca91-adc7-464d-89ed-1dce94292141)



--------



- select,textarea获取选中或者输入 

```
<h3><input type="button" onclick="GetValue();" value="点击"/>触发获取输入内容</h3>
<textarea id="ta1">将getvalue函数getid改为ta1</textarea>
<select id="s1">
    <option value="1">北京</option>
    <option value="2">上海</option>
    <option value="3">广州</option>
</select>

<script type="text/javascript">
    function GetValue() {
        var obj = document.getElementById('s1')
        alert(obj.value)
        obj.value = '2'
    }
</script>
```

> <h3><input type="button" onclick="GetValue();" value="点击"/>触发获取输入内容</h3>
<textarea id="ta1">将getvalue函数getid改为ta1</textarea>
<select id="s1">
    <option value="1">北京</option>
    <option value="2">上海</option>
    <option value="3">广州</option>
</select>
<script type="text/javascript">
    function GetValue() {
        var obj = document.getElementById('s1')
        alert(obj.value)
        obj.value = '2'
    }
</script>



--------


#####其他功能
1. console.log(): 在客户端console打印
2. alert(): 在客户端弹出窗口
3. confirm(): 类似alert也弹出窗口并给返回值

```
<input type="button" value="鼠标指到" onmouseover="MyConfirm();"/>
<script type="application/javascript">
    function MyConfirm() {
        var ret = confirm('confirm');
        console.log(ret)
    }
</script>
```
<input type="button" value="鼠标指到" onmouseover="MyConfirm();"/>
<script type="application/javascript">
    function MyConfirm() {
        var ret = confirm('confirm');
        console.log(ret)
    }
</script>

4.url跳转和刷新
location.href和location.reload,还没弄明白过两天再研究

5.定时器
```
setInterval('alert()', 2000): 循环执行
clearInterval(obj): 停止
setTimeout('alert()', 2000): 只在指定时间执行一次
clearTImeout(): 停止
```
```
<div>
    <p id="pmd">这是一个跑马灯!</p>
    <input type="button" value="停止跑马灯" onclick="stopPmd();"/>
</div>
<script type='text/javascript'>
    stopobj = setInterval('Go()',1000);
    function stopPmd() {
        clearInterval(stopobj)
    }
    function Go(){
        /* title的跑马灯
        var content = document.title;
        var firstChar = content.charAt(0);
        var sub = content.substring(1,content.length);
        document.title = sub + firstChar;
         */
        var content = document.getElementById('pmd').innerText;
        var firstChar = content[0];
        var sub = content.substring(1,content.length);
        document.getElementById('pmd').innerText = sub + firstChar;
    }
</script>
```
> <div>
    <p id="pmd">这是一个跑马灯!</p>
    <input type="button" value="停止跑马灯" onclick="stopPmd();"/>
</div>
<script type='text/javascript'>
    stopobj = setInterval('Go()',1000);
    function stopPmd() {
        clearInterval(stopobj)
    }
    function Go(){
        /* title的跑马灯
        var content = document.title;
        var firstChar = content.charAt(0);
        var sub = content.substring(1,content.length);
        document.title = sub + firstChar;
         */
        var content = document.getElementById('pmd').innerText;
        var firstChar = content[0];
        var sub = content.substring(1,content.length);
        document.getElementById('pmd').innerText = sub + firstChar;
    }
</script>




#####DOM小例

- 数字自增按钮

```
<div>
    <div id="num">1</div>
    <input type="button" value="关注" onclick="Add();" /> //触发一个事件
</div>
<script type="text/javascript">
    function Add(){
        //alert(关注成功); 								//alert在用户页面弹出窗口
        var nid = document.getElementById('num');		//选择
        var text = nid.innerText;						//获取内容和修改
        text = parseInt(text);
        text += 1;
        nid.innerText = text;
    }
</script>
```

><div>
    <div id="num">1</div>
    <input type="button" value="关注" onclick="Add();" />
</div>
<script type="text/javascript">
    function Add(){
        //alert(关注成功);
        var nid = document.getElementById('num');
        var text = nid.innerText;
        text = parseInt(text);
        text += 1;
        nid.innerText = text;
    }
</script>





- 搜索框

```
<input type="text" id="search" value="请输入关键字" onfocus="Focus();" onblur="Blur();"/>

<script type="text/javascript">
    function Focus() {
        var nid = document.getElementById('search')
        var value = nid.value;
        if(value == "请输入关键字"){
            nid.value = "";
        }
    }
    function Blur() {
        var nid = document.getElementById('search')
        var value = nid.value;
        if(!value.trim()){
           nid.value = "请输入关键字"
        }
    }
</script>
```



--------



- 改造标签提交表单

```
//改造后任何标签都可以提交
<form id="f1" action="https://www.sogou.com/web" method="get">
    <input name="query" type="text"/>
    //<input type="submit" value="提交" />  //html提交方式
    <div onclick="Submit();">提交</div>
</form>
<script type="text/javascript">
    function Submit() {
        var nid = document.getElementById('f1');
        nid.submit();    
    }
</script> 
```
> <form id="f1" action="https://www.sogou.com/web" method="get">
    <input name="query" type="text"/>
    <div onclick="Submit();">提交</div>
</form>
<script type="text/javascript">
    function Submit() {
        var nid = document.getElementById('f1');
        nid.submit();
    }
</script>



--------

- 表单检查

```
<form id="f1" action="https://www.sogou.com/web" method="get">
    <input name="query" type="text"/>
    <input type="submit" value="提交" onclick="return MySubmit();"/>
</form>
<script type="application/javascript">
    function MySubmit() {
        var q = document.getElementsByName('query')[0]; //q 是一个列表
        if(q.value.trim()){   //检查q是否为空
            return true  //检查为真就返回true
        }
        else{
            alert('retry')  //不成功就提醒
            return false
        }
    }
</script>
```
> <form id="f1" action="https://www.sogou.com/web" method="get">
    <input name="query" type="text"/>
    <input type="submit" value="提交" onclick="return MySubmit();"/>
</form>
<script type="application/javascript">
    function MySubmit() {
        var q = document.getElementsByName('query')[0]; //q 是一个列表
        if(q.value.trim()){   //检查q是否为空
            return true  //检查为真就返回true
        }
        else{
            alert('retry')  //不成功就提醒
            return false
        }
    }
</script>





##jQuery
jQuery 是一个 JavaScript 库。jQuery 极大地简化了 JavaScript 编程。jQuery 很容易学习。  
中文文档: [点击](http://www.w3school.com.cn/jquery/index.asp)
在实际使用中大多数是使用jQuery或者是bootstrap另外开一篇入门
