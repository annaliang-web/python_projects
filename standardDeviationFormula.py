# Purpose: Standard Deviation Calculator Program
# Status: Complete

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
