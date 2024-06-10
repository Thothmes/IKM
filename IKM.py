"""  «Хитрый купец» Два купца отправились торговать за море. Каждый из них 
повез по N одинаковых тюков с товаром. В пути корабль попал в шторм и дал 
течь. Чтобы корабль не затонул, капитан приказал поднять весь груз на палубу 
корабля,  расставить  его  вдоль  бортов  по  периметру  и  выбросить  за  борт 
половину груза. Груз выбрасывается по следующему правилу:  
•  каждый тюк получает порядковый номер (+), начиная с тюка, стоящего на 
носу корабля;  (-)
•  их нумерация осуществляется по часовой стрелке;  (-)
•  номер  первого  выброшенного  тюка  соответствует  текущему  числу 
месяца M;  (+)
•  через  K  тюков  следующий  тюк  с  товаром  выбрасывается.  Один  из 
купцов прознал про это правило. Как необходимо расставить ему груз, 
чтобы ни один из его тюков не был выброшен? (+)
Использовать циклический однонаправленный список. 
 """


class Cargo_Box: # Класс тюков. Объект имеет след. атрибуты: номер, и указатель на след. тюк  (если обходится без указателя на следующий тюк, то можно вообще не создавать этот класс, а это меняет вс. структуру программы)

    def __init__(self):
        self.number = None
        self.next = None


class LinkedList: # Класс связанного, одноправленного списка

    def __init__(self):
        self.head = None
        self.firts_el = None
        self.previous = None

    def adding_cargo_box(self, RuleData): # Метод добавления в список объекта класса Cargo_Box
        for i in range(RuleData.quanity*2):
            new_box = Cargo_Box()
            new_box.number = i+1
            #print(new_box, new_box.number)
            if i == 0:
                #print('first')
                self.first_el = new_box
                self.head = new_box
            elif i+1 == RuleData.quanity*2:
                #print('last')
                #print(new_box, self.first_el, new_box.next)
                self.head.next = new_box
                new_box.next = self.first_el
                self.head = self.first_el
                #print(new_box, self.first_el, new_box.next, self.head)
            else:
                #print('medium')
                #print(self.head, new_box)
                self.head.next = new_box
                #print(self.head, self.head.next)
                self.head = new_box

    def removing_cargo_box(self, RuleData): # Метод удаления в список объекта класса Cargo_Box
        check = 0; self.head = self.first_el
        while self.head.number != RuleData.day:
            self.head = self.head.next
        indentation_control = 0
        while check != RuleData.quanity:
            if indentation_control == 0:
                #print ('Удаление')
                if self.head == self.first_el:
                    self.first_el = self.first_el.next
                current_box = self.head
                while current_box.next != self.head:
                    current_box = current_box.next
                #print(current_box.number, self.head.number, current_box.next.number, current_box.next.next.number)
                current_box.next = current_box.next.next
                self.head = current_box.next
                indentation_control = RuleData.indentation
                check += 1
            else:
                #print('Пропуск', self.head.number)
                indentation_control -= 1
                self.head = self.head.next

    def counting_boxes(self, RuleData): # Метод подсчета оставшихся (счастливых) мест для тюков.
        current_box = self.first_el; luck_box = []; check = 0
        """ print( RuleData.quanity,
                RuleData.month,
                RuleData.day,
                RuleData.indentation)
        print(self.first_el, 'первый элемент', RuleData.indentation) """
        while check != RuleData.quanity:
            #print(current_box.number, 'То что будет добавлено')
            luck_box.append(current_box.number)
            current_box = current_box.next
            check += 1
        return luck_box


class RuleData_List: # Класс, содержащий параметры для определения тюков и выполнения действий с ними

    def __init__(self):
        self.quanity = None
        self.month = None
        self.day = None
        self.indentation = None


def main(): # Основная функция

    def input_data(): # Функция ввода данных, исходя из которых будут выбрасываться и оставляться тюки

        print('\n','\n',
            'Вам нужно ввести данные, исходя из которых будут выбираться места для тюков, которые не будут выброшены.\n'
            'Сначала вы ввводите все данные, после чего они отправляются на проверку. Если данные подойдут, то программа продолжит работать.\n'
            'В противном случае, если какие-то данные не подошли и вы допустили ошибку - программа остановится после общей проверки данных и сообщит вам об том, что вы ввели некорректные данные.\n'
            'Внимательно читайте сообщения - они содержат важную информацию, по правилам ввода данных.'
            '\n','\n'
            'Правила игры:\n'
            '•  каждый тюк получает порядковый номер (+), начиная с тюка, стоящего на носу корабля;\n'
            '•  их нумерация осуществляется по часовой стрелке;\n'
            '•  номер  первого  выброшенного  тюка  соответствует  текущему  числу месяца M;\n'
            '•  через  K  тюков  следующий  тюк  с  товаром  выбрасывается.\n'
            '\n','\n',
            '---------------------------------------------------------------- * ------------------------------------------------------------------')

        def quanity_cargo_box(): # Фунция ввода кол-ва тюков у одного купца
            try:
                quanity = int(input('Введите целое, неотрицательное число больше нуля, равное количеству тюков у одного купца, у другого будет столько же: '))
            except(ValueError, TypeError):
                condition = False
                quanity = None
            else:
                if quanity == 0:
                    condition = False
                else:
                    condition = True
            print('\n')
            return quanity, condition

        def current_month(): # Функция выбора месяца
            try:
                month = int(input('Введите целое число от 1 до 12, чей номер соответствует месяцу М в григорианском календаре: '))
            except(ValueError, TypeError):
                condition = False
                month = None
            else:
                if month < 1 or month > 12:
                    condition = False
                else:
                    condition = True
            print('\n')
            return month, condition

        def current_day(month): # Функция выбора дня
            try:
                day = int(input('Введите текущий день месяца М. Учтите, что в 1, 3, 5, 7, 8, 10 и 12 месяцах - 31 день. В 4, 6, 9, 11 - 30. В 2 месяце в зависимости от года - 28 или 29: '))
            except(ValueError, TypeError):
                condition = False
                day = None
            else:
                if month in [1, 3, 5, 7, 8, 10, 12]:
                    if day < 1 or day > 31:
                        condition = False
                    else:
                        condition = True
                elif month in [4, 6, 9, 11]:
                    if day < 1 or day > 30:
                        condition = False
                    else:
                        condition = True
                elif month == 2:
                    try:
                        leap_year = int(input('Вы выбрали 2 месяц - это февраль. В зависимости от того, является год висикосным или нет, зависит кол-во дней в месяце. Введите 1 если год високосный, если нет введите 0: '))
                    except(ValueError, TypeError):
                        condition = False
                    else:
                        if leap_year == 1:
                            if day < 1 or day > 29:
                                condition = False
                            else:
                                condition = True
                        elif leap_year == 0: # Выбор года - високосный или нет
                            if day < 1 or day > 28:
                                condition = False
                            else:
                                condition = True
                        else:
                            condition = False
                else:
                    condition = False
            return day, condition

        def indentation(quanity): # Функция для определения промежутка К пропущенных тюков
            try:
                indentation_value = int(input('Введите целое, неотрицательное К, больше 0 - кол-во тюков, которые будут пропущены, прежде чем следующий будет выкинут за борт: '))
            except(ValueError, TypeError):
                condition = False
                indentation_value = None
            else:
                if indentation_value < 0:
                    condition = False
                else:
                    if indentation_value >= quanity*2:
                        indentation_value = indentation_value % day # Если промежуток больше, чем кол-во тюков, то нужно брать остаток от деления такого промежутка на кол-во тюков
                    condition = True
            return indentation_value, condition

        RuleData = RuleData_List()

        quanity, quanity_condition = quanity_cargo_box()
        month, month_condition = current_month()
        day, day_condition = current_day(month)
        indentation_value, indentation_condition = indentation(quanity)
        print('\n','\n',
            '---------------------------------------------------------------- * ------------------------------------------------------------------',
            '\n','\n',)

        if quanity_condition is True and month_condition is True and day_condition is True and indentation_condition is True:
            RuleData.quanity = quanity
            RuleData.month = month
            RuleData.day = day
            RuleData.indentation = indentation_value
            return RuleData
        else:
            return None

    print('---------------------------------------------------------------- * ------------------------------------------------------------------',
        '\n','\n','\n',
        'Здравствуйте, это игра "Хитрый купец"'
        '\n','\n'
        'Два купца, имея одинаковое количество абсолютно идентичных тюков с товаром, отправились торговать за море.\n'
        'В один из дней, в море разыгрался шторм и корабль, на котором ехали купцы, был повреждён.\n'
        'Что бы спасти положение, капитан судна приказал избавится от лишней нагрузки на корабль и выбросить за борт половину товара купцов.\n'
        'Для этого, он решил выкидывать тюки по особому правилу, о котором один из купцов прознал и решил спасти свой товар.\n'
        'Вы сможете задать в этой программе условия и узнать, как купец должен расположить свой товар так, что бы полностью его спасти.\n'
        '\n','\n',
        '---------------------------------------------------------------- * ------------------------------------------------------------------')
    
    status = input_data()
    if status is not None:
        CargoList = LinkedList()
        LinkedList.adding_cargo_box(CargoList, status)
        LinkedList.removing_cargo_box(CargoList, status)
        result = (list(dict.fromkeys(LinkedList.counting_boxes(CargoList, status))))
        for i in result:
            print(i, end=' ')
        print('- Места, на которые хитрому купцу надо поставить свои тюки с товаром',
              '\n'
              '---------------------------------------------------------------- * ------------------------------------------------------------------')
        return None
    else:
        print('Введённые вами данные содержат параметры, несовместимые с условиями')
        return None
        

if __name__ == '__main__': # Вызов основной функции
    main()
