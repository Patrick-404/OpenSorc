import requests
from bs4 import BeautifulSoup

def pesan():
    cookie = input("Coki : ")
    url = input("Masukkan ID : ")
    chat = input("Text : ")
    jumlah_pesan = int(input("Masukkan jumlah pesan yang akan dikirim: "))  # Meminta jumlah pesan dari pengguna
    url = "https://mbasic.facebook.com/messages/read/?fbid=" + url
    with requests.session() as ses_xxx:
        halaman = ses_xxx.get(url, cookies={"cookie": cookie}).content
        sop = BeautifulSoup(halaman, "html.parser")
        form = sop.find("form", method="post")
        url_post = form["action"]
        payload = {}
        for xxx in form:
            input_ = xxx
            payload[input_.get("name")] = input_.get("value")
        
        for _ in range(jumlah_pesan):  # Loop untuk mengirim jumlah pesan yang diminta
            payload.update({"body": chat,
                            "send": "kirim" })
            ses_xxx.post("https://mbasic.facebook.com"+url_post, data=payload, cookies={"cookie": cookie})
            print('Pesan berhasil dikirim')
        
        print('Sukses..')

# Gunakan fungsi pesan dengan cookie yang sesuai
pesan()
