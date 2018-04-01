# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 22:55:13 2018

@author: bglim
"""
import pandas as pd

# Create the CSV conaining initial values. No header neither index, all sorted alphabetically
def init_data():
    names = []
    names.append("Universidade Federal de Alagoas")
    names.append("Universidade Federal da Bahia")
    names.append("Universidade Federal de Sergipe")
    names.append("Universidade Federal de Minas Gerais")
    names.append("Universidade Federal de Pernambuco")
    names.append("Universidade Federal do Rio de Janeiro")
    names.append("Pontifícia Universidade Católica do Rio de Janeiro")
    save_data(names)

# Loads existing CSV and print its data
def load_data():
    df = pd.read_csv('data.csv', header=None)
    names = []
    for name in df[0]:
        names.append(name)
    return names

# Saves an array of names in CSV
def save_data( names ):
    df = pd.DataFrame(names, columns = ['name'])
    df = df.sort_values('name')
    df.to_csv('data.csv', header=False, index=False)
 
if __name__ == '__main__':
    init_data()
    print('[INFO] The file data.csv was created successfuly.')