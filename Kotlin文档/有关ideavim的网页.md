# 定制 Jetbrains vim 插件：ideavim 

http://blog.csdn.net/simple_the_best/article/details/53132943


# vim 配置文件语法 

http://blog.csdn.net/trochiluses/article/details/21776365

vimrc脚本的注释是使用引号(")作行注释。

(1) 标量变量
可以是数字或字符串，基本与perl相同。
命名方式为：作用域:变量名，常用的有如下几种：
b:name —— 只对当前buffer有效的变量
w:name —— 只对当前窗口有效的变量
g:name —— 全局变量
v:name —— vim预定义变量
a:name —— 函数的参变量
注意：引用标量变量的时候请包含作用域和冒号

# gVim 和 Sublime Text Vintage 模式中英文输入法切换麻烦的解决思路

https://www.v2ex.com/t/158804



" 普通模式：关闭输入法

function! Fcitx2en()
    let s:input_status = system("fcitx-remote")
    if  s:input_status == 2
        let l:a = system("fcitx-remote -c")
    endif
endfunction

" 退出插入模式
autocmd InsertLeave * call Fcitx2en()
" 自动命令 事件

## 没有实现这个功能
