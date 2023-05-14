"""
签到
"""
from libs.info import infos
from libs.source import ZWYT

if __name__ == '__main__':
    for stu in infos:
        try:
            yy = ZWYT(stu['name'], stu['sno'], stu['pwd'])
            yy.sign(stu['devName'])  # 签到
        except Exception as e:
            print(e)
            continue
