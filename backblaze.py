import os
g = os.listdir('/home/walker/Documents/canonical/data')
o = open('/home/walker/Documents/canonical/drives.csv', 'w+')

for f in g:
    with open('/home/walker/Documents/canonical/data/' + f) as fl:
        content = fl.readlines()
        del content[0]
        for l in content:
            o.write("%s" % l)
