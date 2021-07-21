import os


if not os.path.exists("cookie"):
    with open("cookie", "w") as f:
        pass


with open("cookie") as f:
    COOKIE = f.read()

if not COOKIE:
    COOKIE = input("请输入有效Cookie:")
    with open("cookie", 'w') as f:
        f.write(COOKIE)


for c in COOKIE.split(';'):
    try:
        k, v = c.strip().split('=')
    except ValueError:
        continue
    if k == 'wr_vid':
        break


USERVID = int(v)
