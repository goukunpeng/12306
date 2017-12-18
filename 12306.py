# 12306
# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
def getTrainInfo():
    train_year = input("输入你的乘车年份：")
    train_month = input("输入你的乘车月份：")
    train_date = input("输入你的乘车日期：")
    # 出发站、始发站列表：https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9035（用火狐打开）
    url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=" + str(train_year) + "-" + str(train_month) + "-" + str(train_date) + "&leftTicketDTO.from_station=CDW&leftTicketDTO.to_station=RXW&purpose_codes=ADULT"
    # url1 = ["https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-12-28&leftTicketDTO.from_station=CDW&leftTicketDTO.to_station=RXW&purpose_codes=ADULT % (train_year,train_month,train_date)"]
    response = requests.get(url)
    # print(response.status_code)                   # 返回get请求的状态码
    dataJSON = response.json()['data']['result']  # 获取json数据
    length = len(dataJSON)  # 计算dataJSON的列表长度
    # print(length)                                 # 打印长度
    n = 0  # 这个while循环的作用：将dataJSON里的每个元素取出来，组成一个新的列表。length是多少，就有多少个新列表。
    while n < length:  # for循环：组成的新列表里，使用split()函数，将这个list里的一个元素分成多个元素；之后，使用enumerate（）函数给每个元素加索引
        for m, data in enumerate(dataJSON[n].split("|")):  # 这样，就能看到dataJSON[n]里包含的信息，如车次、出发站、始发站、出发时间、各个座位的剩余票数.从而找到需要信息的索引。方便我们后面查询票数
            # print(m,data)
            pass
        tmp_list = dataJSON[n].split('|')  # 测试查找车票信息  需求：有硬座票的车次
        seatnum = input("请输入你想购买的座位\n23 = 软卧\n28 = 硬卧\n29 = 硬座\n26 = 无座\n：")
        # 因为这里的input输入的是str类型，所以后面的判断语句不能判断出如字母之类的str。可能try...except能够通过捕获异常判断出
        if not isinstance(int(seatnum), int):
            print("输入座位有误，请重新查询并输入正确的座位！！！")
        elif int(seatnum) != 23 and int(seatnum) != 28 and int(seatnum) != 29 and int(seatnum) != 26:
            print("输入座位有误，请重新查询并输入正确的座位！！！")
        else:
            seatnum = int(seatnum)
            # print(isinstance(seatnum,int))   #判断seatnum的数据类型,经过Int转换后,为int类型
            if tmp_list[seatnum] != '' and tmp_list[seatnum] != u'无':
                print(tmp_list[3])
            else:
                print("查询不到此座位相应车次，请重新查询")
                return getTrainInfo()
        n += 1
    '''
    车次 = 3
    始发站 = 4
    到达站 = 7
    出发时间 = 8
    到达时间 = 9
    历时 = 10
    出发日期 = 13
    软卧 = 23
    硬卧 = 28
    硬座 = 29
    无座 = 26
    # 测试下，
    # n = 0
    # while n < length  :                #  这里注意：length是20，但dataJSON的索引是从0开始的，即 0 ~ 19 ，总共20.所以这里应该是 n < length
    #     # print(dataJSON[n].split('|'))
    #     print(list(enumerate(dataJSON[n].split('|'))))
    #     n = n + 1

    # print(list(enumerate(dataJSON[2].split('|'))))      #
    # from collections import Iterable                   # 判断 dataJSON[]是迭代器还是可迭代对象。 判断结果为：可迭代对象
    # print(isinstance(dataJSON[2],Iterable))
    '''
getTrainInfo()
req = requests.Session()
def login():
    '''
    通过登录测试
    1.输入正确的账号密码，验证码错误。返回了captcha-check这个，提示result_message:"验证码校验失败",没有login
    2.输入错误的账号密码，验证码错误，返回了captcha-check这个，提示result_message:"验证码校验失败",没有login
    3.输入错误的账号密码，验证码正确，返回了captcha-check这个，提示result_message:"验证码校验成功"  ，login，result_message:"您的手机号码尚未进行核验，目前暂无法用于登录，请您先使用用户名或邮箱登录，然后选择手。。。。。(我输入的是未注册的账号)
    4.输入正确的账号密码，验证码正确，验证码校验成功,有login
    通过上面的分析，我们发现12306登录时，是先验证验证码是否输入正确，在验证账号密码是否正确。所以我们在模拟登录时，首先要获取验证码图片，再输入正确的验证码，再输入账号密码，实现登录
    '''
    # 1.获取验证码图片
    url_img = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.8704234609697796'
    img_response = req.get(url_img)
    # print(img_response.content)
    # print(img_response.status_code)
    '''
    f=open('路径/文件名', '读写格式', '编码方式', '错误处理方式') 
    第二个参数：读文本文件用'r'，读二进制文件用'rb'，写文本文件用'w'，写二进制文件用'wb'，追加文件用'a',第二个参数不写，默认为'r'。
    # http://blog.csdn.net/plychoz/article/details/77337682
    '''
    imgfile = open("check.png", 'wb')
    imgfile.write(img_response.content)  # 写入get请求url_img获得的内容,content是获得bytes，text是str类型
    imgfile.close()
    # 到这里就成功把验证码图片获取到了并写进了check.png这个文件里
    checkInfo = input("请输入验证码坐标：")
    # 2.获取验证码
    urlCaptchaCheck = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
    CaptchaCheck_data = {
        'answer': checkInfo,  # 通过这里，发现输入的验证码是通过坐标判断的。首先在验证码图片上找一个点，点击后，登录获得其验证码坐标，再用截图方式找到坐标原点。再用截图的方式获取验证码的坐标
        'login_site': 'E',
        'rand': 'sjrand'
    }
    CaptchaCheck_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3278.0 Safari/537.36'
    }
    # 注意这里的headers
    '''
    'Accept': 'application / json, text / javascript, * / *; q = 0.01',
    'Accept - Encoding': 'gzip, deflate, br',
    'Accept - Language': 'zh - CN, zh;q = 0.9',
    'Connection': 'keep - alive',
    'Content - Length': '41',
    'Content - Type': 'application / x - www - form - urlencoded;charset = UTF - 8',
    '''
    # 如果添加了上面这些内容，请求状态码为406. 406：请求的资源的内容特性无法满足请求头中的条件，因而无法生成响应实体。HTTP状态码参见：https://baike.baidu.com/item/HTTP%E7%8A%B6%E6%80%81%E7%A0%81/5053660?fr=aladdin#3_3
    # 所以这里，只添加user-agent
    CaptchaCheck_response = req.post(urlCaptchaCheck, data=CaptchaCheck_data, headers=CaptchaCheck_headers)
    # print("post请求验证码验证url的状态码：",CaptchaCheck_response.status_code)  #状态码为200,post请求成功
    # print(CaptchaCheck_response.text)
    # 这里说明一下，使用输入正确的验证码坐标后，提示result_message":"验证码校验失败,信息为空","result_code":"8"
    # 需要使用requests.Session()方法；输正确的验证码后，"result_message":"验证码校验成功","result_code":"4"；这里也说明，当result_code为4时，验证码验证成功
    result = CaptchaCheck_response.json()['result_code']
    # print(isinstance(result,str))               #这里判断出result的数据类型为str
    if int(result) == 4:
        print("验证码验证成功!")
    else:
        print("验证码验证失败，请重新输入验证码!")
        return login()
    # 3.模拟登陆
    username = input('请输入你的用户名：')
    password = input('请输入你的密码：')
    urlLogin = 'https://kyfw.12306.cn/passport/web/login'
    dataLogin = {
        'username': username,
        'password': password,
        'appid': 'otn'
    }
    loginheaders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3278.0 Safari/537.36'}
    login_response = req.post(urlLogin, data=dataLogin, headers=loginheaders)
    # print(login_response.status_code,'\n',login_response.text)
    loginResult = login_response.json()['result_code']
    if int(loginResult) == 0:
        print("登陆成功!")
    else:
        print("登陆失败!请检查您的账号密码是否正确，并重新输入!")
        return login()
login()
# 这里应该没有真正的登陆到12306上。
