import pyshorteners as p
link=input("Enter the url")
short=p.Shortener()
x=short.tinyurl.short(link)
print(x)