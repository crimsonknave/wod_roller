#!/usr/bin/env python

import argparse
import random

parser = argparse.ArgumentParser("Rolls dice for World of Darkness")
again = parser.add_mutually_exclusive_group()
again.add_argument('-9, --nine-again', action='store_const', const=9, dest="roll_again")
again.add_argument('-8, --eight-again', action='store_const', const=8, dest="roll_again")
again.add_argument('-0, --ten-again', action='store_const', const=10, dest="roll_again")
again.add_argument('-n, --nothing-again', action='store_const', const=11, dest="roll_again")
parser.add_argument('-v, --verbose', action='store_true', default=False, dest='verbose')
parser.add_argument('count', nargs = '?', default=1, type=int)
parser.set_defaults(roll_again=10)

args = parser.parse_args()

def roll(count = 1, again = 10):
  if count > 0:
    print("Rolling {} with again {}".format(count, again))
    rolls = [random.randrange(10)+1 for i in range(count)]
    rolls.extend(roll(len([x for x in rolls if x >= again]), again))
    return rolls
  else:
    return []


if __name__ == "__main__":
  rolls = roll(args.count, args.roll_again)
  successes = [x for x in rolls if x >= 8]
  re_rolls = len(rolls)-args.count if len(rolls) > args.count else 0
  print("Rolled {} and got {} successes with {} re-rolls".format(args.count, len(successes), re_rolls))
  if args.verbose:
    print(sorted(rolls))

