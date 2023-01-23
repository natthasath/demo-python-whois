import whois
data = input("Enter Domain: ")
domain = whois.whois(data)
domain.expiration_date
domain.text

print(domain)