from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

def facto(n):

    if n == 1:
        return n

    elif n == 0:
        return 1

    elif n < 0:
        return "Not possible !"

    else:
        return n*facto(n-1)

# f(n)
def f_n(n):

    sum_facto = 0

    for j in str(n):
        sum_facto += facto(int(j))

    return sum_facto

# sf(n)
def s_f_n(sum_facto):

    s_sum_facto = 0

    for k in str(sum_facto):
        s_sum_facto += int(k)

    return s_sum_facto

def g_s_f_n(s_sum_f_n, n):
    # s_sum_f_n = 20 # Range for i: 1 upto 20 , here i = s_sum_f_n
    for new_n in range(1, n): # i >= 1

        sum_facto = f_n(new_n)
        s_sum_f_n_g = s_f_n(sum_facto, new_n)

        if (s_sum_f_n == s_sum_f_n_g):
            break

    return new_n, s_sum_f_n

def s_g_s_f_n(n):

    s_g_sum_f_n = 0

    for p in str(n):
        s_g_sum_f_n += int(p)

    return s_g_sum_f_n


def thread_shred(i, n):

    sum_g_i = 0
    for new_n in range(1, n): # i >= 1
        sum_facto = f_n(new_n)
        s_sum_f_n_g = s_f_n(sum_facto)
        # g(i), smallest positive integer, sf(n) = i or s_f_n = i
        if (i == s_sum_f_n_g): # g(i)
            sum_g_i +=  s_g_s_f_n(new_n)    # g(i) ,i = 4 So, s_sum_f_n: 1, 2, 5, 15 = 1+2+5+1+5 = 14
            break
    return sum_g_i

def range_g_s_f_n(i_range, n):

    sum_g_i = 0    # sum of g(i), e-g g(i): 1, 2, 3, 4 = 1 + 2 + 3 + 4 = 10 
    # i_range = 20 # Range for i: 1 upto 20 , here i = s_sum_f_n
    alll = []
    with ThreadPoolExecutor() as exe:
        for i in range(1, i_range + 1): # i <= i_range
            alll.append(exe.submit(thread_shred, i, n))

    z = 0
    for j in alll:
        z += j.result()
    print(z)
    return None

def main():
    
    """
        # UNCOMMENT THIS TO UNDERSTAND THE LOGIC STEP WISE
        n = 342
        
        # f(n)
        sum_facto = f_n(n)

        # sf(n)
        s_sum_f_n = s_f_n(sum_facto, n)
    
        # g(i), i = sf(n), 5 = sf(342)
        # g(i) = ?, i = sf(n)
        # g(i)
        
        # sg(i) , smallest positive interger, i = sf(n) = s_sum_f_n
        smallest_pos_n = g_s_f_n(s_sum_f_n, n)
        print(smallest_pos_n)
        print(smallest_pos_n[0])

        # sg(i), sum smallest_pos_n
        s_g_sum_f_n = s_g_s_f_n(smallest_pos_n[0])
    """
    # Range i, e-g i: 1 to 20
    n = 1000000 
    i_range = 40

    # queries = []

    # number_queries = int(input())

    # while (number_queries):
    #     user_input = list(map(int, input().split(" ")))
    #     queries.append(user_input)
    #     number_queries -= 1

    # for i in range(0, len(queries)):
    #     i_range, n = queries[i]

    #     sum_of_g_i = range_g_s_f_n(i_range, n)
    #     print(sum_of_g_i)
    sum_of_g_i = range_g_s_f_n(i_range, n)
    return None

if __name__ == "__main__":
    main()
