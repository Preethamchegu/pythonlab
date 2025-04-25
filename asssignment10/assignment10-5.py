import numpy as np
l="hello"
centered_text=np.char.center(l,15,fillchar='_')
print(centered_text)
left_justified=np.char.ljust(l,15,fillchar='_')
print(left_justified)
right_justified=np.char.rjust(l,15,fillchar='_')
print(right_justified)
