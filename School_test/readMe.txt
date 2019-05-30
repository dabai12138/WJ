由于配置分布式执行脚本，执行脚本之前，需要配置环境：
下载 selenium-server-standalone-3.141.59.jar  
下载谷歌驱动和火狐驱动，放入python根目录下

启用node：打开cmd-到 selenium-server-standalone-3.141.59.jar 目录下，输入命令：java -jar selenium-server-standalone-3.141.59.jar -role node -port 5555 -hub http://192.168.0.127:4444/gird/register                                        
PS:node可建立多个，port要不同


python 功能包导入  pip install package

用例文件ad开头的为admin端用例；stu开头的为学生端用例，th开头的为教师端用例
