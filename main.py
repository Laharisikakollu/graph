import functions
from collections import defaultdict
#dic = defaultdict(list)
dic={}
'''node = list(input("Enter the nodes ").split())
for i in node:
  lis=[]
  lis=input("Enter the nodes linked to node "+i).split()
  dic[i]=lis
print(functions.edges(dic))'''
while True:
  n=int(input("1-insert edge\n2-delete edge\n3-delete node\n4-exit\n"))
  if(n==1):
    u,v=input("Enter the edge to be inserted  ").split()
    functions.insert(dic,u,v)
  elif(n==2):
    u,v=input("Enter the edge to be deleted  ").split()
    functions.deleteedge(dic,u,v)
  elif(n==3):
    u=input("Enter the node to be deleted  ")
    functions.deletenode(dic,u)
  else:
    break