from transformers.constants import asconstants

z = [1, 2, 3]

def a():
    return len(z)

b = asconstants(z=z)(a)

z = [1,3]
import dis
print "Natural:"
dis.dis(a)
print "\nTransformed:"
dis.dis(b)

# prints: 2, 3