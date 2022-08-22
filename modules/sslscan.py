import conf.conf as conf

def ssl_scan():
    print(
        "===================================================================")
    print(conf.colored(conf.text2art("SSL Scan", "small"), "cyan"))
    print(
        "===================================================================")

    ssl_host = input(conf.colored("\nEnter target: ", "green", attrs=["bold"]))
    conf.os.system(f"sslscan {ssl_host}")
    conf.sys.exit()