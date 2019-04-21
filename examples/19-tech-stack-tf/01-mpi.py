#!python
# -*- coding: utf-8 -*-

import sys
import numpy as np
from mpi4py import MPI


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def part_pi( r,p,n=int(5e8) ):
    s = n//p # размер отрезка для одного процесса
    i = np.array( range( s*r,s*(r+1) ) , dtype=np.float )
    x = (i-0.5)*(1.0/n)
    return np.sum( 4.0 / ( 1.0 + x**2 ) )*(1.0/n)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def main():

    comm = MPI.COMM_WORLD
    p = comm.Get_size() # количество процессов
    r = comm.Get_rank() # номер процесса
    pname = MPI.Get_processor_name() # имя узла

    print('%s : %i/%i'%( pname,r,p) )

    res=np.zeros(1,dtype=np.float)

    comm.Allreduce( 
            np.array( part_pi(r,p), dtype=np.float ), 
            res, 
            op=MPI.SUM 
            )

    if(r==0): print('\n pi',res)
        


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
if __name__=="__main__":
    sys.exit(main())




# mpirun --hostfile ../hosts -np 4   python -uB main.py

# lscpu, nproc, cat /proc/cpuinfo


# $ ./run.sh
# node223 : 4/8
# node223 : 5/8
# node223 : 6/8
# node223 : 7/8
# t61b : 0/8t61b : 1/8
# t61b : 2/8
# t61b : 3/8
# 
# 
#  pi [3.14159266]
# 
# real	0m16,966s
# user	0m30,172s
# sys	0m12,436s



# $ ./run.sh
# t61b : 0/4
# t61b : 1/4
# t61b : 2/4
# t61b : 3/4
# 
#  pi [3.14159266]
# 
# real	0m19,390s
# user	0m55,648s
# sys	0m21,071s
# 
