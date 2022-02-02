from selenium import webdriver
import sys
import time

# settings
id = "*****"
password = "******"
degree1 = "36.2"
degree2 = "36.2"

drive = webdriver.Chrome()
start = time.time()
drive.get('https://mis.uic.edu.cn/survey/login.jsp')
drive.implicitly_wait(30)
drive.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[1]/input[1]").send_keys(id)
drive.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[2]/input").send_keys(password)
drive.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[3]/input").click()
a = drive.find_elements_by_tag_name("tr")
title_list = []
for i in range(1,len(a)):
    title_list.append(a[i].find_elements_by_tag_name("td")[1].text)

switch1 = 0
for j in range(0,len(a)-1):
    if title_list[j].startswith("每天晨午检体温申报"):
        switch1 += 1
        row_number = j+1

if switch1 == 0:
    print("未发现相关打卡要求.")
    drive.close()
    sys.exit(0)
elif switch1 != 1:
    row_number = int(input("相关打卡内容不止一个,请输入所需行序号: "))
else:
    pass

a[row_number].find_elements_by_tag_name("td")[3].find_element_by_tag_name("a").click()

try:
    # 1.本人现在所处什么地方？ *
    if drive.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[2]/div[2]/table/tbody/tr[2]/td/div[1]/strong").text == "1.本人现在所处什么地方？ *":
        print(drive.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[2]/div[2]/table/tbody/tr[2]/td/div[1]/strong").text)
        if drive.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[2]/div[2]/table/tbody/tr[2]/td/div[2]/label").text == "已在UIC住宿":
            print(drive.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[2]/div[2]/table/tbody/tr[2]/td/div[2]/label").text)
            drive.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[2]/div[2]/table/tbody/tr[2]/td/div[2]/label/input").click()

    # 2.本人今天早上的体温为多少度？ *
    if drive.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[2]/div[2]/table/tbody/tr[3]/td/div[1]/strong").text == "2.本人今天早上的体温为多少度？ *":
        print(drive.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[2]/div[2]/table/tbody/tr[3]/td/div[1]/strong").text)
        drive.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[2]/div[2]/table/tbody/tr[3]/td/div[3]/input").send_keys(degree2)

    # 3.本人今天中午的体温为多少度？ *
    if drive.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[2]/div[2]/table/tbody/tr[4]/td/div[1]/strong").text == "3.本人今天中午的体温为多少度？ *":
        print(drive.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[2]/div[2]/table/tbody/tr[4]/td/div[1]/strong").text)
        drive.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[2]/div[2]/table/tbody/tr[4]/td/div[3]/input").send_keys(degree2)

    # 4.本人今天是否有其他异常临床表现？（多选） *[choose: 0 to 4]
    if drive.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[2]/div[2]/table/tbody/tr[5]/td/div[1]/strong").text == "4.本人今天是否有其他异常临床表现？（多选） *[choose: 0 to 4]":
        print(drive.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[2]/div[2]/table/tbody/tr[5]/td/div[1]/strong").text)
        if drive.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[2]/div[2]/table/tbody/tr[5]/td/div[3]/label").text == "无":
            print(drive.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[2]/div[2]/table/tbody/tr[5]/td/div[3]/label").text)
            drive.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[2]/div[2]/table/tbody/tr[5]/td/div[3]/label/input").click()

    drive.find_element_by_xpath("/html/body/div/div/div/div[2]/div/form/div[2]/div[2]/table/tbody/tr[7]/td/button").click()
    drive.find_element_by_xpath("/html/body/div/div/div/div[2]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/a[2]").click()
    drive.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[2]/ul/li[2]/a").click()
    print("打卡成功")
except:
    print("打卡失败")
end = time.time()

input("duration: %.2f s, ENTER for leave" % (end-start))
drive.close()
