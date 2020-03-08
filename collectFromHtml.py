from bs4 import BeautifulSoup
import sys

# 通过将打开想法的页面保存到本地解析，是接口被改动后的无奈选择


def collectBookMarks(html):
    file = open(html, encoding="utf-8")
    soup = BeautifulSoup(file, features='html.parser')
    readerNoteList = soup.find("div", {"class": "readerNoteList"})
    for sectionListItem in readerNoteList.children:
        if sectionListItem is None:
            continue
        sectionListItem_title = sectionListItem.find(
            "div", {"class": "sectionListItem_title"})
        if sectionListItem_title is not None:
            print("### " + sectionListItem_title.text)

        text = sectionListItem.find("div", {"class": "text"})
        abstract = sectionListItem.find("div", {"class": "abstract"})
        # abstract 有值得时候代表有想法，且此时abstract是笔记
        biji = None
        xiangfa = None
        if abstract is not None:
            biji = abstract.text
            # print("- " + )
        if text is not None:
            if biji is not None:
                xiangfa = text.text
            else:
                biji = text.text
        if xiangfa is not None:
            print("- " + biji, end="")
            print("*【" + xiangfa + "】*")
        else:
            print("- " + biji)


if __name__ == "__main__":
    # 保存本地html位置
    html = "a.html"
    # 输出书签位置
    filename = "1.md"
    output = sys.stdout
    outputfile = open(filename, 'w')
    sys.stdout = outputfile
    # 上下都是为了重定向输出到文件
    collectBookMarks(html)

    outputfile.close()
    sys.stdout = output
