#!/usr/bin/python

import sys

def next_step(so_far,items):
  return (n for n in range(1,items+1) if (n not in so_far))

def patterns(tot_items,so_far,n,verbose=False):
  if n == 0:
    if verbose:
      print(so_far)
    return 1
  return sum(patterns(tot_items,so_far+[i],n-1,verbose) for i in next_step(so_far,tot_items))

if __name__ == '__main__':
  n=int(sys.argv[1])
  t=patterns(n,[],n,True)
  print("sum is %d"%t)

