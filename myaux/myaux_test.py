#coding=utf-8


from command.Base import *
from command.myyabiao import *
import pyautogui
import time
from command.scene_yd import *





if __name__=="__main__":
    hwnd=Hwnd()
    my_hwnds=hwnd.get_hwnd()
    print()
    for key in my_hwnds.keys():
        print(my_hwnds.get(key))
        #hwndyabiao=yabiao(int(key))
        #hwndyabiao.get_scene()
        #hwndyabiao.qubiao()
        #print(biaodi)
        yd=scene_yd(int(key))
        #yd.changan_jiangnan()
        #yd.jiangnan_jianye()
        #yd.jianye_donghaiwan()
        yd.kuachengyundong("donghaiwan_aolaiguo")
