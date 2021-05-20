import winreg
from pywinauto import Application as APP
from pywinauto import keyboard
from pywinauto import timings
from time import sleep

def login(name,pwd,path,sa=False):
    # str replace
    pwd = str.replace(pwd," ","{SPACE}")
    # set RememberPassword
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,"SOFTWARE\Valve\Steam", 0, winreg.KEY_SET_VALUE )
    winreg.SetValueEx(key,"RememberPassword",0,winreg.REG_DWORD,0x00000001)
    winreg.SetValueEx(key,"AutoLoginUser",0,winreg.REG_SZ,"")
    winreg.CloseKey(key)
    # auto login
    app = APP().start(path)
    login_gui = app.window(title_re='Steam [^Guard].*',class_name='vguiPopupWindow')
    try:
        login_gui.wait("ready",30)
    except timings.TimeoutError:
        print("unknow")
        return "error"
    login_gui.set_focus()
    sleep(.1)
    keyboard.send_keys(name+"{TAB}"+pwd+"{TAB}{ENTER}")
    if(sa != False):
        print("have guard")
        guard_gui = app.window(title_re ='Steam Guard - .*',class_name='vguiPopupWindow')
        try:
            guard_gui.wait("ready")
        except timings.TimeoutError:
            print("timeout")
            pass
        guard_gui.set_focus()
        sleep(.1)
        keyboard.send_keys(sa.get_code()+"{ENTER}")
    login_gui.wait_not("visible",60000)

if __name__ == '__main__':
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,"SOFTWARE\Valve\Steam", 0, winreg.KEY_QUERY_VALUE )
    exe , t = winreg.QueryValueEx(key, "SteamExe")
    winreg.CloseKey(key)
    u=input("username:")
    p=input("password:")
    login(u,p,exe,g)