import angus_tools as t
import time

tm = time.time()
n = 32416189381 * 32416190071
a = t.factorise(n)
print(a, '=', eval(a), '=', n)
print(time.time() - tm)