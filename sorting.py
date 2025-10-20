import random

unsorted=[9,1,6,2,4,8,3,5,7]

unsorted = []
for i in range(0,5):
    unsorted.append(random.randint(0,1000))
counter=0
def comparativeCheck(list):
    global counter
    counter+=1
    sorted=True
    for i in range(0,len(list)-1):
        if list[i]>list[i+1]:
            sorted=False
    return sorted

# def bubbleSort2(list,a,counter):
#     n=0
#     localList = list
#     if localList[a]>localList[a+1]:
#         n = localList[a]
#         localList[a] = localList[a+1]
#         localList[a+1] = n
#         counter=0
#     else:
#         counter+=1
#     if a<=len(localList)-3:
#         bubbleSort2(localList,a+1,counter)
#     elif counter==len(localList)-1:
#         print(localList)
#     else:
#         bubbleSort2(localList,0,0)
# def bubbleSort(list):
#     sorted=False
#     while not sorted:
#         sorted=True
#         for i in range(0,len(list)-1):
#             if list[i]>list[i+1]:
#                 temp = list[i]
#                 list[i] = list[i+1]
#                 list[i+1] = temp
#                 sorted=False
#     return list
# # bubbleSort2(unsorted,0,0)
# print(bubbleSort(unsorted))


    
def radixSort(list):
    newList=[]
    oldList = list
    for k in range(0,3):
        newList=[]
        for i in range(0,10):
            for j in range(len(oldList)):
                temp = str(oldList[j])
                if len(temp)-k-1 < 0:
                    if i == 0:
                        newList.append(oldList[j])
                else:
                    tempInt = int(temp[len(temp)-k-1])
                    if tempInt == i:
                        newList.append(oldList[j])
        oldList=newList
    print(newList)
def bogoSort(list):
    oldList =list
    newList =[]
    for i in range(len(list)):
        n = random.randint(0,len(oldList)-1)
        newList.append(oldList[n])
        oldList.remove(oldList[n])
    if comparativeCheck(newList):
        print(newList)
        global counter
        print(counter)
    else:
        bogoSort(newList)
        

