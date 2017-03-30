##bootstrap

说了这么多,其实就是因为一直看不懂,玩不来bootstrap.所以从头学习了一下html到jquery.能看懂javascript和html可以理解了.

中文网站: [点击](http://www.bootcss.com/)
#jQuery 入门

##jQuery
是一个 JavaScript 函数库。jQuery 库包含以下特性：
HTML 元素选取  
HTML 元素操作  
CSS 操作  
HTML 事件函数  
JavaScript 特效和动画  
HTML DOM 遍历和修改  
AJAX  
Utilities  

官网: [点击](http://jquery.com/)  
中文文档: [点击](http://www.php100.com/manual/jquery/)  
##书写规范
```
<script src="https://code.jquery.com/jquery-2.2.4.min.js"></script>
					 //代码不能写在引用文件这个容器里
<script>
	$somecode   	 //$符号就表示jQuery
	jQuery.somecode  //等同
</script>
```

>>PS:由于编辑器的JS编码问题中文在js编码过程中没有使用utf-8.显示乱码.实际代码和注释源码有区别

##选择器和筛选器
类似JS有#id(id选择器),element(元素选择器即标签),class(class选择器),组合选择器(selector多种选择器组合),层级选择器,*(选择全部)... 

#####基本选择器
在js基础上稍微修改了一下,是用#代表id, .class代表class,标签直接使用标签名

>>PS:id选择器,使用任何的元字符（如 !"#$%&'()*+,./:;<=>?@[\]^`{|}~）作为名称的文本部分， 它必须被两个反斜杠转义：\\。 参见示例。

```
<div id="testid"></div>
<div class="testclass"></div>
<p></p>
<script   src="https://code.jquery.com/jquery-2.2.4.min.js"   integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44="   crossorigin="anonymous" charset="utf-8"></script>
<script>
        $('#testid').text('#testid相当于js: docment.getElementById("testid")')
        $('p').text('p相当于js: document.getElementsByTagName("p")')
        $('.testclass').text('.testclass相当于js: document.getElementByClassName("testclass")')
```
> <div id="testid"></div>
> <div class="testclass"></div>
> <p></p>
<script   src="https://code.jquery.com/jquery-2.2.4.min.js"   integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44="   crossorigin="anonymous" charset="utf-8" language="JavaScript" type="text/javascript"></script>
<script>
        $('#testid').text('#testid like js: docment.getElementById("testid")')
        //$('p').text('p 相当于 js: document.getElementsByTagName("p")')
        //修改p标签造成编辑器所有p标签被修改这里注释
        $('.testclass').text('.testclass like js: document.getElementByClassName("testclass")')
</script>    

--------

#####组合选择器
类似js定义

```
<div id="testid1"></div>
<div class="testclass1"></div>
<script>
$('#testid1, .testclass1').text('逗号隔开元素组合选择器')
</script>
```
> <div id="testid1"></div>
> <div class="testclass1"></div>
> <script>
$('#testid1, .testclass1').text('Selected')
</script>


#####层级选择器
和JS一样通过空格隔开选择器表达层级路径

```
<form>
  <p>原始</p>
  <div id="test">
      <p>原始</p>
 </div>
</form>
<p >原始</p>
<script>
$('form #test p').text('层级选中')
</script>
```
> <form>
  <p>原始</p>
  <div id="test">
      <p></p>
 </div>
</form>
<p >原始</p>
<script>
$('form #test p').text('Selected')
</script>

#####筛选器

first选择匹配到的第一个

```
<li>list item 1</li>
<ul>
    <li>list item 1</li>
    <li>list item 2</li>
    <li>list item 3</li>
    <li>list item 4</li>
    <li>list item 5</li>
</ul>
<script>
$('ul li').first().text('first')
</script>
```
><li>list item 1</li>
<ul>
    <li>list item 1</li>
    <li id=>list item 2</li>
    <li>list item 3</li>
    <li>list item 4</li>
    <li>list item 5</li>
</ul>
<script>
$('ul li').first().text('first')
</script>



##属性选择器

#####attr设置或返回被选元素的属性值。

```
<div id="testattr">testattr</div>
<script>
$('#testattr').attr('name','test')
</script>
```
![](http://7xread.com1.z0.glb.clouddn.com/fe249a58-88a2-47af-9532-f94f441f40ab)

#####removeAttr从每一个匹配的元素中删除一个属性

```
<div id="rmattr" name="test">rmattr</div>
<script>
$('#rmattr').removeAttr('name')
</script>
```
![](http://7xread.com1.z0.glb.clouddn.com/21eae5e1-7871-4a19-bfe7-a40f65957dec)


#####html和text
js中的innerHtml和innerText

```
<p id="testtext">testtext</p>
<p id="testhtml">testhtml</p>
<script>
    $('#testtext').text('changed')
    $('#testhtml').html('test<br>html')
</script>
```
> <p id="testtext">testtext</p>
<p id="testhtml">testhtml</p>
<script>
    $('#testtext').text('changed')
    $('#testhtml').html('test<br>html')
</script>


#####val

```
<input type="text" id="testval">testval</input>
<script>
    //$('input:text').val('hello')
    $('#testval').val('world')
</script>
```
> <input type="text" id="testval">testval</input>
<script>
    //$('input:text').val('hello')
    $('#testval').val('world')
</script>


#####CSS

```
<div id="testcss">testcss</div>
<script>
	//$('#testcss').height(20)
    //$('#testcss').width(20)
    $('#testcss').css
    ({"color":"white","background":"blue","height":"80px", "width":"80px"})
</script>
```
> <div id="testcss">testcss</div>
<script>
    $('#testcss').css({"color":"white","background":"blue","height":"80px", "width":"80px"})
</script>

>>jQuery还有很多选择器.慢慢看文档吧..很简单,把很多JS复杂的查找封装了很多易用方法,包括筛选器,属性也是类似的方法.

#####事件和文档处理
不是专业做前端的话,东西看起来还是有点多,慢慢看吧,都是这么玩的.

##jQuery小例

1. 菜单切换

```
<style>
        .tab-box{
            height: 300px;
            width: 300px;
        }
        .tab-box a {
            border-right: 2px;
            padding: 8px;
        }
        .tab-box .box-menu{
            line-height: 33px;
            background-color: #dddddd;
            border: 1px solid #dddddd;
        }
        .tab-box .box-body{
            border: 1px solid;
            background-color: white;
        }
        .hide{
            display: none;
        }
        .current{
            background-color: white;
            color: black;
            border-top:2px solid red;
        }
</style>
<div class="tab-box">
    <div class="box-menu">
        <a menu-val="1" onclick="ChangeMenu(this);" class="current">菜单一</a>
        <a menu-val="2" onclick="ChangeMenu(this);">菜单二</a>
        <a menu-val="3" onclick="ChangeMenu(this);">菜单三</a>
    </div>
    <div class="box-body">
        <div id="content1">内容一</div>
        <div id="content2" class="hide">内容二</div>
        <div id="content3" class="hide">内容三</div>
    </div>
</div>
<script>
    function ChangeMenu(ths) {
        $(ths).addClass('current').siblings().removeClass('current');
        //找到当前点击的标签,加上选中样式
        var contentId = $(ths).attr('menu-val');
        //获取当前标签的mene-val
        var tmp = '#content' + contentId;
        $(tmp).removeClass('hide').siblings().addClass('hide');
        //将对应标签menu-val对应的内容标签移除hide属性,给其他没有选中的内容添加hide
        //console.log($('.tab-box').html())
    }
</script>
```
> <style>
        .tab-box{
            height: 300px;
            width: 300px;
        }
        .tab-box a {
            border-right: 2px;
            padding: 8px;
        }
        .tab-box .box-menu{
            line-height: 33px;
            background-color: #dddddd;
            border: 1px solid #dddddd;
        }
        .tab-box .box-body{
            border: 1px solid;
            background-color: white;
        }
        .hide{
            display: none;
        }
        .current{
            background-color: white;
            color: black;
            border-top:2px solid red;
        }
</style>
<div class="tab-box">
    <div class="box-menu">
        <a menu-val="1" onclick="ChangeMenu(this);" class="current">菜单一</a>
        <a menu-val="2" onclick="ChangeMenu(this);">菜单二</a>
        <a menu-val="3" onclick="ChangeMenu(this);">菜单三</a>
    </div>
    <div class="box-body">
        <div id="content1">内容一</div>
        <div id="content2" class="hide">内容二</div>
        <div id="content3" class="hide">内容三</div>
    </div>
</div>
<script>
    function ChangeMenu(ths) {
        $(ths).addClass('current').siblings().removeClass('current');
        //找到当前点击的标签,加上选中样式
        var contentId = $(ths).attr('menu-val');
        //获取当前标签的mene-val
        var tmp = '#content' + contentId;
        $(tmp).removeClass('hide').siblings().addClass('hide');
        //将对应标签menu-val对应的内容标签移除hide属性,给其他没有选中的内容添加hide
        //console.log($('.tab-box').html())
    }
</script>


2. 循环each方法使用,全选,反选,取消


```
<div>
    <input type="button" value="全选" onclick="SelectAll();" />
    <input type="button" value="反选" onclick="ReverseAll();" />
    <input type="button" value="取消" onclick="ClearAll();" />
</div>
<div>
    <table border="1">
        <tr>
            <td><input type="checkbox"></td>
            <td>123</td>
            <td>123</td>
        </tr>
        <tr>
            <td><input type="checkbox"></td>
            <td>123</td>
            <td>123</td>
        </tr>
        <tr>
            <td><input type="checkbox"></td>
            <td>123</td>
            <td>123</td>
        </tr>
    </table>
</div>
<script>
    function SelectAll() {
    	//全选: 获得$('table :checkbox')全部将checked属性改为true
        $('table :checkbox').prop('checked', true);
    }
    function ClearAll() {
    	//取消: 获得$('table :checkbox')全部将checked属性改为false
        $('table :checkbox').prop('checked', false);
    }
    function ReverseAll() {
		// $('table :checkbox')获得所有table :checkbox列表
		//jQuery封装了for循环each(callback),这里会把每个元素传入each(里的function(){}执行)
        $('table :checkbox').each(function () {
            var isChecked =  $(this).prop('checked');
        	//$this在循环内获得当前元素    
            if(isChecked){
                $(this).prop('checked', false);
            }else {
                $(this).prop('checked', true);
            }
        })
//JS原本写法        
//        var checkboxList = $('table :checkbox');
//        for(var i in checkboxList){
//            var ele = checkboxList[i];
//            var isChecked = $(ele).prop('checked');
//            if(isChecked){
//                $(ele).prop('checked', false)
//            }else {
//                $(ele).prop('checked', true)
//            }
//        }
    }
</script>
```
><div>
    <input type="button" value="全选" onclick="SelectAll();" />
    <input type="button" value="反选" onclick="ReverseAll();" />
    <input type="button" value="取消" onclick="ClearAll();" />
</div>
<div>
    <table border="1">
        <tr>
            <td><input type="checkbox"></td>
            <td>123</td>
            <td>123</td>
        </tr>
        <tr>
            <td><input type="checkbox"></td>
            <td>123</td>
            <td>123</td>
        </tr>
        <tr>
            <td><input type="checkbox"></td>
            <td>123</td>
            <td>123</td>
        </tr>
    </table>
</div>
<script>
    function SelectAll() {
        $('table :checkbox').prop('checked', true);
    }
    function ClearAll() {
        $('table :checkbox').prop('checked', false);
    }
    function ReverseAll() {
        $('table :checkbox').each(function () {
            var isChecked =  $(this).prop('checked');
            if(isChecked){
                $(this).prop('checked', false);
            }else {
                $(this).prop('checked', true);
            }
        })
    }
</script>

>>PS: each也可以处理字典,each()还有一个书写方式,
>>```
var testList = [11,22,33,44];
$.each(userList, function(i,item){ //i,item分别对应userList列表的index和值
	some code;
})
> ```


#####返回顶部

```
<style>
    .go-top{
        background-color: blue;
        color: white;
        position: fixed;
        right: 0;
        bottom:0;
        width: 60px;
        border: 2px solid #2728ff;
        line-height: 10px;
        text-align: center;
        cursor: pointer;
    }
    .hide{
        display: none;
    }
</style>
<div class="go-top hide">
    <a onclick="GoTop();">返回顶部</a>
</div>
<script>
    window.onscroll = function () {
        var currentTop = $(window).scrollTop()
        if(currentTop > 100){
            $('.go-top').removeClass('hide')
        }else {
            $('.go-top').addClass('hide')
        }
    }
    function GoTop() {
        $(window).scrollTop(0)
    }
</script>
```


> <style>
    .go-top{
        background-color: blue;
        color: white;
        position: fixed;
        right: 0;
        bottom:0;
        width: 60px;
        border: 2px solid #2728ff;
        line-height: 10px;
        text-align: center;
        cursor: pointer;
    }
    .hide{
        display: none;
    }
</style>
<div class="go-top hide">
    <a onclick="GoTop();">返回顶部</a>
</div>
<script>
    window.onscroll = function () {
        var currentTop = $(window).scrollTop()
        if(currentTop > 100){
            $('.go-top').removeClass('hide')
        }else {
            $('.go-top').addClass('hide')
        }
    }
    function GoTop() {
        $(window).scrollTop(0)
    }
</script>


#####可移动pannal

```
<div style="border: 1px solid #ddd;width: 600px;position: absolute;">
    <div id="title" style="background-color: black;height: 40px;color: white;">
        标题
    </div>
    <div style="height: 300px;">
        内容
    </div>
</div>
<script>
    $(function(){
        // 页面加载完成之后自动执行$(function(){}) $(document).ready(function(){})
        $('#title').mouseover(function(){
            $(this).css('cursor','move');
        }).mousedown(function(e){
            var _event = e || window.event;
            //有些浏览器支持e,有些浏览器不支持e,就使用window.eventhuoqu鼠标位置
            var ord_x = _event.clientX;
            var ord_y = _event.clientY;
            //获取当前鼠标,
            var parent_left = $(this).parent().offset().left;
            var parent_top = $(this).parent().offset().top;
            //this为当前标签,获取标签的位置
            $(this).bind('mousemove', function(e){
            //给鼠标绑定事件
                var _new_event = e || window.event;
                var new_x = _new_event.clientX;
                var new_y = _new_event.clientY;
                //获取新的位置
                var x = parent_left + (new_x - ord_x);
                var y = parent_top + (new_y - ord_y);
                //获取偏移量
                $(this).parent().css('left',x+'px');
                $(this).parent().css('top',y+'px');
                //将当前标签位置加上偏移量
            })
        }).mouseup(function(){
            $(this).unbind('mousemove');
        });
    })
```

