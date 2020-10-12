import function # import(불러오기)를 할 수 있는 것은 단 두 개 (함수 또는 클래스)
                # 그러나 파일자체를 불러오면 잠정적으로 클래스로 인식하여 파일 내에 있는 모든 함수 사용 가능
# print("="*100)
# function.sum()
# function.print_info(name="Ivy", age=37)

import time
# while True:
#     function.sum()
#     function.print_info(name="Cherry", age=28)
#     time.sleep(2)
#     break

import schedule
def job():
    print("I'm working...")

schedule.every(5).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
