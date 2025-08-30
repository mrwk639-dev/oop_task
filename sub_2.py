from time import time
from rich.console import Console

console = Console()

def send_Msg(msg):
    if isinstance(msg, BaseMsg):
        console.print(msg, style=msg.style)
    else:
        print(msg)

class BaseMsg:
    def __init__(self, data: str):
        self._data = data
    @property
    def style(self):
        return ""
    @property
    def data(self):
        return self._data 
    def __str__(self):
        return self._data   
    def __len__(self):
        return len(str(self))
    def __eq__(self, other):
        return str(self) == str(other)
    def __add__(self, other):
        if isinstance(other, BaseMsg):
            return self.__class__(str(self) + " " + str(other))
        elif isinstance(other, str):
            return self.__class__(str(self) + " " + other)
        else:
            raise TypeError("Can't add BaseMsg with this type")
class LogMsg(BaseMsg):
    def __init__(self, data: str):
        super()._init_(data)
        self._timestamp = int(time())

    @property
    def style(self):
        return "black on yellow"

    def __str__(self):
        return f"[{self._timestamp}] {self._data}"

class WarnMsg(LogMsg):
    @property
    def style(self):
        return "white on red"

    def __str__(self):
        return f"[!WARN][{self._timestamp}] {self._data}"

if __name__ == "_main_":
    m1 = BaseMsg("Normal message")
    m2 = LogMsg("This is a log")
    m3 = WarnMsg("This is a warning!")

    send_Msg(m1)
    send_Msg(m2)
    send_Msg(m3)