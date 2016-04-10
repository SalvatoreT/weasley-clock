from pynetgear import Netgear
import json
import tkinter as tk
import pygubu

class Application:

    def __init__(self, master):
        builder = pygubu.Builder()
        builder.add_from_file('main_screen.ui')
        self.mainwindow = main_window = builder.get_object('horizontal_container', master)
        self.add_image(main_window)
        self.add_image(main_window)

    def add_image(self, master):
        builder = pygubu.Builder()
        builder.add_from_file('person_tile.ui')
        parent = builder.get_object('tile_frame', master)
        builder.get_variable('timestamp_text').set('Hey')
        parent.pack(side=tk.LEFT)
        return parent

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()


def hello_world():
    return json.dumps(Netgear().get_attached_devices())


def get_devices():
    from pynetgear import Device
    return [
        Device(
            signal=9,
            ip='192.168.1.4',
            name='Cool Laptop',
            mac='D0:21:E3:73:07:98',
            type='wireless',
            link_rate=26),
        Device(
            signal=None,
            ip='192.168.1.5',
            name='Chromecast',
            mac='CD:E2:9E:84:57:9B',
            type='wired',
            link_rate=None),
        Device(
            signal=None,
            ip='192.168.1.6',
            name='Real iPhone',
            mac='CC:A1:FA:7B:C6:BE',
            type='wireless',
            link_rate=65)]
