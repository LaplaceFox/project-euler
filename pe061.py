from time import time

begin = time()

figurates = [lambda n: n*(n+1)//2,
             lambda n: n**2,
             lambda n: n*(3*n-1)//2,
             lambda n: n*(5*n-3)//2,
             lambda n: n*(2*n-1),
             lambda n: n*(3*n-2)]

fig_dict = {}

for i in range(len(figurates)):
    fn = figurates[i]
    n = 1
    while True:
        if fn(n) >= 10000:
            break
        if fn(n) >= 1000:
            start = fn(n) // 100
            if start in fig_dict:
                fig_dict[start].append((i+3,fn(n)))
            else:
                fig_dict[start] = [(i+3,fn(n))]
        n += 1

def buildCycle(cur):
    #print(cur)
    #input()
    if len(cur) == 6:
        return cur # already done

    figs = list(map(lambda x: x[0], cur))
    end = cur[-1][1] % 100
    
    if end not in fig_dict:
        return None

    for nxt in fig_dict[end]:
        if nxt[0] not in figs:
            res = buildCycle(cur + [nxt])

            if res != None:
                return res
    return None

for k in fig_dict:
    for v in fig_dict[k]:
        res = buildCycle([v])

        if res != None:
            start = res[0][1] // 100 # first 2 digits of first number
            end = res[-1][1] % 100 # last 2 digits of last number

            if start == end:
                print(res)
                print(sum(list(map(lambda x: x[1], res))))
                break

print("Time taken:", time()-begin)