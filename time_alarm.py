import time

flag=True       #定义一个标志
while True:
    h,m,s=time.localtime().tm_hour,time.localtime().tm_min,time.localtime().tm_sec
    print(h,m,s)
    if s==0 and flag==True:     #对应时间，有标志运行
        print('0')
        time.sleep(1)
        flag=False      #运行一次，标志取消，防止时间段内多次运行
    if s==20 and flag==True:
        print('20')
        time.sleep(1)
        flag=False
    if s==40 and flag==True:
        print('40')
        time.sleep(1)
        flag=False

    if s!=0 and s!=20 and s!=40:        #不在对应时间，标志恢复
        flag=True
        time.sleep(1)
