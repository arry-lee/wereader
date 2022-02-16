from cookie import read_cookie_from_path
from wereader import get_bestbookmarks, get_bookmarklist, get_bookshelf, get_chapters

cookies = read_cookie_from_path("cache/Cookies")

FMT = "md"
FLAG = True
TEST = False
CURRENT = None
INFO = """
    -----------------------------------------------------
    -             请选择您想要执行的操作：
    -             1. 查看书架
    -             2. 搜索书架书籍
    -             3. 选择当前书籍
    -             4. 查看当前书籍目录
    -             5. 查看当前书籍热门划线
    -             6. 导出当前书籍热门划线
    -             7. 查看当前书籍笔记
    -             8. 导出当前书籍笔记
    -             0. 退出
    -             help. 打印提示信息
    -----------------------------------------------------
"""


def check_current(func):
    global CURRENT

    def wrapper():
        if CURRENT:
            func()
        else:
            print("请先选择当前要操作的书籍")

    return wrapper


def show_shelf():
    print("您的书架如下:")
    for b in books:
        print(b.bookId, b.title, b.author)


def search_book():
    global CURRENT

    query = input("请输入关键字：")
    result = []
    for b in books:
        if query in b.title or query in b.author:
            result.append(b)

    [print(i, " ".join((b.bookId, b.title, b.author))) for i, b in enumerate(result)]

    select = input("选择您想要作为当前书籍的序号（空为不选择）：")
    if select:
        select = int(select)
        if 0 <= select < len(result):
            CURRENT = result[select]


def choose_current():
    global CURRENT

    bid = input("请输入当前选书籍的ID：")
    choosed_list = [x for x in books if x.bookId == bid]
    CURRENT = choosed_list.pop() if choosed_list else None

    if not CURRENT:
        print("没有找到书籍的ID，请确认后重试。")
        return

    print(f"已选择书籍《{CURRENT.title}》作为当前书籍。")


@check_current
def see_content():
    global CURRENT

    bid = CURRENT.bookId
    for c in get_chapters(int(bid), cookies=cookies):
        print("#" * c[0], c[1])


@check_current
def see_popular():
    global CURRENT

    bid = CURRENT.bookId
    bb = get_bestbookmarks(bid, cookies=cookies)
    print(bb)


@check_current
def export_popular():
    global CURRENT

    bid = CURRENT.bookId
    bb = get_bestbookmarks(bid, cookies=cookies)
    with open(f"{CURRENT.title}-{CURRENT.bookId}-热门划线.{FMT}", "w") as f:
        f.write(bb)
    print("导出成功")


@check_current
def see_mine():
    global CURRENT

    bid = CURRENT.bookId
    bb = get_bookmarklist(bid, cookies=cookies)
    print(bb)


@check_current
def export_mine():
    global CURRENT

    bid = CURRENT.bookId
    bb = get_bookmarklist(bid, cookies=cookies)
    with open(f"{CURRENT.title}-{CURRENT.bookId}.{FMT}", "w") as f:
        f.write(bb)
    print("导出成功")


def leave():
    global FLAG
    FLAG = False


def help_info():
    print(INFO)


func_map = {
    "1": show_shelf,
    "2": search_book,
    "3": choose_current,
    "4": see_content,
    "5": see_popular,
    "6": export_popular,
    "7": see_mine,
    "8": export_mine,
    "0": leave,
    "help": help_info,
}


def main():
    print("欢迎使用微信读书爬虫")

    try:
        global books
        books = get_bookshelf(cookies)
    except Exception as e:
        print(e)
        print("获取书架失败，请重新运行client.py 扫码登录")
        return
    print(INFO)

    while FLAG:
        operation = input(">>> ").lower()
        func_map.get(operation, lambda: print("非法的选择"))()


if __name__ == "__main__":
    main()
