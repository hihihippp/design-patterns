#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class HardWare(object):
    @classmethod
    def power_on(self):
        print('上电')

    @classmethod
    def bootloader(self):
        print('bootloader 启动')

    @classmethod
    def power_off(self):
        print('断电')


class OperatingSystem(object):
    @classmethod
    def load_kernel(self):
        print('加载内核')

    @classmethod
    def load_image(self):
        print('加载镜像')

    @classmethod
    def exit_os(self):
        print('退出操作系统')


class SoftWare(object):
    @classmethod
    def load_app(self):
        print('加载应用程序')

    @classmethod
    def exit_app(self):
        print('退出应用程序')


class Computer(object):
    @classmethod
    def __init__(self):
        self.hw = HardWare()
        self.os = OperatingSystem()
        self.sw = SoftWare()

    @classmethod
    def boot(self):
        self.hw.power_on()
        self.hw.bootloader()
        self.os.load_kernel()
        self.os.load_image()
        self.sw.load_app()

    @classmethod
    def shut_down(self):
        self.sw.exit_app()
        self.os.exit_os()
        self.hw.power_off()


if __name__ == '__main__':
    computer = Computer()

    print('开机')
    computer.boot()

    print('\n关机')
    computer.shut_down()
