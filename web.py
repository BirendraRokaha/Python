import webbrowser

def web():
    u = str(input("Website Name: "))
    url = (f"http://www.{u}.com")
    webbrowser.open_new_tab(url)


n= int(input("How may websites do you want to visit? "))

# Open URL in a new tab, if a browser window is already open.
for i in range(n):
    web()

