import platform
isletim,adi,Sayisi,surumu,mimarisi,islemci = platform.uname()


print(f"""İşletim Sistemi = {isletim + " " +Sayisi}\nKullanıcı Adı = {adi}\nİşlemci Mimarisi = {mimarisi}\nİşlemci = {islemci}\nPython Sürümü = {platform.python_version()}      """)