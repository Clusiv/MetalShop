import datetime
import time

from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine(f"sqlite:///app.db")
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

class MetalRecord(Base):
    __tablename__ = 'metalrecord'

    def __init__(self, kind, weight, date, price = 0):
        self.kind = kind
        self.weight = weight
        self.date = date
        if price:
            self.price = price
        else:
            self.price = self.get_price(kind)
        self.total = weight * self.price

    @classmethod
    def get_price(self, kind):
        metalPrice = {
        'Alum' : 10,
        'Ferrum' : 5
        }
        return metalDict[kind]

    record_id = Column(Integer, primary_key=True)
    kind  = Column(String)
    weight = Column(Integer)
    date = Column(String)
    total = Column(Integer)

    def __str__(self):
        return f'{self.kind} with weight {self.weight} - added {self.date}'

Base.metadata.create_all(engine)
Stop = True

greetings = """
Welcome to our metal shop

To exit program type 0
To add new metal record type 1
To list all records type 2

Your choise: """

# metalNum = {
#     1: 'Alum',
#     2: 'Ferrum'
#     }

metalNum = {
    1: ['Alum', 10],
    2: ['Ferrum', 5]
    }


def get_metal_by_num(num):
    return metalNum[num]

while Stop:
    command = input(greetings)
    if command == '0':
        Stop = False
    elif command == '1':

        for i in metalNum:
            print(f'{i} {metalNum[i][0]}')

        kindNum = metalNum[int(input('Insert kind of metal: '))][0]
        weight = int(input('Insert weight: '))
        price = int(input(f'Текущая цена за метал: {kind} - {MetalRecord.get_price(kind)}.\
Присвоить другую: ') or '0')
        m = MetalRecord(kind, weight, datetime.datetime.now(), price)

        session.add(m)
        session.commit()