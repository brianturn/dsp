from datetime import datetime

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

date_format_a = "%m-%d-%Y"

delta_a = datetime.strptime(date_stop, date_format_a) - datetime.strptime(date_start, date_format_a)

print ("Answer to a: ", delta_a.days)

####b)  
date_start = '12312013'  
date_stop = '05282015'

date_format_b = "%m%d%Y"

delta_b = datetime.strptime(date_stop, date_format_b) - datetime.strptime(date_start, date_format_b)

print ("Answer to b: ", delta_b.days) 

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'

date_format_c = "%d-%b-%Y"

delta_c = datetime.strptime(date_stop, date_format_c) - datetime.strptime(date_start, date_format_c)

print ("Answer to c: ", delta_c.days)  
