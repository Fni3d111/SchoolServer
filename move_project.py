import shutil
import win32file
import os
import time

def locate_usb():
    drive_list = []
    drivebits=win32file.GetLogicalDrives()
    for d in range(1,26):
        mask=1 << d
        if drivebits & mask:
            # here if the drive is at least there
            drname='%c:\\' % chr(ord('A')+d)
            t=win32file.GetDriveType(drname)
            if t == win32file.DRIVE_REMOVABLE:
                drive_list.append(drname)
    return drive_list

source_dir = locate_usb()
source_dir = f'{source_dir[0]}Client'
print(source_dir)
destination_dir = r"C:\Client"
exe_tree = r"C:\Client\client.exe"

def run():
    os.startfile(exe_tree)


def copy():
    shutil.copytree(source_dir, destination_dir)

try:
    copy()
    run()
    print("DONE")
except Exception as e: print(e);
