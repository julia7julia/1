def get_req (req):
    if "плат" in req:
        pay()
    elif 'расп' in req:
        schedule()
    elif 'трен' in req:
        trainer_info()
    elif 'сбор':
        train()
    elif 'групп':
        team()

def schedule():
    print('расписание занятий')
def pay():
    print('сумма к оплате')
def trainer_info():
    print('контакты тренера')
def train():
    print('информация по сборам')
def team():
    print('группа спортсмена')
