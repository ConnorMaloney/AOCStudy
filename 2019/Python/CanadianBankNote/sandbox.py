import time
import random
import operator
while 1:
    time.sleep(1)
    a = random.randint(1,10)
    b = random.randint(1,10)
    ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    o = random.choice(list(ops.keys()))
    print(a,o,b,"=",ops[o](a,b))
