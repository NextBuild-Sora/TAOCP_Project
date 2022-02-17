
# ----------------------- 第三方库自动安装脚本 ---------------------- #


'''

    第三方库自动安装脚本：
    - 需求：批量安装第三方库需要人工干预，能否自动安装？ 
    - 自动执行pip逐一根据安装需求安装 
                如何自动执行一个程序？例如：pip？

# ****************************************************************************** #

    ---- 库名 --------------- 用途 --------------------- 安装命令 ----

    NumPy           N维数据表示和运算:              pip install matplotlib
    Matplotlib      二维数据可视化 ：               pip install pillow
    PIL             图像处理：                      pip install numpy
    Scikit-Learn    机器学习和数据挖掘 ：           pip install sklearn

    Requests        HTTP协议访问及网络爬虫：        pip install requests
    Beautiful Soup  HTML和XML解析器                pip install beautifulsoup4
    Wheel           Python第三方库文件打包工具      pip install wheel
    Django          Python最流行的Web开发框架       pip install django

    Flask            轻量级Web开发框架              pip install flask
    WeRoBot         微信机器人开发框架              pip install werobot
    SymPy           数学符号计算工具                pip install sympy
    Pandas          高效数据分析和计算              pip install pandas
    Networkx        复杂网络和图结构的建模和分析     pip install networkx

    PyQt5 用途      基于Qt的专业级GUI开发框架        pip install pyqt5
    PyOpenGL        多平台OpenGL开发接口            pip install pyopengl
    PyPDF2          PDF文件内容提取及处理           pip install pypdf2
    PyGame          简单小游戏开发框架              pip install docopt
    docopt          Python命令行解析               pip install pygame


# ******************************************************************************** #


'''


import os 
libs = { "numpy","matplotlib","pillow","sklearn","requests", \
        "beautifulsoup4","wheel","networkx","sympy", \
        "django","flask","werobot","pyqt5", \
        "pandas","pyopengl","pypdf2","docopt","pygame" }

try:
    for lib in libs:
        os.system( "python -m pip install " + lib )
    print ( " 安装成功（Successful）： " , lib )
except:
    print ( " 不知何故失败了（Failed Somehow.） " )


