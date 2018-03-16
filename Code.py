# -*- coding: utf-8 -*-
#Author : Abhinav Mahapatra
#Functionality : Adaptive rock paper scissors
#Designed as a hobby project.

import pandas as pd
import numpy as np
import time

input_list = [1, 2, 3, 2, 1, 3, 1, 2, 1, 2]
input_time = [3.665839910507202, 2.487027406692505, 3.7285304069519043, 
           1.2638773918151855, 2.0523548126220703, 2.064756393432617,
           1.5031514167785645, 1.5945348739624023, 1.113497018814087,
           2.0327258110046387]

def smart_move(input_list, input_time, time_diff):

    input_df = pd.DataFrame(input_list)    
    time_df = pd.DataFrame(input_time)

    dataset = pd.concat([time_df, input_df], axis=1)
    dataset.columns = ['Time taken','User_choice']
     
    #Selecing independent and dependent variables
    X = dataset.iloc[:,[0]].values
    y = dataset.iloc[:, [1]].values
    
    #Applying naive bayes classification
    from sklearn.naive_bayes import GaussianNB
    classifier = GaussianNB()
    classifier.fit(X,y)

    #predicting the output
    return(classifier.predict(time_diff))

def result(y_pred, user_input):
    legend = {1:'Rock',
              2:'Paper',
              3:'Scissors'}

    if y_pred == 1 :
        mach_pred = 2
    elif y_pred == 2:
        mach_pred = 3
    elif y_pred == 3:
        mach_pred = 1

    if mach_pred == user_input:
        print('Result: Draw')
        print('Machine Predict: '+legend[mach_pred])
        print('User Predict: '+legend[user_input])

    if mach_pred == 1 and user_input == 2:
        print('Result: User Won')
        print('Machine Predict: '+legend[mach_pred])
        print('User Predict: '+legend[user_input])
    elif mach_pred == 2 and user_input == 1:    
        print('Result: Machine Won')
        print('Machine Predict: '+legend[mach_pred])
        print('User Predict: '+legend[user_input])
    elif mach_pred == 2 and user_input == 3:
        print('Result: User Won')
        print('Machine Predict: '+legend[mach_pred])
        print('User Predict: '+legend[user_input])
    elif mach_pred == 3 and user_input == 2:    
        print('Result: Machine Won')
        print('Machine Predict: '+legend[mach_pred])
        print('User Predict: '+legend[user_input])
    elif mach_pred == 3 and user_input == 1:
        print('Result: User Won')
        print('Machine Predict: '+legend[mach_pred])
        print('User Predict: '+legend[user_input])
    elif mach_pred == 1 and user_input == 3:    
        print('Result: Machine Won')
        print('Machine Predict: '+legend[mach_pred])
        print('User Predict: '+legend[user_input])
    

while 1:
    init_time = time.time()
    user_input = int(input('Enter rock(1), paper(2) or scissors(3): '))
    time_diff = time.time() - init_time    
    y_pred = smart_move(input_list, input_time, time_diff)
    result(y_pred, user_input)
    #Adding the data
    input_list.append(user_input)
    input_time.append(time_diff)
        