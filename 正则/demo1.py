import re


def main(email):
    res = re.match(r"^[0-9a-zA-Z]{4,20}@163\.com$",email)
    if res:
        print("%s 是163邮箱" % email)
    else:
        print("%s 不是163邮箱" % email)


if __name__ == "__main__":
    emial_name = "fdsdsf@163.com"
    main(emial_name)