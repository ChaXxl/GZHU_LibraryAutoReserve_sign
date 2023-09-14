infos = [
    {
        'sno': '*****',  # 学号
        'pwd': '*****',  # 密码
        'devName': '301-012',  # 预约的座位号（不足3位数的要补零）
        'name': '猪猪侠',       # 随便起个名字
        'periods': (               # 预约时间段（注意中英文符号，每段时间不能超过4小时）
            ('8:30:00', '12:30:00'), 
            ('13:30:00', '17:30:00'), 
            ('18:30:00', '22:15:00')
        ),
        'pushplus': '',         # pushplus的token（不知道这是什么的就留空就好了）
        'appAccNo': ''         # 空着, 暂时不用
    },
    
    ##################################################################
    ## 如果只是一个人预约座位，不需要帮别人预约签到，则可把下面三个字典注释/删除
    ##################################################################
    {
        'sno': '******',        # 学号
        'pwd': '******',        # 密码
        'devName': 'G101-008',   # 预约的座位号---桂花岗（不足3位数的要补零）
        'name': '皮卡丘',         # 随便起个名字
        'periods': (               # 预约时间段（注意中英文符号，每段时间不能超过4小时）
            ('8:30:00', '12:30:00'), 
            ('12:30:00', '16:30:00'), 
            ('16:30:00', '20:30:00'), 
            ('20:30:00', '21:45:00')
        ),
        'pushplus': '',         # pushplus的token（不知道这是什么的就留空就好了）
        'appAccNo': ''           # 空着, 暂时不用
    },
    {
        'sno': '******',        # 学号
        'pwd': '******',        # 密码
        'devName': '3c-016',    # 预约的座位号（不足3位数的要补零）
        'name': '熊猫',           # 随便起个名字
        'periods': (               # 预约时间段（注意中英文符号，每段时间不能超过4小时）
            ('8:30:00', '12:30:00'), 
            ('12:30:00', '16:30:00'), 
            ('16:30:00', '20:30:00'), 
            ('20:30:00', '21:45:00')
        ),
        'pushplus': '',         # pushplus的token（不知道这是什么的就留空就好了）
        'appAccNo': ''           # 空着, 暂时不用
    },
    {
        'sno': '******',        # 学号
        'pwd': '******',        # 密码
        'devName': 'M301-001',    # 琴房预约示例（不足3位数的要补零）
        'name': '小白',           # 随便起个名字
        'periods': (               # 预约时间段（注意中英文符号，每段时间不能超过4小时）
            ('8:30:00', '12:30:00'), 
            ('12:30:00', '16:30:00'), 
            ('16:30:00', '20:30:00'), 
            ('20:30:00', '21:45:00')
        ),
        'pushplus': '',         # pushplus的token（不知道这是什么的就留空就好了）
        'appAccNo': ''           # 空着, 暂时不用
    },
]
