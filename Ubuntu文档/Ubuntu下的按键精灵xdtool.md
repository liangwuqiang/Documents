# xdtool安装

sudo apt-get install xdotool

软件首页：http://www.semicomplete.com/projects/xdotool/

# 基本用法：

xdotool mousemove x y

将鼠标移动到在屏幕上特定的X和Y坐标位置

xdotool click 1

点击鼠标左键，1表示左键，2表示中键，3表示右键。

xdotool key ctrl+l

同时按下ctrl和l键

# 更多命令详解请输入：man xdotool

这个工具没有内置延时和循环功能。不过linux下提倡的就是一个软件做一件事，这个功能只要稍微组合一下就能实现了。

举个例子：

如果要鼠标每隔10秒点击左键一次

我们可以用终端下的watch命令组合实现

watch -n 10 xdotool click 1

--------------------------------------------------------

这是我在ST写的用来自动打开机顶盒的脚本

#!/bin/bash

init_stb() {
    xdotool type "telnet 10.80.117.$1"
    xdotool key Return
    sleep 1
    xdotool type "root"
    xdotool key Return
    sleep 1
    xdotool type "cd app0"
    xdotool key Return
    sleep 1
    xdotool type "ifconfig eth0 mtu 1500"
    xdotool key Return
    xdotool type "date"
    xdotool key Return
    sleep 1
    xdotool type "date -s "
    xdotool click 2
    xdotool key Return
    sleep 1
    xdotool type "cd /app0/conf_files/"
    xdotool key Return
    sleep 1
    xdotool type "sh runedva.sh"
    xdotool key Return
}

xdotool key ctrl+shift+t
xdotool type "date +%m%d%H%M%Y > currenttime12345"
xdotool key Return
xdotool type "xclip -i currenttime12345"
xdotool key Return
xdotool type "rm -f currenttime12345"
xdotool key Return

if [ "$1" == "" ]; then
    init_stb 36
    xdotool key ctrl+shift+t
    init_stb 37
else
    init_stb $1
fi
