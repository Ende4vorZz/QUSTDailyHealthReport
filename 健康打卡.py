# @Author : Kevin @Date : 2022-8-26

import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    # 请填写 basc_data 与 login_data 中的信息
    basc_data = {
        "姓名": "",  # 姓名
        "学号": "",  # 学号
        "学院": "",  # 学院
        "班级": "",  # 班级
        "专业": "",  # 专业
        "年级": "",  # 年级
        "手机号": "",  # 手机号
        "学院代码": "",  # 学院代码
        "专业代码": "",  # 专业代码
        "班级代码": "",  # 班级代码
        "当前所在地": "",  # 当前所在地址
    }
    login_data = {
        # 健康信息数据录入
        "账号": "",
        "密码": ""
    }

    sent(basc_data, login_data)


def getDateTime():
    # 时间格式 2022-08-25+00:42:18
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    date_time = time.strftime("%Y-%m-%d")
    # print(currentTime, dateTime)
    return current_time, date_time  # 返回值为元组


def getResult(request):
    response = request
    result = ""
    try:
        response = response.json()
        result = response['message']
    except KeyError:
        result = response['errors']
    except requests.exceptions.JSONDecodeError:
        pass
    finally:
        code = request.status_code
        print(result, code)
        if code == 200 and result == '保存表单数据成功!':
            print("打卡成功!")
        else:
            print("打卡失败!")


def getData(basc_data):
    date_time = getDateTime()
    user_data = {
        # ======请填写以下数据========
        "m:xsjkdk:xm": basc_data["姓名"],  # 姓名
        "m:xsjkdk:xh": basc_data["学号"],  # 学号
        "m:xsjkdk:xy": basc_data["学院"],  # 学院
        "m:xsjkdk:bj": basc_data["班级"],  # 班级
        "m:xsjkdk:zy": basc_data["专业"],  # 专业
        "m:xsjkdk:nj": basc_data["年级"],  # 年级
        "m:xsjkdk:sjh": basc_data["手机号"],  # 手机号
        "m:xsjkdk:tjsj": date_time[0],  # 提交时间
        "m:xsjkdk:jssj": date_time[0],  # 结束时间
        "m:xsjkdk:xydm": basc_data["学院代码"],  # 学院代码
        "m:xsjkdk:zydm": basc_data["专业代码"],  # 专业代码
        "m:xsjkdk:bjdm": basc_data["班级代码"],  # 班级代码
        "m:xsjkdk:dqszdz": basc_data["当前所在地"],  # 当前所在地址
        # =======以下内容无需修改========
        "m:xsjkdk:jrtw": "37.2℃及以下",  # 今日体温
        "m:xsjkdk:jrstzk": "健康",  # 今日身体状况
        "m:xsjkdk:stzkqt": "",  # 身体特殊情况
        "m:xsjkdk:gfxqyjcs": "否",  # 高风险区域接触史
        "m:xsjkdk:ysbrjcs": "否",  # 疑似病人接触史
        "m:xsjkdk:ysbl": "否",  # 疑似病例
        "m:xsjkdk:yxgl": "否",  # 医学隔离
        "m:xsjkdk:jkmys": "绿色",  # 健康码颜色
        "m:xsjkdk:nlqsfybb": "未离青",  # 你离青是否报备
        "m:xsjkdk:nsfyjzxgym": "已接种第3针（加强针）",  # 你是否已接种新冠疫苗
        "m:xsjkdk:nzhychsjcsj": date_time[1],  # 你最后一次核酸检测时间
        "m:xsjkdk:brcn": "是",  # 本人承诺
        "pkField": "",
        "tableId": "2000000000030000",
        "alias": "xsjkdk",
        "tableName": "xsjkdk"
    }

    data_form = "{'main':{'fields':{ \
                    'xm':'" + user_data["m:xsjkdk:xm"] + "',\
                    'xh':'" + user_data["m:xsjkdk:xh"] + "',\
                    'xy':'" + user_data["m:xsjkdk:xy"] + "',\
                    'bj':'" + user_data["m:xsjkdk:bj"] + "',\
                    'zy':'" + user_data["m:xsjkdk:zy"] + "',\
                    'nj':'" + user_data["m:xsjkdk:nj"] + "', \
                    'sjh':'" + user_data["m:xsjkdk:sjh"] + "', \
                    'tjsj':'" + user_data["m:xsjkdk:tjsj"] + "', \
                    'jssj':'" + user_data["m:xsjkdk:jssj"] + "', \
                    'xydm':'" + user_data["m:xsjkdk:xydm"] + "', \
                    'zydm':'" + user_data["m:xsjkdk:zydm"] + "', \
                    'bjdm':'" + user_data["m:xsjkdk:bjdm"] + "', \
                    'dqszdz':'" + user_data["m:xsjkdk:dqszdz"] + "', \
                    'stzkqt':'', \
                    'nzhychsjcsj':'" + user_data["m:xsjkdk:nzhychsjcsj"] + "', \
                    'jrtw':'" + user_data["m:xsjkdk:jrtw"] + "', \
                    'jrstzk':'" + user_data["m:xsjkdk:jrstzk"] + "', \
                    'gfxqyjcs':'" + user_data["m:xsjkdk:gfxqyjcs"] + "', \
                    'ysbrjcs':'" + user_data["m:xsjkdk:ysbrjcs"] + "', \
                    'ysbl':'" + user_data["m:xsjkdk:ysbl"] + "', \
                    'jkmys':'" + user_data["m:xsjkdk:jkmys"] + "', \
                    'lqsfybb':'" + user_data["m:xsjkdk:nlqsfybb"] + "', \
                    'nsfyjzxgym':'" + user_data["m:xsjkdk:nsfyjzxgym"] + "' , \
                    'brcn':'是', \
                    }},'sub':[],'opinion':[]}"

    data_form = data_form.replace("'", '"')
    # print(data_form)
    user_data.update(formData=data_form)
    # print(user_data)
    return user_data


def getCookie(login_data):
    url = "https://bpm.qust.edu.cn/bpmx/platform/form/bpmDataTemplate/editData_xsjkdk.ht?type=WeiXinGzhClient&ticket=ST-1615986-399FSbsirwW5UIGGYZJ2-zfsoft.com"
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Firefox(options=options)
    # 登录信息录入 学号 密码

    driver.get(url)
    time.sleep(0.5)

    driver.find_element(by=By.ID, value='username').send_keys(login_data["账号"])
    driver.find_element(by=By.ID, value='ppassword').send_keys(login_data["密码"])
    driver.find_element(by=By.ID, value='dl').click()
    time.sleep(0.5)

    cookie_list = driver.get_cookies()
    # print(cookie_list)
    time.sleep(0.5)
    # 处理 cookie 数据
    cookie = [item['name'] + '=' + item['value'] for item in cookie_list]
    cookie_str = '; '.join(item for item in cookie)
    print(cookie_str)

    driver.quit()
    return cookie_str


def sent(basc_data, login_data):
    post_url = "https://bpm.qust.edu.cn/bpmx/platform/form/bpmFormHandler/save.ht"
    #########################################################
    print("正在执行打卡操作...")
    date_time = getDateTime()
    cookie = getCookie(login_data)
    post_head = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        "Content-Length": "2909",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "bpm.qust.edu.cn",
        "Origin": "https://bpm.qust.edu.cn",
        "Cookie": cookie,
        "Referer": "https://bpm.qust.edu.cn/bpmx/platform/form/bpmDataTemplate/editData_xsjkdk.ht?type=WeiXinGzhClient&ticket=ST-1615986-399FSbsirwW5UIGGYZJ2-zfsoft.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
        "X-Requested-With": "XMLHttpRequest"
    }
    post_data = getData(basc_data)
    res = requests.post(post_url, headers=post_head, data=post_data, verify=False)
    # print(head)
    ########################################################
    getResult(res)


if __name__ == '__main__':
    main()
