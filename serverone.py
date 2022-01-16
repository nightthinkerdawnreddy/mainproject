import socket
import threading
import time
s=socket.socket()
print('socket created')
s.bind(('localhost',9999))
l=[]
def func():
    while True:
        s.listen(3)
        c,addr=s.accept()
        l.append(c)
t1=threading.Thread(target=func)
t1.start()

from pynput import mouse,keyboard
def on_move(x, y):
    #pos=str(x)+','+str(y)+'move'
    #c.send(bytes(pos,'utf-8'))  
    pos='Pointer moved to {0}'.format((x, y)) 
    for i in l:
        i.send(bytes(pos,'utf-8'))
    
    #c.send(bytes(pos,'utf-8'))
def on_click(x, y, button, pressed):
    #print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
    pos='On click {0}'.format((str(x),str(y)))#str(x)+','+str(y)+'onclick'
    #c.send(bytes(pos,'utf-8'))
    for i in l:
        i.send(bytes(pos,'utf-8'))
    '''if not pressed:
        #Stop listener
        return False'''
def on_scroll(x, y, dx, dy):
    pos='Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y))
    #pos=str(x)+','+str(y)+'onscroll'
    #c.send(bytes(pos,'utf-8'))
    for i in l:
        i.send(bytes(pos,'utf-8'))

# Collect events until released
'''with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()'''
# ...or, in a non-blocking fashion:
from pynput import keyboard
def on_press(key):
    try:
        #c.send(bytes(str(key),'utf-8'))
        for i in l:
            i.send(bytes(str(key.char),'utf-8'))
    except AttributeError:
       # print('special key {0} pressed'.format(key))
        #c.send(bytes(str(key),'utf-8'))
        for i in l:
            i.send(bytes(str(key),'utf-8'))
def on_release(key):
    pass
    #print('{0} released'.format(key))
    '''if key == keyboard.Key.esc:
        # Stop listener
        return False'''
    #c.send(bytes(str(key),'utf-8'))
# Collect events until released
'''with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()'''

# ...or, in a non-blocking fashion:
keyboardlistener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
keyboardlistener.start()
mouselistener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
mouselistener.start()
keyboardlistener.join()
mouselistener.join()

    
    
    