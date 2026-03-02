print("Phishing Detector Started 🎣")

url = input("Enter URL: ")

if "@" in url:
    print("⚠ Suspicious: Contains @ symbol")
elif url.startswith("http://"):
    print("⚠ Warning: Not secure (No HTTPS)")
elif url.count("-") > 3:
    print("⚠ Suspicious: Too many hyphens")
elif any(char.isdigit() for char in url):
    print("⚠ Check carefully: Contains numbers")
else:
    print("✅ URL looks safer (Manual check recommended)")