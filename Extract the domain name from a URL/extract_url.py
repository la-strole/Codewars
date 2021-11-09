def domain_name(url):
    url = url.replace('www.','')
    url = url.split('.')[0]
    return url.split('//')[-1]

if __name__ == "__main__":
    test_url = "http://github.com/carbonfive/raygun"
    print(f"domain name form url {test_url} is {domain_name(test_url)}")
