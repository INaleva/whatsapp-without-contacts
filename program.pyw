from tkinter import *
import webbrowser


class WindowsGui(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        top_frame = Frame(root)
        top_frame.pack(pady=10)

        bottom_frame = Frame(root)
        bottom_frame.pack(side=BOTTOM, pady=10)
        self.phone_text = Label(top_frame, text="Enter phone number:", fg="blue")
        self.phone_text.pack(side=LEFT)

        self.phone_number = Entry(top_frame, width=25)
        self.phone_number.pack(side=LEFT)
        self.phone_number.focus_set()

        self.open_whatsapp_button = Button(bottom_frame, text="Open Chat", command=self.open_chat_btn)
        self.open_whatsapp_button.pack()

        self.phone_text = Label(bottom_frame, text="Example: 0512345678 or 051-12345678", fg="grey")
        self.phone_text.pack()
        
        self.credits = Label(bottom_frame, text="Built by Ilia Naleva", fg="grey")
        self.credits.pack()

        self.credits = Label(bottom_frame, text="Built by Ilia Naleva", fg="grey")
        self.credits.pack()

    def open_chat_btn(self):
        number = self.phone_number.get()
        number = str(number).replace('-', '')
        url = "https://wa.me/" + "972" + number
        webbrowser.open_new_tab(url)

    def open_chat_enter(self, parent):
        number = self.phone_number.get()
        number = str(number).replace('-', '')
        url = "https://wa.me/" + "972" + number
        webbrowser.open_new_tab(url)




root = Tk()

root.title("Anonymous whatsApp chat")
root.geometry("300x130")
root.resizable(False, False)

win_gui = WindowsGui(root)
win_gui.phone_number.bind('<Return>', win_gui.open_chat_enter)
win_gui.pack()
root.mainloop()