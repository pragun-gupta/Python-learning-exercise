urls = [
    "https://a.co",
    "http://what-the-hell456.com",
    "http://paypa1-secure-login.com/verify?id=88213",
    "https://www.wikipedia.org",
    "https://github.com/pragun-gupta",
    "https://www.python.org/downloads/",
    "http://192.168.0.1/login.php",
    "https://user@free-gift-cards.net/claim",
    "http://amaz0n-support-help.com/signin?session=9f3a7c21",
    "http://www.google.com.account-security-check.info/verify",
]

results=[]
for url in urls:
    digit_count = 0
    for ch in url:
        if ch.isdigit():
            digit_count+=1
    results.append({"URLS": url,"Length":len(url),"Digits":digit_count,"has_@":'@' in url,"has_hyphen":'-' in url,"has_://":'://' in url,"https": url.lower().startswith('https'), "dots": url.count('.') })


for r in results:
    print(f"URL : {r['URLS']}")
    print(f"Length: {r['Length']}")
    print(f"Digits: {r['Digits']}")

    print(f"@ is present?  {r['has_@']}")
    print(f"- is present?  {r['has_hyphen']}")
    print(f":// is present?  {r['has_://']}")
    print(f"URL starts with https? {r['https']}")
    print(f"Number of dots present in the URL {r['dots']}" )
         
