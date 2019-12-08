from wereader import get_bookshelf,get_chapters,get_bookmarklist,get_bestbookmarks

def main():
    print('欢迎使用微信读书爬虫')
    try:
        books = get_bookshelf()
    except:
        print('请检查您的Cookie设置')
        return
    print('您的书架如下:')
    for b in books:
        print(b.bookId,b.title,b.author)

    while True:
        bid = input('想看哪本书的目录，请输入对应书籍id:')

        for c in get_chapters(int(bid)):
            print('#'*c[0],c[1])

        y =  input('是否需要查看该书的热门划线，y/n?')
        if y.lower() == 'y':
            bb = get_bestbookmarks(bid)
            print(bb)

        y =  input('是否需要查看你的笔记，y/n?')
        if y.lower() == 'y':
            bb = get_bookmarklist(bid)
            print(bb)

        y = input('是否需要查看其他书，y/n?')

        if y.lower() == 'y':
            continue
        else:
            print('bye~')
            break

main()
    