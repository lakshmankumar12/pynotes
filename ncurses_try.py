#!/usr/bin/python

import curses
import curses.textpad

def my_function(stdscr):
  curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
  stdscr.addstr("Your pattern:", curses.color_pair(1))
  stdscr.refresh()
  (curry,currx) = stdscr.getyx()
  curses.echo()
  stdscr.move(15,5);
  stdscr.addstr("Print something here", curses.color_pair(1))
  stdscr.move(curry,currx);
  stdscr.addstr("continueing..", curses.color_pair(1))
  stdscr.getch()

curses.wrapper(my_function)
