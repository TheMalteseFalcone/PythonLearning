import webbrowser
sorgu = input("Aratmak istediğiniz Kelime:")
adres = f"https://github.com/search?q={sorgu}"
webbrowser.open(adres)
