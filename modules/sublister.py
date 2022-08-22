import conf.conf as conf

def sublist3r_scan():
    print(
        "===================================================================")
    print(conf.colored(conf.text2art("Sublister Scan", "small"), "cyan"))
    print(
        "===================================================================")
    d = input(conf.colored("\nEnter Domain: ", "green", attrs=["bold"]))
    p = ssl_host = input(conf.colored("\nEnter port: ", "green", attrs=["bold"]))
    conf.os.system(f"sublist3r -d {d} -p {p}")
    conf.sys.exit()
    # print(
    #     "===================================================================")
    # print(conf.colored(conf.text2art("Sublist3r Scan", "small"), "cyan"))
    # print(
    #     "===================================================================")
    # domain = input(conf.colored("\nEnter target: ", "green", attrs=["bold"]))
    # subdomains = conf.sublist3r.main(domain, f'{domain}_subdomains.txt', 40, ports='80', silent=False, verbose=False, enable_bruteforce=False, engines=None)
    # header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36'}

    # new1=[]
    # for a in subdomains:
    #     url = f'http://{a}'
    #     try:
    #         b = conf.requests.get(url,headers=header,timeout=10)
    #         c = b.status_code
    #         d = int(c)
    #         print(d)
    #         if d == 200:
    #             new1.append(a)
    #         else:
    #             del a

    #     except:
    #         continue

    # print(new1)
    # newsubdomains = conf.sublist3r.main(domain, f'{domain}_subdomains.txt', 40, ports='443', silent=False, verbose=False, enable_bruteforce=False, engines=None)
    # new2=[]
    # for e in newsubdomains:
    #     url = f'http://{e}'
    #     try:
    #         f = conf.requests.get(url,headers=header,timeout=10)
    #         g = f.status_code
    #         h = int(g)
    #         print(h)
    #         if h == 200:
    #             new2.append(e)
    #         else:
    #             del e

    #     except:
    #         continue
    # print(new2)
    # # sub_output = conf.dir_output(sub_output, "reports/sublister", new2)
    # # conf.create_dir(sub_output)

    # # conf.os.system(
    # #     f"python3 {conf.home}/.local/share/dirsearch/dirsearch.py -u {new2} --format plain -o {sub_output}/sublister.txt"
    # # )
    # # conf.clear()
    # # conf.sys.exit()
