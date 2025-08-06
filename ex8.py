formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4)) #formatter.format() as a function
print(formatter.format("one","two","three","four"))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter)) #nested format
print(formatter.format(
"Try your",
"Own text here",
"Maybe a poem",
"Or a song about fear"
))