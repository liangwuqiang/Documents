shutter使用gnome-web-photo可截取整个网页，png格式

## 安装

sudo apt install -y shutter gnome-web-photo



----------------------------------------------


https://linux.cn/article-3140-1.html

http://www.linuxidc.com/Linux/2014-07/104820.htm


在 Ubuntu 和 Debian 的分支下：

    $ sudo apt-get install gnome-web-photo

要为一个网页截图：

    $ gnome-web-photo -t 0 --mode=photo http://www.unixmen.com output.png

上面这条命令将为 Unixmen 的主页截取一个完整长度的截图，并保存在当前工作目录下。

-t 这个参数可以设置生成截图的超时时间。-t 0 则表示禁用超时参数。

通过 gnome-web-photo，你可以用下面的命令为一个网页生成一个缩略图：（默认大小是 256×256，但是可以通过 “-s” 来指定缩略图的大小）

    $ gnome-web-photo -t 0 -s 128 --mode=thumbnail http://www.unixmen.com output.png


如果你想将网页截取成一个可供打印的多页 PDF 文档，你可以输入下面的命令：

    $ gnome-web-photo -t 0 --mode=print http://www.unixmen.com output.pdf

注意这个应用并不支持 .jpg 格式。

