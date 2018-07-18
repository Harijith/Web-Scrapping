import re
pattern=re.compile("A..t")
matchObject=pattern.match("ACGTAAT")
if(matchObject):
    print(matchObject.group())
    print(matchObject.start())
    print(matchObject.end())
