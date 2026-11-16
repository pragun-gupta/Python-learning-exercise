urls = ["https://a.co","http:what-the-hell456","http://paypa1-secure-login.com/verify?id=88213"]

for url in urls:
    print(url)
    digit_count = 0
    for ch in url:
        if ch.isdigit():
            digit_count+=1
    print(f"Length: {len(url)}")
    print(f"Digits: {digit_count}")

    print("@ is present? ",'@' in url )
    print("- is present? ",'-' in url )
    print(":// is present? ",'://' in url )
    print("URL starts with https?", url.lower().startswith('https'))
    print("Number of dots present in the URL ", url.count('.') )
