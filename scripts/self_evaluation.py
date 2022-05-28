from re import split
from functools import reduce 


TEXT='''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla vehicula purus vitae sem
lacinia, et condimentum ipsum vestibulum. Nullam ullamcorper nulla vel ligula feugiat
accumsan. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sit
amet faucibus dui.'''


# 0 pari ovviamente 
# assumo 20 compreso 
def sum_even_with_next_odd(max_n=20):
    out = [x+x+1 for x in range(0,max_n+1,2)]
    return out

def find_exact_occurrences(text,occurrences=2):
    words=split(r'\W+',text.lower()) # split by regex the lowercase string  
    count = {} # dict access O(1)
    for word in words:
        if word not in count: # questo if e' evitabile usando defaultdict(int)
            count[word] = 0 
        count[word] += 1
    return sorted(list(filter(lambda x: count[x] == occurrences,count.keys()))) 

if __name__ == '__main__':
    numbers=sum_even_with_next_odd()
    print(f'1: {numbers}')
    text=find_exact_occurrences(TEXT)
    print(f'2: {text}')