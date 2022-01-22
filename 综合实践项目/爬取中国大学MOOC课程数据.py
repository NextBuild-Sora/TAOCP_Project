#**********************************
# 爬取中国大学 MOOC 课程数据
#**********************************


from selenium import webdriver
#from selenium.webdriver.chrome.options import Options

try:
    '''
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome = webdriver.Chrome(chrome_options= chrome_options)
    '''

    # 指定chrome.exe绝对路径。设置binary_location属性:
    options = webdriver.ChromeOptions()
    options.binary_location = r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
    chrome = webdriver.Chrome(options=options)

    chrome.get( "https://www.icourse163.org/search.htm?search=python#" )

    mdiv = chrome.find_element_by_id( "j-courseCardListBox" )
    divs = mdiv.find_elements_by_xpath(".//div[@data-action='课程点击']")
    for div in divs:
        course = div.find_element_by_xpath(".//span[@class=' u-course-name f-thide']").text

        d = div.find_element_by_xpath( ".//div[@class='t2 f-fc3 f-nowrp f-f0']" )
        links = d.find_elements_by_xpath(".//a")
        college = links[0].text
        if len(links) >= 2:
            teacher = links[1].text
        else:
            teacher= ""

        team =teacher
        try:
            team += d.find_elements_by_xpath(".//span").text
        except:
            pass

        count = div.find_element_by_xpath(".//span[@class='hot']").text
        process = div.find_element_by_xpath(".//span[@class='txt']").text
        brief = div.find_element_by_xpath(".//span[@class='p5 brief f-ib f-f0 f-cb']").text
        print(course, college, teacher, team, count, process, brief)

    chrome.close()

except Exception as err:
    print("爬取错误：", err)




