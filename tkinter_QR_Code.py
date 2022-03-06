import tkinter as tk
from tkinter import CENTER, ttk
import qrcode
from datetime import datetime


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # window
        self.title('QR CODE GENERATOR')
        self.geometry('270x100')
        self.text = tk.StringVar()

        self.entry = ttk.Entry(self,
                                textvariable=self.text,
                                justify=CENTER,
                                width=40,)
        self.entry.pack(pady=10)
        self.entry.bind('<Key-Return>', self.submit)

        # label
        self.label = ttk.Label(self, text='Enter your text')
        self.label.pack()

        # button
        self.button = ttk.Button(self, text='Generate QR')
        self.button['command'] = self.submit
        self.button.pack()

    def clear_entry(self):
        self.entry.delete(0, 'end')

    def time(self):
        now = datetime.now()
        self.time_now = now.strftime("%d-%m-%Y--%H-%M-%S")

    def submit(self, *args):
        self.time()
        qr_code = qrcode.QRCode(version=1, 
                                box_size=30, 
                                border=1,)

        if self.text.get() != "":
            qr_code.add_data(self.text.get())
            qr_code.make(fit=True)
            qr_img = qr_code.make_image(fill_color='black',
                                        back_color='white',)

            qr_img.save(self.time_now + '.png')
            self.clear_entry()
        else:
            # empty entry
            pass


if __name__ == '__main__':
    app = App()
    app.resizable(False, False)
    app.mainloop()