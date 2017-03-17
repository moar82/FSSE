from __future__ import division
from Benchmarks.POM3 import pre_defined
from Algorithms.NSGA2 import action
from repeats import request_new_file
import time
import pdb

if __name__ == '__main__':
    model = pre_defined()[2]
    for repeat in range(1):
        start_time = time.time()
        res = action(model, mu=300, ngen=10000//100, cxpb=0.9, mutpb=0.15)
        finish_time = time.time()

        with open(request_new_file('/Users/jianfeng/Desktop/tse_rs/nsga2', model.name), 'w') as f:
            f.write('T:' + str(start_time) + '\n~~~\n')
            f.write('T:' + str(finish_time) + '\n')
            for i in res:
                f.write(' '.join(map(str, i.fitness.values)))
                f.write('\n')

        print('******   ' + str(repeat) + '   ******')
