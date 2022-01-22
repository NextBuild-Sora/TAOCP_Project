#*********************************************
#
# 2、服务器程序
#
#*********************************************


import flask

app=flask.Flask(__name__, static_folder="images")

@app.route("/")
def show():
    pageRowCount = 3
    rowItemCount = 4
    if "pageIndex" in flask.request.values:
        pageIndex = int(flask.request.values.get("pageIndex"))
    else:
        pageIndex = 1
    startRow = (pageIndex-1)*pageRowCount*rowItemCount
    endRow = pageIndex*pageRowCount*rowItemCount
    phones = []
    try:
        fobj = open("phones.csv", "r", encoding= "utf-8")
        rows = fobj.readlines()
        count = 0
        for row in rows:
            if row.strip().strip("\n") != "":
                count = count + 1
        pageCount = count // (pageRowCount*rowItemCount)
        if count % (pageRowCount*rowItemCount) != 0:
            pageCount += 1
        rowIndex = 0
        for i in range(1, count):
            row = rows[i]
            if rowIndex >= startRow and rowIndex < endRow:
                row = row.strip().strip("\n")
                s = row.split(",")
                phones.append({"no":s[0], "mark":s[1], "price":s[2], "note":s[3], "inage":s[4]})
            rowIndex += 1
        fobj.close()
    except Exception as err:
        print("错误：", err)

    return flask.render_template("phone.html", phones = phones, rowltemCount = rowItemCount, numbers = len(phones), pageIndex = pageIndex, pageCount = pageCount)

app.run()



