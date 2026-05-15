import datetime
import pytz

# print(dir(datetime))

# print(dir(pytz))



print([x for x in dir(pytz) if not x.startswith('_')])
print('\n')
print([x for x in dir(datetime) if not x.startswith('_')])
