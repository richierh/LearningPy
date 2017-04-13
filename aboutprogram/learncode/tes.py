def test(a):
    print a
    for a in xrange(3,10,5):
        print a
        b=12
    return a,b

def function():
    answer,jawaban=test(0)
    return jawaban,answer

print function()
i = 1
while i < 20:
    print i
    i=+0.5+i

for h in ("rumah","kandang","kambing","punyaku"):
    print h
noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
x for x in range(2, 50) if x not in noprimes:
    print x
