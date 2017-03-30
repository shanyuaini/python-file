
//alert('from: js-file');

/*
变量声明 用var 表示局部变量
window.name = 'sylar'   全局变量
var name = 'tom'  局部变量一定要加var
*/

//函数申明
Foo('sylar')
Bar()

name = 'tom'
function Foo(name){
    //var arg2 = arguments[1]  //设置默认参数
    var name = 'jerry'
    console.log(name);       //在浏览器控制台打印
   // console.log(arg2);
}


function Bar(){
    console.log(name)
    return 9
}