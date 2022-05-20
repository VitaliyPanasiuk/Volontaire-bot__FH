from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import State, StatesGroup

class MakePost(StatesGroup):
    geo = State()
    geo2 = State()
    amountbed = State()
    time_for_live = State()
    pets = State()
    photo = State()
    comment = State()
    type = State()
    helptype = State()
    clotype = State()
    closize = State()
    
class getNumber(StatesGroup):
    num = State()
    num2 = State()
    num3 = State()
    
class redactPost(StatesGroup):
    act = State()
    postid = State()
    postid2 = State()
    amountbed = State()
    time_for_live = State()
    pets = State()
    comment = State()
    type = State()
    helptype = State()
    clotype = State()
    closize = State()
    