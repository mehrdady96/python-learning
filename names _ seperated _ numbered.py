names = ['mehrdad', 'ali', 'kimia']
for name in names:
   output  = ''
   for n, m in enumerate(name, start=1):
       output += f'{n} -> {m} / '
   print(output[:-3])
 
