# coding=utf-8
# 2015/5/21

import time,os

#显示
def showlist():
 os.system("cls")
 print time.strftime('%Y/%m/%d %H:%M:%S')
 print "n [ Todo x ",str(len(todolist)),']'
 print '...please input show/add */del nu/quit...'
 j = 1
 for line in todolist:
  print str(j) + '# ' + line
  j = j+1
 print '.........................................'

#增加
def additem(text):
 if len(todolist) > 9:
  print 'too many lists'
 else:
  os.system("cls")
 todolist.append(text)
 showlist()

#删除
def delitem(no): 
 if no < len(todolist):
  os.system("cls")
 del todolist[no]
 showlist()
 
def quit():
 with open('todo.txt','w') as filelist:
  for line in todolist:
   filelist.write(line)

if __name__ == '__main__':
 todolist = []
#读取文本数据
 with open('todo.txt','r') as filelist:
  for line in filelist.readline():
   todolist.append(line)

#显示列表
showlist()

#判断输入状态
while True:
 reply = raw_input()
 if reply == 'quit':#退出
  quit()
  break
 elif reply[0:4] == 'add ': #增加
  additem(reply.replace('add ',''))
 elif reply[0:4] == 'del ': #删除
  if len(reply) == 5:
   delitem(int(reply[4:5])-1)
  else:
   print 'input error'
 elif reply == 'show':
  showlist()
 else:
  print 'please input show/add/del/quit'