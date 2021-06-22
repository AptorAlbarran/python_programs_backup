# esto es para iniciar sin que sea clase
# if __name__=="__main__":
#     nm()
import os
def junta(x):
    # print(x) # guardo esta lista para la futura funcion de ir atras
    try:
        if x.index('home')==0:
            x=[sub.replace('home','/home')for sub in x]
            b='/'.join(map(str,x))
            # print(b)
            return b
    except ValueError:
        b='/'.join(map(str,x))
        # print(b)
        return b
        pass
a=input('accion: ')
raiz=0
ruta_rel=0
def ax(a):
    if a=='establece raiz':
        temp=os.getcwd()
        print(temp)
        b=input('este directorio está bien? y/n ')
        global raiz
        if b=='y':
            raiz=temp
            ax(a=input('algo más? '))
        elif b=='n':
            tr=junta(x=input('nueva ruta de raiz separada por: "¡" ').split('¡'))
            try:
                raiz=os.chdir(tr)
            except FileNotFoundError:
                print('esa vaina no existe, para intentar de nuevo escribe el mismo comando')
                pass
            raiz=tr
            ax(a=input('algo más? '))
    elif a=='muestra raiz':
        print(raiz)
        ax(a=input('algo más? '))
    elif a=='ontoi':
        c=os.getcwd()
        print(c)
        ax(a=input('algo más? '))
    elif a=='ve a':
        d=junta(x=input('ruta separada por "¡": ').split('¡'))
        try:
            td=os.chdir(d)
        except FileNotFoundError:
            print('esa vaina no existe, para intentar de nuevo escribe el mismo comando')
            pass
        ax(a=input('algo más? '))
    elif a=='regresa a raiz':
        os.chdir(raiz)
        ax(a=input('algo más? '))
    elif a=='crea':
        b=input('archivo/directorio:\n')
        if b=='directorio':
            temp=os.path.join(junta(x=input('dame la ruta del nuevo directorio separada por "¡": ').split('¡')))
            if not os.path.exists(temp):
                os.mkdir(temp)
            else:
                print('ya existe el directorio')
            ax(a=input('algo más? '))
        elif b=='archivo':
            temp=os.path.join(junta(x=input('dame la ruta del directorio donde se creara el nuevo archivo, terminando con la extencion del mismo (.txt), separada por "¡": ').split('¡')))
            if not os.path.isfile(temp):
                arch=open(temp,'w+')
                lines=[]
                while True:
                    line=input()
                    if line:
                        lines.append(line)
                    else:
                        break
                text='\n'.join(lines)
                arch.write(text)
            else:
                print('el archivo ya existe')
    elif a=='muestra contenido de':
        b=input('archivo/directorio:\n')
        if b=='archivo':
            temp=os.path.join(junta(x=input('dame la ruta del directorio donde se encuentra el archivo, separada por "¡": ').split('¡')))
            if os.path.isfile(temp):
                arch=open(temp,'r')
                lee=arch.read()
                print(lee)
            else:
                print('el archivo no existe')
        elif b=='directorio':
            temp=os.path.join(junta(x=input('dame la ruta del directorio, separada por "¡": ').split('¡')))
            if os.path.exists(temp):
                # print('si existe')
                for files in os.listdir(temp):
                    if not files.startswith('.'):
                        print(files)
            else:
                print('esa vaina no existe')
        ax(a=input('algo más? '))
    elif a=='borra':
        print('borrar opcion')
        
    elif a=='modifica':
        print('modifica opcion')
    elif a=='ño':
        print('sale bye')
ax(a)
