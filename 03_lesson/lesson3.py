
#class User:   название класса
    #age =0; по умолчанию

    #def __init__(self, name): #создаем метод; строка с отступом, потому что находится внутри класса
      #  print ("Я создался")
        #self.username = name

    #def sayName(self):  #задали параметр
       # print ("меня зовут", self.username)


  #  def sayAge(self):
      #  print(self.age)
    #def setAge (self, newAge):
    #    self.age = newAge
        
from user import User
from card import Card
user1 = User ("Alex")
#user2 = User("Mark")
#user3 = User ("Denis")

user1.sayName() #запрос на имя для конкретного экземпляра
#user1.sayAge() #запрос на возраст для конкретного экземпляра
user1.setAge(33)
user1.sayAge()

card = Card ("1235 5678 5823 5687", "11/28", "Alex F")
user1.addCard(card)
user1.getCard().pay (1000)