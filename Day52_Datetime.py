#import functions (datetime, time) from datetime
from datetime import datetime 
from datetime import time

no = datetime.now()
ddt = datetime(2020, 2, 2)
tim = time()

print(no , "\n" , ddt , "\n" , tim.strftime("%I") , "\n" , no.strftime("%c"))