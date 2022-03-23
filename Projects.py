try:
    import sys
    import requests
    import os
    from  requests import get
    import uuid
    import time
    import json
    from time import sleep
    import random
except Exception as e:
    print(e)
    input("[$] Click Enter To Exit...")
    sys.exit()
os.system('cls')
os.system('color a')
def out():
    print("+" + "-" * 10 + "Close" + "-" * 10 + "+")
    input("[$] Click Enter To Exit...")


rs = requests.session()
uid = str(uuid.uuid4())
print("""
    █████╗ ██████╗ ██████╗ 
   ██╔══██╗██╔══██╗██╔══██╗
   ╚█████╔╝██████╔╝██████╔╝
   ██╔══██╗██╔═══╝ ██╔══██╗
   ╚█████╔╝██║     ██║  ██║
    ╚════╝ ╚═╝     ╚═╝  ╚═╝        
      [ Programmer 8PR ]      
""")
print("instagram [ @T8PR ] Follow Me <3")
print("+"+"-"*10+"Programmer-8PR"+"-"*10+"+")
print("[+] Choose The Tool,")
print("""
+---------Checkers---------+
|  [01] Twitch Checker     |
|  [02] TikTok Checker     |
|  [03] GitHub Checker     |
|  [04] Reddit Checker     |
|  [05] Pastebin Checker   |
|  [06] Tellonym Checker   |
|  [07] Zoomerang Checker  |
+--------------------------+

+----------Another---------+
|  [08] IG info            |
|  [09] Cut Urls           |
|  [10] Find User          | 
|  [11] The Title          |
|  [12] Zoomerang Reg      |
|  [13] Get Session ID     |
|  [14] Best User Maker    |
+--------------------------+
""")
# Start Coding \
try:
    tool = int(input("[?] Enter Here : "))
except ValueError:
    print("[-] Just Number !!")
    out()
    sys.exit()
if tool == 1:
    def twitch_checker():
        print("[+] Twitch Checker Was Run...")
        print("+" + "-" * 10 + "Programmer-8PR" + "-" * 10 + "+")
        print(f"# Twitch Checker By [ Programmer 8PR ] | My Account In instagram [@t8pr] Follow Me <3")
        print(f"( Enjoy <3 )")
        print("---------------------------------")
        input("[+] Click Enter To Start \n")

        v_1 = 0
        v_2 = 0
        v_3 = 0
        the_list = open("users.txt", "r")

        while True:
            user = the_list.readline().split("\n")[0]
            if user == "":
                break
            twitch_url = f"https://m.twitch.tv/{user}"

            headers = {
                'Host': 'm.twitch.tv',
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
                "Accept-Language": "en-us",
                "Accept-Encoding": "gzip, deflate, br",
                "Referer": "https://m.twitch.tv/service-worker.js",
                'Connection': 'keep-alive'
            }

            re = rs.get(twitch_url, headers=headers)
            if re.status_code == 404:
                if len(user) >= 4:
                    v_1 += 1
                    v_2 += 1
                    print(f"[+] Available --> [{user}] | --> [{v_1}]")
                    with open("Available.txt", "a") as Save:
                        Save.write(f"{user}\n")
                else:
                    v_1 += 1
                    v_3 += 1
                    print(f"[-] Less Than 4 --> [{user}] | --> [{v_1}]")
            elif re.status_code == 200:
                v_1 += 1
                v_3 += 1
                print(f"[-] Not Available --> [{user}] | --> [{v_1}]")
        the_list.close()
        print("---------------------------------")
        print(f"Checked Was Successfully")
        print(
            f"Available Users : [{v_2}] | Not Available Users : [{v_3}] | Users Was Checked : [{v_1}]\nAll Available Users Was Saved In [ Available.txt ]")
        print("---------------------------------")
        out()
        sys.exit()
    twitch_checker()
elif tool == 2:
    def tiktok_checker():
        print("[+] TikTok Checker Was Run...")
        print("+" + "-" * 10 + "Programmer-8PR" + "-" * 10 + "+")
        print(f"This TikTok Checker By [ Programmer 8PR ] Follow Me In instgaram [@t8pr] <3")
        print("---------------------------------")
        input(f"[+] Click Enter To Start \n")

        the_list = open("users.txt", "r")
        All = 0
        Good = 0
        Bad = 0
        while True:
            List = the_list.readline().split("\n")[0]
            if List == "":
                break
            url = f'https://www.tiktok.com/@{List}?lang=ar'

            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
                "Connection": "close",
                "Host": "www.tiktok.com",
                "Accept-Encoding": "gzip, deflate",
                "Cache-Control": "max-age=0"
            }

            re = rs.get(url, headers=headers)
            if re.status_code == 404:
                All += 1
                Good += 1
                print(f"[+] Available --> [{List}] | --> [{All}]")
                with open("Available.txt", "a") as Save:
                    Save.write(f"{List}\n")
            elif re.status_code == 200:
                All += 1
                Bad += 1
                print(f"[-] Not Available --> [{List}] | --> [{All}]")
            else:
                All += 1
                Bad += 1
        the_list.close()
        print("---------------------------------")
        print(f"Checked Was Successfully")
        print(
            f"Available Users : [{Good}] | Not Available Users : [{Bad}] | Users Was Checked : [{All}]\nAll Available Users Was Saved In [ Available.txt ]")
        print("---------------------------------")
        out()
        sys.exit()
    tiktok_checker()
elif tool == 3:
    def github_checker():
        print("[+] GitHub Checker Was Run...")
        print("+" + "-" * 10 + "Programmer-8PR" + "-" * 10 + "+")
        print(f"This GitHub Checker By [ The Deep 8PR ] Follow Me In instgaram [@t8pr]")

        print("---------------------------------")
        input(f"[+] Click Enter To Start \n")
        the_list = open("users.txt", "r")
        All = 0
        Good = 0
        Bad = 0
        while True:
            List = the_list.readline().split("\n")[0]
            if List == "":
                break
            url = f'https://github.com/{List}'

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'cookie': '_octo=GH1.1.757675268.1606661116; _device_id=f629b81e5083a13fa7ff014a68f146ad; tz=Asia%2FDubai; tz=Asia%2FDubai; user_session=1_webWJdC6-KCRvLPP8kCdYXseBBDeWd-uLbw5B1PN8iGaqg; __Host-user_session_same_site=1_webWJdC6-KCRvLPP8kCdYXseBBDeWd-uLbw5B1PN8iGaqg; logged_in=yes; dotcom_user=w89X; has_recent_activity=1; _gh_sess=EjdS347LjhnAHcdI%2B7aLQV9xGe0exyfegs3osnq3UdiDl8rOC8td4pKGZ%2Fp0qpn6xGlE2Apl2BuZgSYL9rUGuBHBzcJ%2Fi05RwIMeoWi%2BxGRWFWUeZp5O38PUCLx3sJ%2BYTJRxjs0NC84iYLcNpygCph5UNw2mHR4WD96F5jMTUNVj5wQH4ntWGHeAtvcDXF9h4sS1k4iLZ%2Bxj97PDOg8PpyhWTaOiQK7awdm2V9AGKcRsdhpkZ4Y5%2BtK1ytFCA9FlLUsshiHc2eBp8eE8kS03rhh1UeFgyeywoOJOYCID2cM%2BmYszXQxkAMbsGay8youvQzxL128%2B4kgG%2FCLX8insdoEZjsSxPFEge7F1myY5IBxDjeOui8skQfY3qjWQ1qWz%2Fpz4ort3tL8jfkN8H7ZYP3%2BL1n9AHayFw4ehNLlnJWyVSicbcxq7T1IqdpGrqiFHDTOhN%2Fg9A0zqK%2FLt%2FNAsplwVcRtwVMBsfynjEKVd3tYJXytFccDS3uGI1uUtahGYHspepz3gWL1tGuM88%2BsvBG6ao%2Bv1Jeg91LziNDgqrFzA4rTFdMHhLzhzBoaZXbK4w%2F4sUMZrz7QdSjJ7Cgy6E%2BkGzuAFX7Y9qyFPTa0b%2BO2flxg7oJIHAk%2B%2Bl0I4LC8fBXeT0q2th6mzki%2F3oqS38AL1ZRDm8hTZhzAv%2FvNc7amwOHCjveVnU1N0rfEOPHyX24JF3clZggLB0ptgfcFmkW9u%2FlBNDAZSOzwjXG5l6a18TV%2FtR6HoX2V5tViSqspjpurMiE2%2F7oWKoMWDa6eZe89o9QMtuj2FDi1txY18WbSlJmfUSSfERCvzL00KyVgj47l00bPFtgD7y2WkGFEYO2S9CTMkvX2P6og2igbY5LRqL94K9cEXd5vTvdLMF3cp%2FMgCXGQ%2FmRwPYIVRmQRlzySV1%2FgaMVufn46k05Ubvl%2FmqPWr0A2BNfHARB%2F%2F31w5OeQAHIKWTqSThMmuZ3D2BGRXVm0%2FnpnYl2XUW%2Fo%2BtApuJ9KRQYKngVHOg5vu0U6hJx58Z7i09cB9tKisIY8q43kFfK%2FHkOjwfSdzUEaiRO6vqOBYS1sSUyRUMiJdbijkdIfN7dQVaUNXeMbY--epk8IbZB8LCR3S32--4y%2FdnK2SoukkzGXhhv245Q%3D%3D',
                # t8pr
                'if-none-match': 'W/"38bd103a9925fd49af948e551ca81125"',
                'referer': f'https://github.com/berliv',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
            }

            re = rs.get(url, headers=headers)
            if re.status_code == 404:
                All += 1
                Good += 1
                print(f"[+] Available --> [{List}] | --> [{All}]")
                with open("Available.txt", "a") as Save:
                    Save.write(f"{List}\n")
            elif re.status_code == 200:
                All += 1
                Bad += 1
                print(f"[-] Not Available --> [{List}] | --> [{All}]")
            else:
                All += 1
                Bad += 1
        the_list.close()
        print("---------------------------------")
        print(f"Checked Was Successfully")
        print(
            f"Available Users : [{Good}] | Not Available Users : [{Bad}] | Users Was Checked : [{All}]\nAll Available Users Was Saved In [ Available.txt ]")
        print("---------------------------------")
        out()
        sys.exit()
    github_checker()
elif tool == 4:
    def reddit_checker():
        print("[+] Reddit Checker Was Run...")
        print("+" + "-" * 10 + "Programmer-8PR" + "-" * 10 + "+")
        print(f"This Reddit Checker By [ The Deep 8PR ] Follow Me In instgaram [@t8pr]")

        print("---------------------------------")
        input(f"[+] Click Enter To Start \n")

        the_list = open("users.txt", "r")
        All = 0
        Good = 0
        Bad = 0
        while True:
            List = the_list.readline().split("\n")[0]
            if List == f"":
                break
            url = f'https://www.reddit.com/user/{List}'
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                'cookie': 'csv=1; edgebucket=XLi4dckGsH3ZzbBPkm; __aaxsc=1; recent_srs=t5_2riqp%2Ct5_37dnc%2C; G_ENABLED_IDPS=google; reddit_session=774396530106%2C2021-02-15T11%3A01%3A57%2C3ea6ea9fe7630a960e0d5bd7e82707205938ac26; loid=00000000009vr3p6t6.2.1610997412710.Z0FBQUFBQmdLbFNsQ2JhU0tkMFdSaGpna3lNb2RoSGNXcWduUWR0aFY5OVBjRjVUZF8wVmdNUEhuU1RLRjdnOW5aRTVZTUlUVjdDSVB5THJRVUVHRmdFUUNGUVhXdEVhVWlpZnBtTDlLUzdabGhJZXFZMmpmUjRmU0RjSVIyamR3bHR5V25ZSXBQeDM; token_v2=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTMzOTAzOTcsInN1YiI6Ijc3NDM5NjUzMDEwNi1yak1sUVJNNy1XODdBWXBuSTVWLXBFdmx6RDAiLCJsb2dnZWRJbiI6dHJ1ZSwic2NvcGVzIjpbIioiLCJlbWFpbCJdfQ.r4tOKmu4JR0mx9Nde2ztjAMBMINyS88e-R8tq9PeZnc; Puzzleheaded-Bit-529_recentclicks2=t3_3fytv0; USER=eyJwcmVmcyI6eyJnbG9iYWxUaGVtZSI6IlJFRERJVCIsImNvbGxhcHNlZFRyYXlTZWN0aW9ucyI6eyJmYXZvcml0ZXMiOmZhbHNlLCJtdWx0aXMiOmZhbHNlLCJtb2RlcmF0aW5nIjpmYWxzZSwic3Vic2NyaXB0aW9ucyI6ZmFsc2UsInByb2ZpbGVzIjpmYWxzZX0sIm5pZ2h0bW9kZSI6dHJ1ZSwicnBhbkR1RGlzbWlzc2FsVGltZSI6bnVsbCwidG9wQ29udGVudERpc21pc3NhbFRpbWUiOm51bGwsInRvcENvbnRlbnRUaW1lc0Rpc21pc3NlZCI6MH19; session_tracker=kkoilgqmkmagbhfjqj.0.1613387003522.Z0FBQUFBQmdLbFQ3clNqY0NNQ21qalRGbEhQR0pYbmsxbXBaWkJkd3BLajBRXy1zbjJRamZGMnNyNlJZTng4NnY0ZnFIQVkzeGFaVUQzbG5fdE9pVnotMTB0dXVXTFlic25uYXB5bFIyVXhsS2Y1bXFtWW1NbGJuRmRGVUVpTnE1TXFtbmhZRnQwN0M; session=676cbfbb8c2881ee93584adfdda78b7dffe4cd5fgASVSQAAAAAAAABK/1QqYEdB2AqVDgxHGn2UjAdfY3NyZnRflIwoZDBmYjAwNzQyN2Q5MzM4ODY3N2Y2ZjdjM2FjMjFiY2VhNTdiODUyYpRzh5Qu; aasd=6%7C1613386798125',
                # t8pr
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            }
            re = rs.get(url, headers=headers)
            if re.status_code == 404:
                if len(List) >= 3:
                    Good += 1
                    All += 1
                    print(f"[+] Available --> [{List}] | --> [{All}]")
                    with open("Available.txt", "a") as Save:
                        Save.write(f"{List}\n")
                else:
                    All += 1
                    Bad += 1
                    print(f"[-] Less Than 4 --> [{List}] | --> [{All}]")
            elif re.status_code == 200:
                All += 1
                Bad += 1
                print(f"[-] Not Available --> [{List}] | --> [{All}]")
            else:
                All += 1
                Bad += 1
        the_list.close()
        print("---------------------------------")
        print(f"Checked Was Successfully")
        print(
            f"Available Users : [{Good}] | Not Available Users : [{Bad}] | Users Was Checked : [{All}]\nAll Available Users Was Saved In [ Available.txt ]")
        print("---------------------------------")
        out()
        sys.exit()
    reddit_checker()
elif tool == 5:
    def pastebin_checker():
        print("[+] Pastebin Checker Was Run...")
        print("+" + "-" * 10 + "Programmer-8PR" + "-" * 10 + "+")
        print("instagram [ @T8PR ] Follow Me <3")
        print("+" + "-" * 37 + "+")
        # End Title /

        # Start Coding \
        input(f"[+] Click Enter To Start \n")

        the_list = open("users.txt", "r")
        All = 0
        Good = 0
        Bad = 0
        while True:
            List = the_list.readline().split("\n")[0]
            if List == "":
                break
            url = f'https://pastebin.com/u/{List}'
            re = rs.get(url)
            if re.status_code == 404:
                All += 1
                Good += 1
                print(f"[+] Available --> [{List}] | --> [{All}]")
                with open("Available.txt", "a") as Save:
                    Save.write(f"{List}\n")
            elif re.status_code == 200:
                All += 1
                Bad += 1
                print(f"[-] Not Available --> [{List}] | --> [{All}]")
            else:
                All += 1
                Bad += 1
        the_list.close()
        print("+" + "-" * 37 + "+")
        print(f"[+] Checked Was Successfully")
        print(
            f"[+] Available Users : [{Good}] | Not Available Users : [{Bad}] | Users Was Checked : [{All}]\n[+] All Available Users Was Saved In [ Available.txt ]")
        print("+" + "-" * 37 + "+")
        out()
        sys.exit()
        # End Coding /
    pastebin_checker()
elif tool == 6:
    def telloym_checker():
        print("[+] Tellonym Checker Was Run")
        print("+" + "-" * 10 + "Programmer-8PR" + "-" * 10 + "+")
        print(f"This Tellonym Checker By [Programmer 8PR] Follow Me In instgaram [@t8pr] <3")
        print("---------------------------------")
        input(f"[+] Click Enter To Start \n")

        the_list = open("users.txt", "r")
        All = 0
        Good = 0
        Bad = 0
        while True:
            List = the_list.readline().split("\n")[0]
            if List == "":
                break
            url = f'https://tellonym.me/{List}'

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                'cookie': '__cfduid=d0ffc45fa1efa9e0d736b1c14bb6c594a1605979176; _ga=GA1.2.821290333.1605979177; G_ENABLED_IDPS=google; __gads=ID=c7705da3c1f492a3:T=1606880061:S=ALNI_MZomN5KxOkG_i59jEZaJOEsiBQi6g; _gid=GA1.2.725225671.1606979880; cf_clearance=dcd41d1895597ca22ffa90136382f60ddea9e6e2-1606979881-0-150; __rtgt_sid=ki8ibzq4bp1k2d; _gat=1',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.24 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
            }

            re = rs.get(url, headers=headers)
            if re.status_code == 404:
                All += 1
                Good += 1
                print(f"[+] Available --> [{List}] | --> [{All}]")
                with open("Available.txt", "a") as Save:
                    Save.write(f"{List}\n")
            elif re.status_code == 200:
                All += 1
                Bad += 1
                print(f"[-] Not Available --> [{List}] | --> [{All}]")
            else:
                All += 1
                Bad += 1
        the_list.close()
        print("---------------------------------")
        print(f"Checked Was Successfully")
        print(
            f"Available Users : [{Good}] | Not Available Users : [{Bad}] | Users Was Checked : [{All}]\nAll Available Users Was Saved In [ Available.txt ]")
        print("---------------------------------")
        out()
        sys.exit()
    telloym_checker()
elif tool == 7:
    def zoomerang_checker():
        print("[+] Zoomerang Checker Was Run...")
        print("+" + "-" * 10 + "Programmer-8PR" + "-" * 10 + "+")
        print("+" + "-" * 10 + "Zoomerang" + "-" * 10 + "+")
        input(f"[+] Click Enter To Start \n")
        the_list = open("users.txt", "r")
        All = 0
        Good = 0
        Bad = 0
        while True:
            List = the_list.readline().split("\n")[0]
            if List == "":
                break
            url = f'https://us-central1-zoomerang-dcf49.cloudfunctions.net/apiv2/v2/user/short?username={List}'
            headers = {
                'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'cache': 'cache',
                'if-none-match': 'W/"107-5cF9jXLF+oqmjC3Ow3KrgEtTRIY"',
                'origin': 'https://zoomerang.app',
                'referer': 'https://zoomerang.app/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
            }
            Check = rs.get(url, headers=headers).text
            if '"message":"user not found"' in Check:
                All += 1
                Good += 1
                print(f"[+] Available --> [{List}] | --> [{All}]")
                with open("Available.txt", "a") as Save:
                    Save.write(f"{List}\n")
            else:
                All += 1
                Bad += 1
                print(f"[-] Not Available --> [{List}] | --> [{All}]")

        print("+" + "-" * 10 + "Zoomerang" + "-" * 10 + "+")
        print(
            f"[/] Available Users : [{Good}]\n[/] Not Available Users : [{Bad}]\n[/] Users Was Checked : [{All}]\n[<>] All Available Users Was Saved In [ Available.txt ]")
        print("+" + "-" * 10 + "Zoomerang" + "-" * 10 + "+")
        out()
        sys.exit()
    zoomerang_checker()
elif tool == 8:
    def ig_info():
        print("[+] IG info Was Run...")
        print("+" + "-" * 10 + "Programmer-8PR" + "-" * 10 + "+")

        def mood(M):
            for c in M + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(1. / 50)
        user = input(f"[?] Enter The Target : ")
        head = {
            'HOST': "www.instagram.com",
            'KeepAlive': 'True',
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
            'Cookie': 'cookie',
            'Accept': "*/*",
            'ContentType': "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
            "X-IG-App-ID": "936619743392459",
            "X-Instagram-AJAX": "missing",
            "X-CSRFToken": "missing",
            "Accept-Language": "en-US,en;q=0.9"
        }
        try:
            url = f'https://www.instagram.com/{user}/?__a=1'
            info = rs.get(url, headers=head).json()
        except Exception:
            print(f"[-] Maybe This Time Tool Is Broken Try Liter Or Restart Your Device..,")
            out()
            sys.exit()

        # ['graphql']['user']

        try:
            user = str(info['graphql']['user']['username'])
            ID = str(info['graphql']['user']['id'])
            private = str(info['graphql']['user']['is_private'])
            verified = str(info['graphql']['user']['is_verified'])
            business = str(info['graphql']['user']['is_business_account'])
            highlight = str(info['graphql']['user']['highlight_reel_count'])
            full_name = str(info['graphql']['user']['full_name'])
            posts = str(info['graphql']['user']['edge_owner_to_timeline_media']['count'])
            followers = str(info['graphql']['user']['edge_followed_by']['count'])
            following = str(info['graphql']['user']['edge_follow']['count'])
            link = str(info['graphql']['user']['external_url'])
            avatar = str(info['graphql']['user']['profile_pic_url_hd'])
            last = requests.get(avatar)
            last_avatar = last.headers['last-modified']
            bio = str(info['graphql']['user']['biography'])
        except Exception:
            print(f"[-] Check The Target Pls..,")
            out()
            sys.exit()
        print("_________________________________________________________")
        mood(f"[X] Username : [ {user} ]")
        mood(f"[X] ID : [ {ID} ]")
        if full_name == "":
            mood(f"[X] Full Name : [ Account Have No Name ]")
        else:
            mood(f"[X] Full Name : [ {full_name} ]")
        if private == "True":
            mood(f"[X] IS Private Account : [ Yes ]")
        else:
            mood(f"[X] IS Private Account : [ No ]")
        if verified == "True":
            mood(f"[X] IS Verified Account : [ Yes ]")
        else:
            mood(f"[X] IS Verified Account: [ No ]")
        if business == "True":
            mood(f"[X] IS Business Account : [ Yes ]")
        else:
            mood(f"[X] IS Business Account : [ No ]")
        mood(f"[X] Number Of Highlight : [ {highlight} ]")
        mood(f"[X] Number Of Posts : [ {posts} ]")
        mood(f"[X] Followers : [ {followers} ]")
        mood(f"[X] Following Them : [ {following} ]")
        if link == "":
            mood(f"[X] The Link : [ Account Have No Name ]")
        else:
            mood(f"[X] The Link : [ {link} ]")
        mood(f"[X] Last Time Was Avatar Changed [ {last_avatar} ]")
        mood(f"[X] Avatar Link : [ {avatar} ]")
        if bio == "":
            mood(f"[X] Bio : Account Have No Bio")
        else:
            mood(f"[X] Bio : \n{bio}")
        mood("_________________________________________________________")
        mood("Done Transfer")
        out()
        sys.exit()
    ig_info()
elif tool == 9:
    def cut_urls():
        print("[+] Cut Urls Was Run...")
        print("+" + "-" * 10 + "Programmer-8PR" + "-" * 10 + "+")
        def mood(deep):
            for i in deep + '\n':
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(1. / 50)
        print("instagram [ @T8PR ] Follow Me <3")
        print("+" + "-" * 31 + "+")
        Link = input("[?] Enter The Url : ")
        mood("+" + "-" * 10 + "The-Cut-Url" + "-" * 10 + "+")
        # Start Coding
        url = 'https://bitly.com/data/anon_shorten'
        head = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '59',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': '_xsrf=18c3d4f6a0a34f7897a8dc7dbfec6e7a; anon_u=cHN1X184MjVkZGUwNi0zZThlLTQxN2UtOTY5NC02MDgzNGE0ZmRmOGU=|1614970920|3278e45cc9ce0aac843247ad7de7bc4082d79f3f; optimizelyEndUserId=oeu1614970921823r0.07068580073875474; _ga=GA1.2.97694063.1614970923; _gid=GA1.2.531168222.1614970923; _gat=1; _mkto_trk=id:754-KBJ-733&token:_mch-bitly.com-1614970923279-32054; wow-modal-id-7=yes; anon_shortlinks=https://bit.ly/3rkUJ7R; __q_state_s3IbMN4fxgnkq7YJ=eyJ1dWlkIjoiNmI5MjA3ZTYtNmU2My00NDE3LTg2Y2YtNGZmYmM2M2UwYzk0IiwiY29va2llRG9tYWluIjoiYml0bHkuY29tIn0=',
            'origin': 'https://bitly.com',
            'referer': 'https://bitly.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'x-xsrftoken': '18c3d4f6a0a34f7897a8dc7dbfec6e7a',
        }
        data = {
            'url': Link,
        }

        Cut = requests.post(url, data=data, headers=head).json()
        try:
            URL = str(Cut['data']['id'])
        except KeyError:
            mood("[-] Bad Url !!?")
            out()
            sys.exit()
        mood(f"[+] [  {URL}  ]")
        mood("+" + "-" * 10 + "The-Cut-Url" + "-" * 10 + "+")
        # End Coding
        out()
        sys.exit()
    cut_urls()
elif tool == 10:
    def find_user():
        print("[+] Find User Was Run...")
        print("+" + "-" * 10 + "Programmer-8PR" + "-" * 10 + "+")
        print("instagram [ @T8PR ] Follow Me <3")
        print("=================================")
        user = input("[?] Enter The Username : ")
        if user == "":
            print("Enter Something Pls..,")
            out()
            sys.exit()
        else:
            print("_" * 40)

            def TikTok():
                url = f'https://www.tiktok.com/@{user}?lang=ar'

                headers = {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
                    "Connection": "close",
                    "Host": "www.tiktok.com",
                    "Accept-Encoding": "gzip, deflate",
                    "Cache-Control": "max-age=0"
                }

                re = rs.get(url, headers=headers)
                if re.status_code == 404:
                    print(f"[+] [ TikTok ] --> Available [{user}]")
                elif re.status_code == 200:
                    print(f"[-] [ TikTok ] --> Not Available [{user}]")

            # ------------------------------------------------------------------------------------------------------------------------------------------------------
            def Tellonym():
                url = f'https://tellonym.me/{user}'

                headers = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                    'cookie': '__cfduid=d0ffc45fa1efa9e0d736b1c14bb6c594a1605979176; _ga=GA1.2.821290333.1605979177; G_ENABLED_IDPS=google; __gads=ID=c7705da3c1f492a3:T=1606880061:S=ALNI_MZomN5KxOkG_i59jEZaJOEsiBQi6g; _gid=GA1.2.725225671.1606979880; cf_clearance=dcd41d1895597ca22ffa90136382f60ddea9e6e2-1606979881-0-150; __rtgt_sid=ki8ibzq4bp1k2d; _gat=1',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
                }
                re = rs.get(url, headers=headers)
                if re.status_code == 404:
                    print(f"[+] [ Tellonym ] --> Available [{user}]")
                elif re.status_code == 200:
                    print(f"[-] [ Tellonym ] --> Not Available [{user}]")

            # ------------------------------------------------------------------------------------------------------------------------------------------------------
            def GitHub():
                url = f'https://github.com/{user}'

                headers = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'max-age=0',
                    'cookie': '_octo=GH1.1.757675268.1606661116; _device_id=f629b81e5083a13fa7ff014a68f146ad; tz=Asia%2FDubai; tz=Asia%2FDubai; user_session=1_webWJdC6-KCRvLPP8kCdYXseBBDeWd-uLbw5B1PN8iGaqg; __Host-user_session_same_site=1_webWJdC6-KCRvLPP8kCdYXseBBDeWd-uLbw5B1PN8iGaqg; logged_in=yes; dotcom_user=w89X; has_recent_activity=1; _gh_sess=EjdS347LjhnAHcdI%2B7aLQV9xGe0exyfegs3osnq3UdiDl8rOC8td4pKGZ%2Fp0qpn6xGlE2Apl2BuZgSYL9rUGuBHBzcJ%2Fi05RwIMeoWi%2BxGRWFWUeZp5O38PUCLx3sJ%2BYTJRxjs0NC84iYLcNpygCph5UNw2mHR4WD96F5jMTUNVj5wQH4ntWGHeAtvcDXF9h4sS1k4iLZ%2Bxj97PDOg8PpyhWTaOiQK7awdm2V9AGKcRsdhpkZ4Y5%2BtK1ytFCA9FlLUsshiHc2eBp8eE8kS03rhh1UeFgyeywoOJOYCID2cM%2BmYszXQxkAMbsGay8youvQzxL128%2B4kgG%2FCLX8insdoEZjsSxPFEge7F1myY5IBxDjeOui8skQfY3qjWQ1qWz%2Fpz4ort3tL8jfkN8H7ZYP3%2BL1n9AHayFw4ehNLlnJWyVSicbcxq7T1IqdpGrqiFHDTOhN%2Fg9A0zqK%2FLt%2FNAsplwVcRtwVMBsfynjEKVd3tYJXytFccDS3uGI1uUtahGYHspepz3gWL1tGuM88%2BsvBG6ao%2Bv1Jeg91LziNDgqrFzA4rTFdMHhLzhzBoaZXbK4w%2F4sUMZrz7QdSjJ7Cgy6E%2BkGzuAFX7Y9qyFPTa0b%2BO2flxg7oJIHAk%2B%2Bl0I4LC8fBXeT0q2th6mzki%2F3oqS38AL1ZRDm8hTZhzAv%2FvNc7amwOHCjveVnU1N0rfEOPHyX24JF3clZggLB0ptgfcFmkW9u%2FlBNDAZSOzwjXG5l6a18TV%2FtR6HoX2V5tViSqspjpurMiE2%2F7oWKoMWDa6eZe89o9QMtuj2FDi1txY18WbSlJmfUSSfERCvzL00KyVgj47l00bPFtgD7y2WkGFEYO2S9CTMkvX2P6og2igbY5LRqL94K9cEXd5vTvdLMF3cp%2FMgCXGQ%2FmRwPYIVRmQRlzySV1%2FgaMVufn46k05Ubvl%2FmqPWr0A2BNfHARB%2F%2F31w5OeQAHIKWTqSThMmuZ3D2BGRXVm0%2FnpnYl2XUW%2Fo%2BtApuJ9KRQYKngVHOg5vu0U6hJx58Z7i09cB9tKisIY8q43kFfK%2FHkOjwfSdzUEaiRO6vqOBYS1sSUyRUMiJdbijkdIfN7dQVaUNXeMbY--epk8IbZB8LCR3S32--4y%2FdnK2SoukkzGXhhv245Q%3D%3D',
                    # t8pr
                    # t8pr
                    'if-none-match': 'W/"38bd103a9925fd49af948e551ca81125"',
                    'referer': f'https://github.com/berliv',
                    'sec-ch-ua-mobile': '?0',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
                }
                re = rs.get(url, headers=headers)
                if re.status_code == 404:
                    print(f"[+] [ GitHib ] --> Available [{user}]")
                elif re.status_code == 200:
                    print(f"[-] [ GitHub ] --> Not Available [{user}]")

            # ------------------------------------------------------------------------------------------------------------------------------------------------------
            def Twitch():
                twitch_url = f"https://m.twitch.tv/{user}"
                headers = {
                    'Host': 'm.twitch.tv',
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
                    "Accept-Language": "en-us",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Referer": "https://m.twitch.tv/service-worker.js",
                    'Connection': 'keep-alive'
                }

                re = rs.get(twitch_url, headers=headers)
                if re.status_code == 404:
                    if len(user) >= 4:
                        print(f"[+] [ Twitch ] --> Available [{user}]")
                    else:
                        print(f"[-] [ Twitch ] --> Less Than 4 [{user}]")
                elif re.status_code == 200:
                    print(f"[-] [ Twitch ] --> Not Available [{user}]")

            # ------------------------------------------------------------------------------------------------------------------------------------------------------
            def Twitter():
                url = f'https://tweeterid.com/ajax.php'
                headers = {
                    'Accept': '*/*',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'ar,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                    'Connection': 'keep-alive',
                    'Content-Length': '22',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Cookie': '__utma=116903043.1720803994.1612504548.1612504548.1612504548.1; __utmc=116903043; __utmz=116903043.1612504548.1.1.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmb=116903043.1.10.1612504548; __gads=ID=88cfb7beeee2c10b-22d6173bbfa600bb:T=1612504549:RT=1612504549:S=ALNI_MZ6nNZgByoGcMcYOoxsJhmoIAX2fg',
                    'Host': 'tweeterid.com',
                    'Origin': 'https://tweeterid.com',
                    'Referer': 'https://tweeterid.com/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
                    'X-Requested-With': 'XMLHttpRequest'
                }
                data = {
                    'input': user
                }
                re = rs.post(url, data=data, headers=headers).text
                if ('error') in re:
                    print(f"[+] [ Twitter ] --> Available [{user}]")
                else:
                    print(f"[-] [ Twitter ] --> Not Available [{user}]")

            # ------------------------------------------------------------------------------------------------------------------------------------------------------
            def Reddit():
                url = f'https://www.reddit.com/user/{user}'
                headers = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                    'cookie': 'csv=1; edgebucket=XLi4dckGsH3ZzbBPkm; __aaxsc=1; recent_srs=t5_2riqp%2Ct5_37dnc%2C; G_ENABLED_IDPS=google; reddit_session=774396530106%2C2021-02-15T11%3A01%3A57%2C3ea6ea9fe7630a960e0d5bd7e82707205938ac26; loid=00000000009vr3p6t6.2.1610997412710.Z0FBQUFBQmdLbFNsQ2JhU0tkMFdSaGpna3lNb2RoSGNXcWduUWR0aFY5OVBjRjVUZF8wVmdNUEhuU1RLRjdnOW5aRTVZTUlUVjdDSVB5THJRVUVHRmdFUUNGUVhXdEVhVWlpZnBtTDlLUzdabGhJZXFZMmpmUjRmU0RjSVIyamR3bHR5V25ZSXBQeDM; token_v2=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MTMzOTAzOTcsInN1YiI6Ijc3NDM5NjUzMDEwNi1yak1sUVJNNy1XODdBWXBuSTVWLXBFdmx6RDAiLCJsb2dnZWRJbiI6dHJ1ZSwic2NvcGVzIjpbIioiLCJlbWFpbCJdfQ.r4tOKmu4JR0mx9Nde2ztjAMBMINyS88e-R8tq9PeZnc; Puzzleheaded-Bit-529_recentclicks2=t3_3fytv0; USER=eyJwcmVmcyI6eyJnbG9iYWxUaGVtZSI6IlJFRERJVCIsImNvbGxhcHNlZFRyYXlTZWN0aW9ucyI6eyJmYXZvcml0ZXMiOmZhbHNlLCJtdWx0aXMiOmZhbHNlLCJtb2RlcmF0aW5nIjpmYWxzZSwic3Vic2NyaXB0aW9ucyI6ZmFsc2UsInByb2ZpbGVzIjpmYWxzZX0sIm5pZ2h0bW9kZSI6dHJ1ZSwicnBhbkR1RGlzbWlzc2FsVGltZSI6bnVsbCwidG9wQ29udGVudERpc21pc3NhbFRpbWUiOm51bGwsInRvcENvbnRlbnRUaW1lc0Rpc21pc3NlZCI6MH19; session_tracker=kkoilgqmkmagbhfjqj.0.1613387003522.Z0FBQUFBQmdLbFQ3clNqY0NNQ21qalRGbEhQR0pYbmsxbXBaWkJkd3BLajBRXy1zbjJRamZGMnNyNlJZTng4NnY0ZnFIQVkzeGFaVUQzbG5fdE9pVnotMTB0dXVXTFlic25uYXB5bFIyVXhsS2Y1bXFtWW1NbGJuRmRGVUVpTnE1TXFtbmhZRnQwN0M; session=676cbfbb8c2881ee93584adfdda78b7dffe4cd5fgASVSQAAAAAAAABK/1QqYEdB2AqVDgxHGn2UjAdfY3NyZnRflIwoZDBmYjAwNzQyN2Q5MzM4ODY3N2Y2ZjdjM2FjMjFiY2VhNTdiODUyYpRzh5Qu; aasd=6%7C1613386798125',
                    # 8pr
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
                }
                re = rs.get(url, headers=headers)
                if re.status_code == 404:
                    if len(user) >= 3:
                        print(f"[+] [ Reddit ] --> Available [{user}] ")
                    else:
                        print(f"[-] [ Reddit ] --> Less Than 3 [{user}] ")
                elif re.status_code == 200:
                    print(f"[-] [ Reddit ] --> Not Available [{user}] ")

            # ------------------------------------------------------------------------------------------------------------------------------------------------------
            def Instagram():
                url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'

                headers = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7',
                    'content-length': '61',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                    'origin': 'https://www.instagram.com',
                    'referer': 'https://www.instagram.com/accounts/emailsignup/',
                    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
                    'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                    'x-ig-app-id': '936619743392459',
                    'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
                    'x-instagram-ajax': '72bda6b1d047',
                    'x-requested-with': 'XMLHttpRequest'

                }
                data = {
                    'email': 'A@gmail.com',
                    'username': f'{user}',
                    'first_name': 'AAAAAA',
                    'opt_into_one_tap': 'false'
                }

                re = requests.post(url, headers=headers, data=data).text

                if (
                        '{"account_created": false, "errors": {"email": [{"message": "Too many accounts are using a@gmail.com.", "code": "email_sharing_limit"}], "__all__": [{"message": "Create a password at least 6 characters long.", "code": "too_short_password"}]}, "dryrun_passed": false, "username_suggestions": [], "status": "ok", "error_type": "form_validation_error"}') in re:
                    print(f"[-] [ Instagram ] --> Available [{user}] ")

                else:
                    print(f"[-] [ Instagram ] --> Not Available [{user}] ")

            def SnapChat():

                url = f'https://accounts.snapchat.com/accounts/get_username_suggestions'

                headers = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-length': '57',
                    'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
                    'cookie': 'xsrf_token=qguFhKiP7FrimtibnGvopQ; web_client_id=6dee3ce3-db42-4fd0-b538-682cdb294f9a; _scid=482919d7-1390-46c8-8951-d3031e352b63; _sca={%22cid%22:%22e22c1577-7f73-4b69-85ff-79b72444951a%22%2C%22token%22:%22v1.key.2020-03-05_UKiB4eNE.iv.MeUzIJboKx7l+nZu.zf9r/dgUl/1vg1iBp4fz27qapzxGL1VJowr9Clna1AvHYCTUocABFHpeSMdPC2BGmfDmAfrA8eEqFPnV5qNP/QJCPISHEUpj7aGeYGpoggjapYZZ%22}; sc-cookies-accepted=true; Preferences=true; Performance=true; Marketing=true; _ga=GA1.2.148694331.1613677502; _gid=GA1.2.1609447525.1613677502; _gat_UA-41740027-4=1',
                    'origin': 'https://accounts.snapchat.com',
                    'referer': 'https://accounts.snapchat.com/',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'same-origin',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
                }
                data = {
                    'requested_username': f'{user}',
                    'xsrf_token': 'qguFhKiP7FrimtibnGvopQ',
                }
                re = requests.post(url, data=data, headers=headers)
                if re.text.find('"status_code":"OK"') >= 0:
                    print(f"[+] [ SnapChat ] --> Available [{user}]")
                elif re.text.find('"status_code":"TAKEN"') >= 0:
                    print(f"[-] [ SnapChat ] --> Not Available [{user}]")
                else:
                    print(f"[-] [ SnapChat ] --> Banded [{user}]")

            def pastebin():
                # End Title /
                # Start Coding \
                url = f'https://pastebin.com/u/{user}'
                re = rs.get(url)
                if re.status_code == 404:
                    print(f"[+] [ Pastebin ] --> Available [{user}]")
                elif re.status_code == 200:
                    print(f"[-] [ Pastebin ] --> Not Available [{user}]")
                # End Coding /

            def zoomerange():
                url = f'https://us-central1-zoomerang-dcf49.cloudfunctions.net/apiv2/v2/user/short?username={user}'
                headers = {
                    'accept': 'application/json, text/plain, */*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache': 'cache',
                    'if-none-match': 'W/"107-5cF9jXLF+oqmjC3Ow3KrgEtTRIY"',
                    'origin': 'https://zoomerang.app',
                    'referer': 'https://zoomerang.app/',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'cross-site',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
                }
                Check = rs.get(url, headers=headers).text
                if '"message":"user not found"' in Check:
                    print(f"[+] [ Zoomerange ] --> Available [{user}]")
                else:
                    print(f"[-] [ Zoomerange ] --> Not Available [{user}]")

            Instagram()  # 1
            SnapChat()  # 2
            Tellonym()  # 3
            Twitter()  # 4
            TikTok()  # 5
            Twitch()  # 6
            GitHub()  # 7
            Reddit()  # 8
            pastebin()  # 9
            zoomerange()  # 10
        print("_" * 40)
        print("Find User Tool By Programmer 8PR")
        out()
        sys.exit()
    find_user()
elif tool == 11:
    def the_title():
        print("[+] The Title Was Run...")
        print("+" + "-" * 10 + "Programmer-8PR" + "-" * 10 + "+")
        print("instagram [ @T8PR ] Follow Me <3")
        print("=================================")
        def TITLE():
            title = input("[+] Enter The Title : ")
            print("_" * 40)
            print("")
            print("")
            Title = get('http://artii.herokuapp.com/make?text={}'.format(title)).text
            print(Title)
            print("_" * 40)
        # -=-==-=-=-==-@t8pr
        TITLE()
        out()
        sys.exit()
    the_title()
elif tool == 12:
    def zoomerang_reg():
        print("[+] Zoomerang Registry Was Run...")
        print("+" + "-" * 10 + "Programmer-8PR" + "-" * 10 + "+")

        Password = 't8pr1221'
        count = 0
        done = 0
        error = 0
        print("instagram [ @T8PR ] Follow Me <3")
        print("+" + "-" * 10 + "Zoomerang" + "-" * 10 + "+")
        email = input("[?] Enter The E-mail : ")
        try:
            looping = int(input("[?] Enter How Many Account Do You Want : "))
            slp = int(input("[?] Enter Sleep : "))
        except ValueError:
            print("Just Numbers !!")
            out()
            sys.exit()
        print("+" + "-" * 10 + "Programmer-8PR" + "-" * 10 + "+")
        for Acc in range(looping):
            count += 1
            Email = f"{email}.{count}@gmail.com"
            url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=AIzaSyAZyyldZdaECkbp9vEr0IkFFfghSgtv20U'
            headers = {
                'Accept': '*/*',
                'Accept-encoding': 'gzip, deflate, br',
                "Accept-Language": "en",
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
                'X-Client-Version': 'iOS/FirebaseSDK/6.9.2/FirebaseCore-iOS',
                'X-Ios-Bundle-Identifier': 'com.yantech.zoomerang'
            }
            data = {
                "email": Email,
                "password": Password,
                "returnSecureToken": "true"
            }
            Registry = rs.post(url, headers=headers, json=data).text
            if 'localId' in Registry:
                print(f"[+] Successfully Created >> [ {Email} ] | [{count}]")
                with open('Done Created.txt', 'a') as Save:
                    Save.write(f"{Email}\n")
                done += 1
            else:
                print(f"[-] Error Created >> [ {Email} ] | [{count}]")
                error += 1
            sleep(slp)
        print("+" + "-" * 10 + "Programmer-8PR" + "-" * 10 + "+")
        print(f"[<>] All Accounts Have Same Password -> [ {Password} ]")
        print(f"[<>] All Successfully Created Was Saved In [ Done Created.txt ] File")
        print("")
        print(f"[/] Successfully Created [{done}]\n[/] Error Created [{error}]\n[/] All Created [{count}]")
        out()
        sys.exit()
    zoomerang_reg()
elif tool == 13:
    def get_session_id():
        print("[+] Get Session ID Insta Was Run...")
        print("+" + "-" * 10 + "Programmer-8PR" + "-" * 10 + "+")

        print("instagram [ @T8PR ] Follow Me <3")
        print("_" * 40)
        user = input(f"[?] Enter Your Username : ")
        Pass = input(f"[?] Enter Your Password : ")
        Login_url = 'https://i.instagram.com/api/v1/accounts/login/'
        Login_head = {
            'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US",
            "X-IG-Capabilities": "3brTvw==",
            "X-IG-Connection-Type": "WIFI",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'Host': 'i.instagram.com'
        }
        Login_data = {
            '_uuid': uid,
            'username': user,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(Pass),
            'queryParams': '{}',
            'optIntoOneTap': 'false',
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_count': '0'
        }
        LOG = rs.post(Login_url, data=Login_data, headers=Login_head, allow_redirects=True)
        if LOG.text.find("is_private") >= 0:
            print(f"[+] Login Successfully To --> {user}")
            rs.headers.update({'X-CSRFToken': LOG.cookies['csrftoken']})
            print("_" * 40)
            sid = LOG.cookies['sessionid']
            print("")
            print(f"This Your Session id [ {sid} ]")
        elif LOG.text.find("invalid_credentials") >= 0:
            print(f"[x] Wrong Password --> {user} ")
        elif LOG.text.find('two_factor_required') >= 0:
            print(f"[x] Your Account Have Two Factor. Chang User.., ")
        else:
            print(f"[x] We Have PP With Your Request. Try Liter.., ")
            out()
            sys.exit()
    get_session_id()
elif tool == 14:
    def best_user_maker():
        print("[+] Best User Maker Was Run...")
        print("+" + "-" * 10 + "Programmer-8PR" + "-" * 10 + "+")

        print("instagram [ @T8PR ] Follow Me <3")
        print("+" + "-" * 10 + "User-Maker" + "-" * 10 + "+")
        try:
            Users = int(input("[?] Enter How Many User Do You Want : "))
            Letters = int(input("[?] Enter How Long Do You Want Letter : "))
        except ValueError:
            print("Just Numbers !!")
            out()
            sys.exit()

        def Make_users(data):
            Leeter = (Letters)
            User = ""
            while len(User) != Leeter:
                The_Choice = random.choice(data)
                User += The_Choice
            return User

        Choose = 'qwertyuioplkjhgfdsaxzcvbnm1234576890___'
        num = 0
        for Make in range(Users):
            Done_User = Make_users(Choose)
            with open('users.txt', 'a+') as Type:
                Type.write(f"{Done_User}\n")
                num += 1
                print(f"\r[+] Successfully Make >> [{num}] [{Done_User}]", end="")
        print("\n+" + "-" * 11 + "Filtering" + "-" * 10 + "+")
        the_file = open(f'users.txt')
        the_lines = the_file.readlines()
        the_lines = [line.strip() for line in the_lines]
        final_lines = {}

        def file_lengthy(fname):
            with open(fname) as f:
                for i, l in enumerate(f):
                    pass
            return i + 1

        def file_lengthy2(fname):
            with open(fname) as f:
                for i, l in enumerate(f):
                    pass
            return i + 1

        print("\r[+] Before Filtering -->", file_lengthy(f"users.txt"), end="")
        for line in the_lines:
            if line not in final_lines.keys():
                final_lines[line] = 0
        lines = "\n".join(list(final_lines.keys()))
        file = open(f"users.txt", "w")
        file.write(lines + "\n")
        file.close()
        print("\n[+] After Filtering -->", file_lengthy2(f"users.txt"))
        print("+" + "-" * 11 + "Filtering" + "-" * 10 + "+")
        print("[!] All Users Was Saved In [ users.txt ] File")
        out()
        sys.exit()
    best_user_maker()
else:
    print("[-] Choose From Options Pls !!.")
    out()
    sys.exit()
# End Coding \
