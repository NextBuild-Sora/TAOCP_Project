
#3.3 表单 checkbox
# 3.4.2
#测试文件


def getClassList():
    cList = []
    
    # f = open("D:\ProgramData\PyCharm_Community_Edition\
    # PyCharm-Community-2020\Python网络爬虫程序技术\
    # 附录C3_Django_表单_forms\
    # Django_demo_C3\classList.txt", \
    # "rt", encoding= "utf-8")

    f = open("classList.txt", "rt", encoding= "utf-8")
    rows = f.readlines()
    for row in rows:
        s = row.strip()
        if s != "":
            cList.append(s)
    f.close()

    return cList


print(getClassList())


