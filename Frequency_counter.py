### Frequency counter
def Frequency_Counter(arr):
    freq_dt = dict()
    for i in arr:
        if i in freq_dt:
            freq_dt[i]+=1
        else:
            freq_dt[i] = 1

    return  freq_dt      
if __name__ == "__main__":
    arr =[1, 9, 8, 5, 5, 1, 8, 4, 1, 7, 7, 10, 10, 8, 2, 8, 5, 3, 10, 1]
    freq = Frequency_Counter(arr)
    print(freq)

### frequency counter plm solve with defaultdict data structure
from collections import defaultdict  
def Frequency_Counter(arr):
    freq_dt = defaultdict(int)
    for i in arr:
        freq_dt[i]+=1

    return  freq_dt      
if __name__ == "__main__":
    arr =[1, 9, 8, 5, 5, 1, 8, 4, 1, 7, 7, 10, 10, 8, 2, 8, 5, 3, 10, 1]
    freq = Frequency_Counter(arr)
    print(freq)

### frequency counter plm solve with Counter data structure
from collections import Counter
def Frequency_Counter(arr):
    freq_dt = Counter(arr)


    return  freq_dt      
if __name__ == "__main__":
    arr =[1, 9, 8, 5, 5, 1, 8, 4, 1, 7, 7, 10, 10, 8, 2, 8, 5, 3, 10, 1]
    freq = Frequency_Counter(arr)
    print(freq)    