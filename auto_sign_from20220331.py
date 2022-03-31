from selenium import webdriver
import sys

# settings
id = "n830026070"
password = "fairy013LYH"
key_words = ["都没有", "以下", "健康", "珠海"]
key_words2= [ "不含"]
def if_in(string):
    a = [i in string for i in key_words]
    b = [i in string for i in key_words2]
    if (True in a) and (True not in b):
        return True
    else:
        return False


drive = webdriver.Chrome("./chromedriver")
drive.get('https://mis.uic.edu.cn/survey/login.jsp')
drive.implicitly_wait(30)
drive.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[1]/input[1]").send_keys(id)
drive.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[2]/input").send_keys(password)
drive.find_element_by_xpath("/html/body/div/div/div/div[2]/form/div[3]/input").click()
drive.implicitly_wait(30)

def sign(html):
    # title = tr.find_elements_by_tag_name("td")[1].text
    # html = tr.find_elements_by_tag_name("td")[3].find_element_by_xpath("./a").get_attribute("href")
    # print("For %s"%title)
    drive.get(html)
    label_list = drive.find_elements_by_tag_name("label")
    label = [{"input": i.find_element_by_xpath("./input"), "text": i.text} for i in label_list]
    for i in label:
        if if_in(i["text"]):
            i["input"].click()
    input("check the anwser, input anything to comfirm:")
    x = drive.find_elements_by_tag_name("button")[1]
    x.click()


all_tr = drive.find_elements_by_tag_name("tr")
need_sign_tr = []
title_list = []
html_list = []
for i in range(1,len(all_tr)):
    title_text = all_tr[i].find_elements_by_tag_name("td")[1].text
    if title_text.startswith("每天健康申报"):
        title_list.append(title_text)
        html_list.append(all_tr[i].find_elements_by_tag_name("td")[3].find_element_by_xpath("./a").get_attribute("href"))
        need_sign_tr.append(all_tr[i])

if len(need_sign_tr) == 0:
    print("未发现相关打卡要求.")
    drive.close()
    sys.exit(0)
else:
    print("发现%d个打卡要求:"%len(title_list))
    for i in title_list:
        print(i)
    print("---------------------------------------------------")

for i in html_list:
    sign(i)

print("finished!!")
drive.close()