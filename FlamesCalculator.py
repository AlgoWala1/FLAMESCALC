print("Hello, welecome to FLAMES prediction...")
# dictionary for each alphabet meaning
code = {"F": "Friendship", "L": "Love", "A": "Affair",
       "M": "Marriage", "E": "Enemy", "S": "Siblings"}
       
while True:
   name1 = input("Name1:")
   name2 = input("Name2:")
   
   #format both strings
   name1 = name1.lower()
   name1 = name1.replace(" ", "")
   name2 = name2.lower()
   name2 = name2.replace(" ", "")
   
   c = "FLAMES"
   common = []
   # Compute all the common alphabets
   for i in name1:
      for j in name2:
        if i == j:
            if i not in common:
               common.append(j)
               
   # Remove all these common characters from these strings
   for m in common:
    name1 = name1.replace(m, "")
    name2 = name2.replace(m, "")
    
   # iteration with length
   l = len(name1)+len(name2)
   pos = 0  # from the start
   while True:
     k = 0
     while k < l:
        if pos == len(c):
            pos = 0
        pos += 1
        k += 1
        
     pos = pos - 1
     
     if pos == len(c):
         pos = 0
     #keep on removing alphabets from the FLAMES string
     c = c.replace(c[pos],"")
     
     
     #the alphabet that remains is the flames result
     if len(c) == 1:
        print("FLAMES Prediction is",code.get(c))
        break
   
   c = input("Again Y/N:")
   c = c.upper()
   if c == 'N':
    break
    

