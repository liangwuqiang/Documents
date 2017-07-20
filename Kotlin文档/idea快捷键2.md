http://www.cnblogs.com/yjm-yang/p/4868623.html


# Intelli IDEA快捷键(配合IdeaVim)

Intelli IDEA开发环境，个人总结的一些常用的快捷键。

想要使用vim方式编辑代码，可以使用Intelli IDEA的IdeaVim。IdeaVim插件功能很强大，在vim编辑模式下还可以使用IDEA的一些代码提示功能，我把vim模式和IDE模式切换键换成了CTRL+ALT+;，默认切换键是CTRL+ALT+v，但这个键和IDE其他热键冲突，所以需要修改，我修改为CTRL+ALT+;。

## 自动提示：

CTRL+space：通常我们敲代码时IDEA会自动出现提示，如果提示被中断了可以使用CTRL+space，提示会再次出现

CTRL+SHIFT+space：智能自动提示，会更加类型匹配智能提示

## 自动补全：

当出现自动提示时选择合适代码然后回车即可自动补全

CTRL+SHIFT+ENTER，当我们敲入if、else、for、while等关键字时然后按CTRL+SHIFT+ENTER就会自动补后面的（）{}

 

## 代码自动生成：

ALT+insert：自动生成类的一些方法（构造函数、getter、seter、equals、hashCode等），当定位到目录上时可以用来创建文件

ALT+ENTER：类似Eclipse的快速修复（quick fix）、导入包、实现接口方法，这个很好用

postfix completion功能，想要输入for(People people: peoples){}，只需输入peoples.for+tab即可，还有其他类似的功能

psvm+TAB：自动生成main函数

sout+TAB：自动生成System.out.println()代码

soutm+TAB：自动打印当前类名和方法名

soutp+TAB：自动打印变量名和变量值　　System.out.println("args = [" + args + "]");

soutv+TAB：自动打印变量名和变量值　　System.out.println("args = " + args);

 

## 编辑：

我比较喜欢配合vim做输入和编辑，vim的一些操作就不介绍了，下面是一些IDE常用的编辑方式

CTRL+W：选中文本，扩充选中，类似于vim中的vi+action和va+action

SHIFT+F6：重命名

CTRL+SHIFT+上下箭头：上下移动代码块

CTRL+/：生成注释，个人比较喜欢使用vim的block visual模式插入注释

 

## 重构：

CTRL+SHIFT+ALT+T：Refactor this：重构一切

SHIFT+F6：重命名

CTRL+ALT+m：方法抽取，选中代码，按ATRL+ALT+m对选中的代码块抽取成一个函数

CTRL+ALT+n：方法内联，对一个函数进行方法内联，即代码替换函数

CTRL+ALT+v：引入局部变量

CTRL+ALT+p：引入参数

CTRL+ALT+f：引入类变量

CTRL+ALT+c：引入类常量

 

## 查找：

/：当前文件中vim正向查找，n继续查找下一个，N继续反向查找下一个

?：当前文件中vim反向查找，n继续查找下一个，N继续反向查找下一个

CTRL+f：当前文件中IDE的查找，F3继续查找下一个，SHIFT+F3继续反向查找下一个

CTRL+r：替换查找，也可以使用vim的替换功能：全文替换%s/org/changed/g

CTRL+F12：当前文件中查找方法

CTRL+N：查找类，支持按大写字母缩略查找

CTRL+SHIFT+N：查找文件，支持按大写字母缩略查找

ALT+F7：查找所有被引用处

CTRL+SHIFT+F：全局查找，另外SHIFT+SHIFT也可以全局搜索

 

## 跳转：

CTRL+B：跳转到光标所在位置类或方法或变量的声明处，然后想回来时可用CTRL+TAB

CTRL+ALT+B：跳到实现处

ALT+上下箭头：跳转到当前文件上一个/下一个方法

CTRL+SHIFT+H：显示方法层次结构

CTRL+Q：显示类/方法说明

 

## 窗口：

ALT+<--/-->：在编辑窗口中左右切换，如果左右的几个工作窗口不见了试试ALT+1/2/3

CTRL+TAB：在当前编辑窗口和上一个编辑窗口切换，按下CTRL+TAB然后CTRL键不放可以通过方向键选择具体哪个编辑窗口

CTRL+SHIFT+F12：全屏/退出全屏

ALT+F12：调出/关闭终端窗口

ALT+1：调出/关闭左侧工程栏窗口

ALT+8：调出/关闭右侧窗口

ALT+4：调出/关闭下侧运行结果窗口

大写ZZ：关闭当前编辑窗口

## 调试运行：

ALT+SHIFT+F10：运行

ALT+SHIFT+F9：调试

F7：单步进入

F8：单步跳过

F9：跳过

 

## 其他：

CTRL+SHIFT+T：生成测试用例

CTRL+ALT+O：整理import，自动导入

CTRL+SHIFT+F7：高亮显示

ALT+F1：在左侧工程栏中定位到当前编辑文件，然后可以使用SHIFT+F6或者CTRL+SHIFT+ALT+T重命名等操作

CTRL+SHIFT+A：调出显示其他命令的框框

 

vim的系统剪切板 * +，系统剪切板粘贴到编辑器*p、+p；复制编辑器内容到系统剪切板（选择内容）*y、+y;

参考网址：http://blog.csdn.net/dc_726/article/details/42784275
