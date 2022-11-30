class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computation(self):
        return f'Memory + memory = {self.__memory + self.__memory} '


    def __str__(self):
        return f'Cpu: {self.cpu}'\
                f'Memory: {self.memory}'

    def __add__(self, other):
            return self.__memory + other.memory

    def __sub__(self, other):
            return self.__memory - other.memory

    def __gt__(self, other):
        return self.__memory > other.memory

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_card_list(self):
        return self.__sim_cards_list

    @sim_card_list.setter
    def sim_card_list(self, value):
        self.__sim_cards_list = value



    def call(self, call_to_number, sim_card_number):
        # self.call_to_number = call_to_number
        # self.sim_card_number = sim_card_number
        print(f'Идёт звонок на номер {call_to_number}'
              f' с сим карты {sim_card_number}')

    def __str__(self):
        return f'sim_cards_list.{self.sim_card_list}'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f'Маршрут проложен до: {location}!')

    def __str__(self):
        return f'Cpu: {self.cpu} Memory: {self.memory} Sim: {self.sim_card_list}'

sim = ['1 MegaCom', '2 O!']

comp =Computer(8, 1000)
comp.make_computation()
tel =Phone(1)
sp = SmartPhone(4, 64, sim[0])
sp2 = SmartPhone(6, 258, sim[1])

sp.call('+996500090909', sim[0])
sp.use_gps('Bishkek')

print(comp)
print(comp.make_computation())
print(tel)
print(sp)
print(sp2)
print(comp > sp)
print(comp + sp)
print(sp2 - sp)


