import ctypes
from tkinter import *

if __name__ == '__main__':
    root = Tk()
    root.wm_attributes("-alpha", 0.002, "-topmost", True)
    root.wm_overrideredirect(True)

    root.wm_protocol("WM_DELETE_WINDOW", lambda: "break")

    # root.wm_attributes("-alpha", 1, "-toplevel", True)

    #   store some stuff for win api interaction
    set_to_foreground = ctypes.windll.user32.SetForegroundWindow
    keybd_event = ctypes.windll.user32.keybd_event

    alt_key = 0x12
    extended_key = 0x0001
    key_up = 0x0002


    def steal_focus():
        keybd_event(alt_key, 0, extended_key | 0, 0)
        set_to_foreground(root.winfo_id())
        keybd_event(alt_key, 0, extended_key | key_up, 0)


    while True:
        x, y = root.winfo_pointerxy()
        x -= 1024
        y -= 512

        root.wm_geometry(f"4096x4096+{0}+{0}")
        # root.update()
        # root.update_idletasks()
        # root.wm_focusmodel()
        root.after(0, lambda: root.focus_force())
        root.after(0, lambda: root.focus_set())
        steal_focus()
        root.focus_lastfor()
        root.update()
        root.update_idletasks()
        root.focus_displayof()
        root.update()
        root.update_idletasks()
        root.focus_force()
        root.update()
        root.update_idletasks()
        root.focus_set()
        root.update()
        root.update_idletasks()
