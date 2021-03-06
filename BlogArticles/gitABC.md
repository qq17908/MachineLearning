3/20/2016 10:31:23 PM 
![](http://i.imgur.com/dXQM4aU.png)
# **专用名词** #
    1.  workspace:工作区
    2.  Index / Stage :暂存区
    3.  Repository：仓库区（或本地仓库）
    4.  Remote：远程仓库

# 一、集中式和分布式 #
	集中式版本控制，即建立中央服务器，在中央服务器保管所有版本控制内容。若你需要对某个内容进行修改时，需从“中央服务器”先提取至本地，在完成修改后，重新提交至“中央服务器”。常见的有SVN，CVS，VSS。
	
	分布式版本控制，即每个本地版本含有全套内容（每个本地版本即为中央服务器）。git属于分布式版本控制系统。

# 二、安装GIT #
	msysgit是Windows版的Git，从http://msysgit.github.io/下载，然后按默认选项安装即可

# 三、基本内容 #
##3.1 创建版本库##
1、初始化一个Git仓库，使用"git init"

2、添加文件至Git仓库：

	a、使用git add<file>,PS:可以反复多次使用，添加多个文件
	b、使用git commit，完成提交。
		
##3.2 版本回退##
	git status 理解仓库当前状态
	git diff 查看修改内容
	->HEAD 指向的版本就是当前版本。
	git log  查看提交历史
	git log --pretty=oneline
	
	git relog  查看命令历史
	git reset --hard HEAD    回退版本

##3.3 提交修改##
	git add 将工作区第一次修改的内容放入暂存区，准备提交
	git commit  只负责将暂存区内容提交至
	
##3.4 撤销修改##
	git checkout -- <file> 将工作区的修改全部撤销
	如果修改内容尚未放到“暂存区”，则回退到版本库版本；
	如果修改内容之前提交到“暂存区”，又做了修改，则撤销修改将回到“暂存区”版本
		
##3.5 删除文件##
	git rm <file> 删除版本库文件
	如果误删文件，可通过git checkout恢复之前版本。

# 四、远程仓库管理
Git是分布式版本控制系统，同一个Git仓库，可以分布到不同的机器上。
gitHub.com是一个免费git仓库托管服务网站。

##4.1 添加远程库##
	a、关联远程库
		git remote add origin git@server-name:path/repo-name.git;
	b、第一次推送master
		git push -u origin master
	c、再次推送
		git push origin master
		git push [remote] --force #强行推送当前分支到远程仓库，即使有冲突
		git push [remote] --all#推送所有分支到远程仓库
		
##4.2 从远程库克隆##
	git clone git@github.com:xxxxx/learnPython.git

##4.3 其它命令##
	git fetch [remote]  #下载远程仓库的所有变动
	git remote -v 显示所有远程仓库
	git remote show #显示某个远程仓库的信息
	git pull [remote][branch] 取回远程仓库的变化，并与本地分支合并


	
# 五、分支管理 #
##5.1 创建与合并分支##
-  	查看分支：git brach
-  	创建分支：git brache <name>
-  	切换分支：git checkout <name>
-  	创建+切换分支： git checkout -b <name>
-  	合并某分支到当前分支： git merge <name>
-  	删除分支： git branch -d <name>
	
##5.2 解决冲突##
	各个版本及分支都有修改主要在master和支线间。当git无法自动合并分支时，先人工解决冲突，再提交，完成合并。
	
	**git log --graph 可以看到分支合并图**
	
##5.3 分支管理策略##
	使用Fast forward模式进行合并分支，在这种模式下，删除分支后，将清除分支信息。
	git merge --no-ff -m "content" <branch>

##5.4 Bug分支##
	git stash 将当前工作现场“储藏”起来。
	git stash list 查看封存的工作现场
	恢复工作现场
		一种：git stash apply  #需要删除stash内容
			git stash drop
		二种：git stash pop
		
##5.5 Feature 分支##
	已经提交分支，进行强行删除：git branch -d <branchName>
	
##5.6 多人协作##
	1、查看远程库信息，git remove -v
	2、从本地推送分支git push origin branch-name ,如果推送失败，则先用 git pull 抓取远程的新提交文件；
	3、本地创建和远程分支：git checkout -b branch-name origin/branch-name
	4、建立本地分支和远程分支的关联：git branch --set-upstream branch-name origin/branch-name;
	
#六、标签管理#
	1、查看所有标签：git tag
	2、创建标签：git tag <name> <commit id>
	3、查看标签信息：git show <tagname>
	4、删除标签：git tag -d <tag-name>
	5、推送标签：git push origin <tag-name>
	6、推送全部未推送的本地标签：git push origin --tags
	7、删除远程标签：git push origin :refs/tags/<tagname>
	
#七、忽略特殊文件#
	需要忽略某些文件是，编写.gitignore
	.gitignore文件本身需要放在版本库中
	