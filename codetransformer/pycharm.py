from transformers.constants import asconstants

z = [1, 2, 3]
class A(object):
    def a(s):
        return len(z)

b = asconstants(a=A(), z=z)(lambda: a.a())

z = [1,3]
import dis
print "Natural:"
# dis.dis(a)
print "\nTransformed:"
dis.dis(b)

print  b()
# prints: 2, 3