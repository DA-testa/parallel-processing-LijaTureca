# python3
import re
def parallel_processing(n, m, data):
    output = []
    threads = []
    
    for i in range(n):
       thread = (i, 0)
       threads.append(thread)

    for i in range(m):
        def get_time(elem):
         return elem[1]
    
        min_thread = min(threads, key=get_time)
        output.append((min_thread[0], min_thread[1]))
        threads.remove(min_thread)
        threads.append((min_thread[0], min_thread[1] + data[i]))

    return output

def main():
    n_m=[]
    nm=input()
    b=re.split(' ',nm)
    for x in b:
        n_m.append(int(x))
    n=n_m[0]
    m=n_m[1]

    data=[]
    d=input()
    a=re.split(' ',d)
    for x in a: 
        data.append(int(x))

    result = parallel_processing(n, m, data)

    for r in result:
        print(r[0], r[1])



if __name__ == "__main__":
    main()
