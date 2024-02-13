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
https://mbasic.facebook.com/composer/mbasic/?csid=46de2cd6-e700-41cd-8106-0238e07814bd&cwevent=add_privacy&view_overview&av=100086390785409&privacyx=291667064279714&paipv=0&eav=Afb4qZqpSwT_KuMk_0i1JAcwdF4x7vr4KodTNm6fNcOB5zNlmAfEVWR7IObvE6xPU3k&wtsid=rdr_0CHtmtDdIwVRNr8QG&_rdr