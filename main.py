def haftaning_kuni(sana):
    kunlar = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    sana = sana.split("-")
    sana = int(sana[2])
    hafta_kuni = kunlar[(sana - 1) % 7]
    return hafta_kuni

sana = input("Sana kiriting (yil-mojavaq-kun): ")
print(haftaning_kuni(sana))
