# Функция поиска каталогов по реестру

import winreg
import win32con
import sys


def parse_reg(name, hive, flag):
    aReg = winreg.ConnectRegistry(None, hive)
    aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall", 0, win32con.KEY_READ | flag)
    count_subkey = winreg.QueryInfoKey(aKey)[0]
    ans = []
    for i in range(count_subkey):
        try:
            asubkey_name = winreg.EnumKey(aKey, i)
            asubkey = winreg.OpenKey(aKey, asubkey_name)
            app_name = winreg.QueryValueEx(asubkey, "DisplayName")[0]
            path_name = winreg.QueryValueEx(asubkey, "InstallLocation")[0]
            if name.lower() in app_name.lower() and path_name:
                if path_name[-1] == '\\':
                    ans.append(path_name[:len(path_name)-1]) 
                else:
                    ans.append(path_name)

        except EnvironmentError:
            continue
    return ans




