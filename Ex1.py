Old: print "The answer is", 3*3
New: print("The answer is", 3*23

Old: print a,           # Trailing comma suppresses newline
New: print(a, end=" ")  # Appends a space instead of a newline

Old: print              # Prints a newline
New: print()            # You must call the function!

Old: print >>sys.stderr, "fatal error"
New: print("fatal error", file=sys.stderr)

Old: print (a, b)       # prints repr((a, b))
New: print((a, b))      # Not the same as print(a, b)
