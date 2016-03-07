# crawler
手机搜狐网应聘题目
编写思路：
	首先利用urllib模块将网页保存成文本形式，然后用正则表达式匹配源码中的src=“*****.jpg”,href="*****.css",src="****.js",也就是图片，css,js部分，然后在文本上搜索这些匹配并且利用urllib下载，html直接下载。
	文件夹名字就是用time模块把当地时间变成字符串，至于每隔60秒备份一次就是用time的sleep延迟时间。

用例：main.py -d 60 -u http://m.sohu.com -o /tmp/backup
