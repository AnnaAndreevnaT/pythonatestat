# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

uniquevalues= data["whoAmI"].unique() #получаем значение из "whoAmI"
one_hote_data = pd.DataFrame() #создаем пустой DataFrame
for value in uniquevalues:
    one_hote_data[value] = (data['whoAmI'] == value).astype(int) #для каждого значения создаем столбец и заполняем 1 или 0 
one_hote_data.head()
