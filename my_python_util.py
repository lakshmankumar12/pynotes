def general_expect(child, expect_list, intent_desc, eof_ok=0, print_output=0, timeout=0, timeout_ok=0):
  ''' Wrapper on top of pexpect's child.expect([expect-list])

      intent_desc  is a string, that will printed if expect throws a exception.
      eof_ok       if non-0, returns len(expect_list)+1 when eof is hit. Otherwise eof is bad
      print_output is whether to emit child's stdout in the good-case condition
                   O/p is always stored into general_expect_failure on error
      timeout_ok   if non-0, then timeout doesn't raise Exception. You will get len(expect_list)+2 as result.
      timeout      if non-0, is passed to expect, otherwise Not. You can wait infinitely with this wrapper. Sorry.

      Note that child.before and child.after are still available to caller to consume
  '''
  try:
    error = ""
    if timeout:
      result = child.expect(expect_list, timeout)
    else:
      result = child.expect(expect_list)
      if result >= len(expect_list):
        #huh!
        error = "Got none of the expected result!"
  except pexpect.EOF:
    if eof_ok:
      result = len(expect_list)
    else:
      error="Eof hit:\n"
  except pexpect.TIMEOUT:
    if timeout_ok:
      result = len(expect_list)+1
    else:
      error="Timeout out without matches:\n"
  if print_output:
    print child.before+child.after
  if error:
    err_str = "Error while doing:" + intent_desc + "\n" + "Error:" + error + "\n"
    if isinstance(expect_list, basestring):
      expected=expect_list
    else:
      expected = ""
      for i in expect_list:
        expected += i + "\n"
    err_str += "Expected:\n" + expected + "\n"
    open("general_expect_failure","w").write(err_str+child.before)
    raise Exception(err_str);
  return result
