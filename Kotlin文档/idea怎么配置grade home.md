idea怎么配置grade home？

首先，先download最新版本的gradle，网址如下：

然后将下载下来的zip包放在你要安装的路径上，我安装在
/usr/local/bin；
然后打开电脑上的.bash_profile文件，输入以下命令：

GRADLE_HOME=/usr/local/bin/gradle-1.8;
export GRADLE_HOME
export PATH=$PATH:$GRADLE_HOME/bin

然后再在console上输入以下命令：
source ~/.bash_profile

这样就安装成功啦，可以通过以下命令来查看是否安装成功。
gradle -version

如果提示没有gradle命令，则有可能是：
1. GRADLE_HOME路径可能不对；
2. 没有执行source ~/.bash_profile
