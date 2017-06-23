
# 学习笔记

## 第三课 子进程调用call

ret = subprocess.call("ping 192.168.31.97", shell=True, stdout=f, stderr=subprocess.STDOUT)

-------------------------------

subprocess模块用来生成子进程，并可以通过管道连接它们的输入/输出/错误，以及获得它们的返回值。

### subprocess.call
语法:
     `subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False)`
语义:
     运行由args指定的命令，直到命令结束后，返回 返回码的属性值。

上面的参数是最常见的方式，下面是示例代码:

```python
>>>
>>> subprocess.call(["ls", "-l"])
0
>>> subprocess.call("exit 1", shell=True)
1
```

WARNING: 使用 shell=True 是一种安全保护机制。

NOTE: 在使用这个函数时，不要使用 stdout=PIPE 或 stderr=PIPE 参数，
      不然会导致子进程输出的死锁。
      如果要使用管道，可以在 communicate()方法中使用Popen

示例代码:
```python
import subprocess
rc = subprocess.call(["ls","-l"])
```

可以通过一个shell来解释一整个字符串:
```python
import subprocess
out = subprocess.call("ls -l", shell=True)
out = subprocess.call("cd ..", shell=True)
```

使用了shell=True这个参数。

这个时候，我们使用一整个字符串，而不是一个表来运行子进程。

Python将先运行一个shell，再用这个shell来解释这整个字符串。

shell命令中有一些是shell的内建命令，这些命令必须通过shell运行，$cd。

shell=True允许我们运行这样一些命令。

> shell=True使用字符串来表示命令，否则使用列表list来表示命令

## 第二课 子进程打开Popen

for server in open('server_list.txt'):
	subprocess.Popen(('nslookup '+server))

> 子进程Popen进行的系统调用，可与应用进行交互。而子进程call进行的系统调用，只是让应用跑起来，没有交互。
> 所以，Popen比call来的高级一点。

popen()函数通过创建一个管道，调用fork()产生一个子进程，执行一个shell以运行命令来开启一个进程。
这个管道必须由pclose()函数关闭，而不是fclose()函数。pclose()函数关闭标准I/O流，等待命令执行结束，然后返回shell的终止状态。
如果shell不能被执行，则pclose()返回的终止状态与shell已执行exit一样。

Nslookup是一个检测网络中DNS服务器能否正确实现域名解析的命令行工具。

## 第一课 与系统交互OS和os.path

```python
if not os.path.exists('testdir'):
  os.makedirs('testdir')
```

> 程序中实现系统shell的命令调用。（新建目录）


----------------------------------------------------

### os与sys两模块的区别

os 这个模块提供了一种方便的使用操作系统函数的方法。

sys 这个模块可供访问由解释器使用或维护的变量和与解释器进行交互的函数。

**os模块负责程序与操作系统的交互，提供了访问操作系统底层的接口;
sys模块负责程序与Python解释器的交互，提供了一系列的函数和变量，用于操控python的运行时环境。**
