import re
data = "shakil/35656-main-hgfhfh-123456"
value = re.search("/\d+",data)
val =re.search("\d+",value.group())
print(val)