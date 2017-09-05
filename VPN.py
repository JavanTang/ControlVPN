#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/30 13:49
# @Author  : TangZhiFeng
# @File    : VPN.py
# @Software: PyCharm Community Edition

import os


class VPNHelper(object):
    def __init__(self, _vpnIP, _userName, _passWord, WinDir=r"C:\windows\system32", RasDialFileName=r'\rasdial.exe'):
        self.IPToPing = _vpnIP
        self._VPNName = _vpnIP;
        self._UserName = _userName;
        self._PassWord = _passWord;
        self._WinDir = WinDir
        self._RasDialFileName = RasDialFileName
        self._VPNPROCESS = self._WinDir + self._RasDialFileName

    def TryConnectVPN(self):
        try:
            command = self._VPNName + " " + self._UserName + " " + self._PassWord
            os.system(self._VPNPROCESS + " " + command)
        except:
            print("VPN连接失败!")

    def TryDisConnectVPN(self):
        try:
            command = self._VPNName + " /d"
            os.system(self._VPNPROCESS + " " + command)
        except:
            print("VPN断开失败!")

    def Restart(self, waitingTime=0):
        import time
        self.TryDisConnectVPN()
        time.sleep(waitingTime)
        self.TryConnectVPN()


if __name__ == "__main__":
    vpn = VPNHelper("sdtadx.ipduoduo.cc", "hz0003", "hanzheng")
    vpn.Restart()
