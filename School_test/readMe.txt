由于配置分布式执行脚本，执行脚本之前，需要配置环境：
配置Java环境
下载 selenium-server-standalone-3.141.59.jar  
下载谷歌驱动和火狐驱动...，放入python根目录下

分布式管理：
（直接连接我的或者自己启用hub；http://localhost:4444/grid/console）
启用hub：打开cmd-到 selenium-server-standalone-3.141.59.jar 目录下，输入命令：java -jar selenium-server-standalone-3.141.59.jar -role hub -port 4444
启用node：打开cmd-到 selenium-server-standalone-3.141.59.jar 目录下，输入命令：java -jar selenium-server-standalone-3.141.59.jar -role node -port 5555 -hub http://localhost:4444/gird/register                                        
PS:node可建立多个，port要不同

配置python3环境：
python 功能包导入  pip install package
用例文件ad开头的为admin端用例；stu开头的为学生端用例，th开头的为教师端用例
common：存放自定义的方法函数
report:存放最新测试报告
screen:存放截图照片
Test_case:存放测试用例
Tools:工具包
WX_data:存放数据、页面元素（Excel、Csv）
WX_Log:存放log日志
run_all_case.py:运行脚本、生成测试报告
