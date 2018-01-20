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

## you can also use urwid library which is a wrapper on top of curses
# pip install urwid
import urwid

#Urwid classes:
txt = urwid.Text("text-value")
#  Text widget formats blocks of text
#              auto wraps to next line if necessary
#              its a flow widget: you give columns(here full screen), and they flow to any number of rows
txt.set_text('whatever')
#               replaces current text

fill = urwid.Filler(txt, "top")
#  Filler widget    fills blank lines above/below a flow-widget
#                   its a box-widget (has fixed rows/cols)

loop = urwid.MainLoop(fill, unhandled_input=callback_fn)

def callback_fn(key):
    ''' Takes a single key argument that was pressed'''

    # to get string form of key pressed
    str_form = repr(key)

    # to exit out of MainLoop
    raise urwid.ExitMainLoop

