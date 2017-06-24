-------------------------------------------------
Git SSH Key 生成步骤

# git config --global user.name liangwuqiang

# git config --global user.email l_wuqiang@126.com

查看是否已经有了ssh密钥：cd ~/.ssh

# $ ssh-keygen -t rsa -C l_wuqiang@126.com
按3个回车，密码为空。
最后得到了两个文件：id_rsa和id_rsa.pub 在home/lwq/.ssh目录中

添加密钥到ssh：ssh-add 文件名  需要之前输入密码。 

$cat id_rsa.pub 复制里面的内容，即ssh
https://github.com/，在setting中SSH and GPG keys添加ssh

5.测试：ssh git@github.com

------------------------------------------------
仓库上传
echo "# my-document" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:liangwuqiang/my-document.git
git push -u origin master

-----------------------------------------------
解决git status中文显示的问题：

$ git status -s
?? "\350\257\264\346\230\216.txt\n
$ printf "\350\257\264\346\230\216.txt\n"
说明.txt

通过将Git配置变量 core.quotepath 设置为false，就可以解决中文文件名称在这些Git命令输出中的显示问题，
示例：
# $ git config --global core.quotepath false
$ git status -s
?? 说明.txt
