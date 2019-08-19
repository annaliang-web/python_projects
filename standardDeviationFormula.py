# File: Lab7A.py
# Programmer: Chaoer Liang
# Date: Feb.20, 2019
# Purpose: Standard Deviation Program
# Status: Complete

'''
=== RESTART: /Users/anna/Desktop/Coquitlam College/CSCI120A/Lab 7/Lab7A.py ===
------------ Standard Deviation Formula ------------
How many numbers do you want to enter? 6
Enter element 1 : 2
2.0
Enter element 2 : 5
5.0
Enter element 3 : 9
9.0
Enter element 4 : 12
12.0
Enter element 5 : 15
15.0
Enter element 6 : 17
17.0
[2.0, 5.0, 9.0, 12.0, 15.0, 17.0]
total: 60.0
Mean: 10.0
64.0
25.0
1.0
4.0
25.0
49.0
168.0
Difference: 168.0
Standard Deviation!! 5.291502622129181
>>> 

'''
'''
=== RESTART: /Users/anna/Desktop/Coquitlam College/CSCI120A/Lab 7/Lab7A.py ===
------------ Standard Deviation Formula ------------
How many numbers do you want to enter? 7
Enter element 1 : 3.5
3.5
Enter element 2 : 4.2
4.2
Enter element 3 : 5.7
5.7
Enter element 4 : 8.8
8.8
Enter element 5 : 10.6
10.6
Enter element 6 : 11.9
11.9
Enter element 7 : 13.2
13.2
[3.5, 4.2, 5.7, 8.8, 10.6, 11.9, 13.2]
total: 57.900000000000006
Mean: 8.271428571428572
22.766530612244907
16.576530612244902
6.612244897959187
0.2793877551020407
5.422244897959178
13.166530612244895
24.290816326530596
89.1142857142857
Difference: 89.1142857142857
Standard Deviation!! 3.56799835270393
>>> 
'''
'''
=== RESTART: /Users/anna/Desktop/Coquitlam College/CSCI120A/Lab 7/Lab7A.py ===
------------ Standard Deviation Formula ------------
How many numbers do you want to enter? 8
Enter element 1 : 13.6
13.6
Enter element 2 : 14.9
14.9
Enter element 3 : 18.2
18.2
Enter element 4 : 23.7
23.7
Enter element 5 : 41.8
41.8
Enter element 6 : 52.9
52.9
Enter element 7 : 63.8
63.8
Enter element 8 : 71.8
71.8
[13.6, 14.9, 18.2, 23.7, 41.8, 52.9, 63.8, 71.8]
total: 300.7
Mean: 37.5875
575.4001562499999
514.72265625
375.87515625
192.86265625
17.745156249999987
234.47265625
687.09515625
1170.4951562499998
3768.66875
Difference: 3768.66875
Standard Deviation!! 21.704460227105397
>>> 

'''
import math

print();
print('\u231B \u231B \u231B Standard Deviation Formula \u231B \u231B \u231B')
def sd(Num_Elements, Dif_Func):   #Standard Deviation Formula
    divide = Dif_Func / Num_Elements
    return round(math.sqrt(divide), 4)      #5.2915

def difference(Mean_Func,Initial_List_Func):    #dif_func
    dif_total = 0
    for i in range(len(Initial_List_Func)):
        dif = (Initial_List_Func[i] - Mean_Func)**2
        dif_total = dif_total + dif
    return dif_total

def mean(Num_Elements, Initial_List_Func):      #mean_func
    total = 0
    for i in range(len(Initial_List_Func)):
        total = total + Initial_List_Func[i]
    print('\nTotal:', total)
    mean = total / Num_Elements
    return round(mean, 1)     #10.0

def initial_list(Num_Elements, Elements_List):  #initial_list_func 
    for e in range(Num_Elements):   #use loop to store each user input data
        each_element = float(input('Enter' + ' element ' + str(e+1) + ' : ')) #2 5 9 12 15 17
        Elements_List.append(each_element)
    print('Entered numbers:', end=" ")
    for n in range(len(Elements_List)):
        print(Elements_List[n], end=", ")    #outputs entered numbers to the user
    return Elements_List
    
def main():
    elements_list = []
    num_elements = int(input('\nHow many numbers do you want to enter? ')) #6  number of elements
    initial_list_func = initial_list(num_elements, elements_list) #call initial_list()
    mean_func = mean(num_elements, initial_list_func) #call mean()
    print('Mean:', mean_func)
    dif_func = difference(mean_func, initial_list_func)    #call difference()
    #print('Difference:', dif_func)
    sd_func = sd(num_elements, dif_func)
    print('Standard Deviation:', sd_func)
main()
