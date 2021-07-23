class Date:

    @classmethod
    def day_month_year(cls, date):
        print(*map(int, (date.split('-'))))

    @staticmethod
    def valid_date(date):
        if int(date.split('-')[0]) in range(0, 32) and int(date.split('-')[1]) in range(0, 13):
            print('Дата введена верно')
        else:
            print('Некорректные данные')


Date.day_month_year(r'20-12-2020')
Date.valid_date(r'20-10-2020')
Date.valid_date(r'20-14-2020')
