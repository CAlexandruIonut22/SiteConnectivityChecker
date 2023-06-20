import urllib.request
import tkinter as tk


def test_connectivity():
    window = tk.Tk()
    window.geometry('600x400')
    head = tk.Label(window, text='Site Connectivity Checker')
    head.pack(pady=30, side="top")

    def check_url():
        web = (url.get())
        status_code = urllib.request.urlopen(web).getcode()
        website_is_up = status_code

        if website_is_up == 200:
            tk.Label(window, text='Website Available').place(x=260, y=200)
        elif website_is_up == 303:
            tk.Label(window, text='Website Redirect').place(x=260, y=200)
        elif website_is_up == 400:
            tk.Label(window, text='Bad request').place(x=260, y=200)
        elif website_is_up == 404:
            tk.Label(window, text='Resource not found').place(x=260, y=200)
        elif website_is_up == 500:
            tk.Label(window, text='Internal server error').place(x=260, y=200)

    url = tk.StringVar()
    tk.Entry(window, textvariable=url).place(x=185, y=80, height=30, width=280)
    tk.Button(window, text='Check', command=check_url).place(x=285, y=150)
    window.mainloop()


if __name__ == '__main__':
    test_connectivity()
