�������÷ֲ�ʽִ�нű���ִ�нű�֮ǰ����Ҫ���û�����
���� selenium-server-standalone-3.141.59.jar  
���عȸ������ͻ������������python��Ŀ¼��

��ֱ�������ҵĻ����Լ�����hub��http://192.168.0.127:4444/grid/console��
����hub����cmd-�� selenium-server-standalone-3.141.59.jar Ŀ¼�£��������java -jar selenium-server-standalone-3.141.59.jar -role hub -port 4444
����node�����cmd-�� selenium-server-standalone-3.141.59.jar Ŀ¼�£��������java -jar selenium-server-standalone-3.141.59.jar -role node -port 5555 -hub http://localhost:4444/gird/register                                        
PS:node�ɽ��������portҪ��ͬ


python ���ܰ�����  pip install package

�����ļ�ad��ͷ��Ϊadmin��������stu��ͷ��Ϊѧ����������th��ͷ��Ϊ��ʦ������