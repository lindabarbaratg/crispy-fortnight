from seleniumbase import *
import random
from supabase import create_client, Client
import time
import csv
import string
import random
import os
from selenium.webdriver.common.keys import Keys


SUPABASE_URL = "https://cqakrownxujefhtmsefa.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNxYWtyb3dueHVqZWZodG1zZWZhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzIyNjMyMzMsImV4cCI6MjA0NzgzOTIzM30.E9jJxNBxFsVZsndwhsMZ_2hXaeHdDTLS7jZ50l-S72U"
SUPABASE_TABLE_NAME = "movie"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def random_string(count):
    string.ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return "".join(random.choice(string.ascii_letters) for x in range(count))





EMAIL ='lesley_nash@gdrive.or.id'
PASSWORD = 'Cobasih12#'



with SB(undetectable=True) as sb:
    try:
          
        
        sb.open('https://accounts.google.com/signin')
        sb.sleep(3)

        sb.type("#identifierId", EMAIL + Keys.ENTER )
    
        sb.sleep(2)
        
        sb.type("input[name='Passwd']", PASSWORD  + Keys.ENTER)
        sb.sleep(5)
       

        sb.open(f'https://wikiart.org/')
        sb.sleep(10)
        
        sb.click("b[class='ng-binding']")
        sb.sleep(2)

        sb.click("button[value='google']")
        sb.sleep(10)

        with open("x.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                kw = line[0]
                try:

                    nama_modif = kw.replace(" ", "-")
                        
                    
                    judul = f"!#[.VIRAL@CLIPS.] {kw} OnlyFans Private Video Original Leaked Full On Social Media "
                
                
                    sb.get("https://www.wikiart.org/en/edit/john-constable/new")
                    sb.sleep(10)
        

                    # Path file yang akan diunggah
                    file_path = "bs.jpg"
                    file_path = os.path.abspath(file_path) 

                    sb.choose_file("label.upload-button input[type='file']", file_path)

                    # Kirim path file ke input file untuk mengunggahnya
                    
                    sb.sleep(5)



                    sb.type("input[placeholder='Empty field'][name='PaintingName']",judul)
                    sb.sleep(3)         

                    konten = f"{judul} OnlyFans video Leaked Viral the internet. Watch {judul} OnlyFans Leaked Video Trending on Twitter (X), Discord. \n \n [url href=https://clipsfans.com?title={nama_modif}&ref=wikiart]CLICK HERE >>> WATCH {judul} Leaked Video[/url] \n \n [url href=https://clipsfans.com?title={nama_modif}&ref=wikiart]CLICK HERE >>> DOWNLOAD {judul} Leaked Video[/url] \n \n Who Is {judul} OnlyFans? \n \n Pakistani TikTok Star Deactivates Social Media Accounts After Private Video Leaks Online Pakistani TikToker {judul} OnlyFans is currently facing intense trolling after her explicit videos went viral on social media. Reacting to the controversy, {judul} OnlyFans has deactivated her social media account. \n \n {judul} OnlyFans viral video: Why {judul} OnlyFans has deactivated her account? \n \n The TikToker became the new victim of privacy breach after her explicit videos went viral, being shared widely on WhatsApp. After the controversy, {judul} OnlyFans has become a scapegoat for social media trolling and hate messages. Meanwhile, in interviews to local channels, {judul} OnlyFans has said that she was born on 7 October 2002 in Lahore. \n \n What’s there in the ‘explicit’ clip {judul} OnlyFans? \n \n Pakistani TikToker has met a similar fate to that of social media influencer {judul} OnlyFans. The Instagrammer is facing intense trolling after her explicit videos went viral on social media. Reacting to the controversy, {judul} OnlyFans has deactivated her social media account. \n \n The young TikToker has become the new victim of privacy breach after her explicit {judul} OnlyFans videos have gone viral on social media and have been shared widely on WhatsApp. After the controversy, she has become a scapegoat for social media trolling and hate messages. \n \n After facing immense trolling, the social media influencer deactivated her Instagram and TikTok accounts, reported Economic Times. {judul} OnlyFans has fallen prey to privacy breaches, and there is no information on whether she has taken any legal action in the matter. The incident raises serious questions about the privacy of social media influencers, as a few days ago, Pakistani TikTok {judul} OnlyFans received immense hate on social media after her explicit videos went viral online. \n \n Related Searches: \n \n {judul} OnlyFans Leaked Video on Twitter \n \n {judul} OnlyFans Leaked Leaks \n \n {judul} OnlyFans Leaked leak video \n \n {judul} OnlyFans Leaked leaked pictures \n \n {judul} OnlyFans Leaked explicit content leak \n \n {judul} OnlyFans Leaks \n \n {judul} OnlyFans Leaked Twitter Video \n \n {judul} OnlyFans Leaked \n \n {judul} OnlyFans Leaked Shower Video \n \n {judul} OnlyFans Leaked Photos \n \n {judul} OnlyFans Leak \n \n {judul} OnlyFans Leaked Porn \n \n {judul} OnlyFans Leaks 2024 \n \n {judul} OnlyFans Leaked Leaks \n \n {judul} OnlyFans Leaked Onlyfans Video \n \n {judul} OnlyFans Leaked 2024 \n \n {judul} OnlyFans Leaked personal information exposed \n"
                    sb.type("textarea[name='bbcode-area']",konten)
                    sb.sleep(5)
                    

                    sb.click("span[ng-hide='$root.ajaxRequest']")
                    sb.sleep(10)


                    response = (
                        supabase.table(SUPABASE_TABLE_NAME)
                        .insert({"result": sb.get_current_url()})
                        .execute()
                    )

                    print(f"SUKSES CREATE: {kw}")

                    sb.sleep(5)
                except:
                    print ("TERJADI ERROR")
    
    except Exception as e:
        print(f"Terjadi kesalahan:{str(e)}")
        sb.driver.quit()  # Tutup browser jika terjadi kesalahan

