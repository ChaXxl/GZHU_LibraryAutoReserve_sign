"""
签到
"""

import argparse

from libs.info import infos
from libs.source import ZWYT, ReturnCode, load_cookie_cache, save_cookie_cache


def main():

    parser = argparse.ArgumentParser(
        prog = 'sign.py',
        description = 'GZHU图书馆签到脚本',
    )
    
    # 指定需要签到的用户昵称及其cookie对, 格式为name:cookie
    # 不指定则默认签到info中的所有用户, 另外cookie项可忽略. 
    # 例如：python sign.py 猪猪侠:cookie1 皮卡丘:cookie2 熊猫
    parser.add_argument('name_cookie_pairs', nargs = '*')

    # 指定使用缓存ic-cookie的文件, 不指定则不使用cookie缓存, 
    # 缓存cookie的文件名默认为cookie_cache
    # 脚本优先使用命令行中提供的cookie, 没有提供则使用缓存的cookie文件
    # 如果命令行没有提供cookie, 也没有缓存的cookie文件, 或者cookie错误或过期, 则尝试直接登录
    parser.add_argument('-c', '--cookie', nargs = '?', const = 'cookie_cache', default = None, required = False)

    args = parser.parse_args()

    target_infos = []
    
    if args.name_cookie_pairs:
        targets = dict()
        for pair in args.name_cookie_pairs:
            pair = pair.split(':', 1)
            targets[pair[0]] = pair[1] if len(pair) == 2 else None  

        for stu in infos:
            name = stu['name']
            if name in targets:
                # cookie is appointed by command line
                if targets[name] is not None:
                    stu['cookie'] = targets[name]
                target_infos.append(stu)
    else:
        target_infos = infos

    cookie_dirty = False
    external_cookies = {}
    if args.cookie is not None:
        external_cookies = load_cookie_cache(args.cookie)

    # 遍历 target_infos 信息，获取每个用户的昵称、预约座位号、用户名、密码、时间段、推送token（推送可以为空）
    for stu in target_infos:
        name = stu['name']
        cookie = stu.get('cookie', external_cookies.get(name, ''))
        try:
            # 初初始化类示例，传入昵称、用户名、密码、时间段、推送token（推送可以为空）
            yy = ZWYT(name, stu['sno'], stu['pwd'], stu['periods'], stu['pushplus'], cookie = cookie)


            # 尝试签到的次数, 不应该少于2次, 因为如果cookie过期则会导致签到失败, 需要重新登录
            retc = ReturnCode.SUCCESS
            for _ in range(2):
                # 登录, 如果cookie已存在则会跳过
                retc = yy.login(force_login = retc == ReturnCode.COOKIE_EXPIRED)
                if retc == ReturnCode.SUCCESS: 
                    # 更新cookie
                    external_cookies[name] = yy.cookies['ic-cookie']
                    cookie_dirty = True
                elif retc == ReturnCode.GET_LOGIN_URL_FAILED:
                    if stu['pushplus']:
                        yy.pushplus(f"{name} {stu['devName']} 登录失败", "获取登录链接失败")
                    break

                # 签到
                retc = yy.sign_for_ahead_reservation()
                if retc in (ReturnCode.SUCCESS, ReturnCode.ALREADY_SIGNED, ReturnCode.NO_RESERVATION):
                    break


        except Exception as e:
            print(e)
            if stu['pushplus']:
                yy.pushplus(f"{name} {stu['devName']} 签到失败", e)
            continue
    
    if args.cookie and cookie_dirty:
        save_cookie_cache(args.cookie, external_cookies)

if __name__ == '__main__':
    exit(main())
