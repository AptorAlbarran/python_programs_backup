# import math
# print ("esto es una prueba")
# a=float(input("dame un numero a sumar"))
# b=float(input("dame el segundo numero"))
# c=a+b
# print('el resultado es: {0}'.format(c))

import os
# b=input('valores separados por: "¡" ').split('¡')
# print(b)
# def junta(a):
#     try:
#         if a.index('home')==0:
#             a=[sub.replace('home','/home')for sub in a]
#             b='/'.join(map(str,a))
#             print(b)
#             return b
#     except ValueError:
#         b='/'.join(map(str,a))
#         print(b)
#         return b
#         pass
# # junta(b)
# cambio=os.chdir(junta(b))
# print(os.getcwd())

# f=open('temp.txt','w+')
# f.write('archivo txt')
# f.close()

# lines=[]
# while True:
#     line=input()
#     if line:
#         lines.append(line)
#     else:
#         break
# text='\n'.join(lines)
# print(text)

o='/home/samuel'
# def lista(o):
#     for root,dirs,files in os.walk(o):
#         level=root.replace(o,'').count(os.sep)
#         indent=' '*4*(level)
#         print('{}{}/'.format(indent,os.path.basename(root)))
#         subindent=' '*4*(level+1)
#         for f in files:
#             print('{}{}'.format(subindent,f))
# lista(o)
# arr=os.listdir(o)
# print(arr)
for files in os.listdir(o):
    if not files.startswith('.'):
        print(files)
