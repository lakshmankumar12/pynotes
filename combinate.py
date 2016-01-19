#!/usr/bin/python

import sys

def choose(available,so_far,to_pick,verbose=False):
  if to_pick == 0:
    if verbose:
      print(so_far)
    return 1
  s = 0
  if to_pick < len(available):
    s = choose(available[1:],so_far,to_pick,verbose)
  return s + choose(available[1:],so_far+[available[0]],to_pick-1,verbose)

if __name__ == '__main__':
  n=int(sys.argv[1])
  r=int(sys.argv[2])
  t=choose(list(range(1,n+1)),[],r,True)
  print("%d C %d is %d"%(n,r,t))

