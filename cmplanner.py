from tabulate import tabulate
from docopt import docopt
from planner import*
usage='''
Usage:
cmplanner.py  --init
cmplanner.py  --insert <category> <amount>
cmplanner.py  --update <category> <amount>
cmplanner.py  --remove <category>
cmplanner.py  --show   [<category>]
'''
args=docopt(usage)
if args['--init']:
    init()
    print('Table created')
if args['--insert']:
    try:
       insert(args['<category>'],args['<amount>']) 
       print('Item added') 
    except:
        print(usage)
if args['--update']:
    update(args['<category>'],args['<amount>']) 
    print('Item updated')   
if args['--remove'] :
    remove(args['<category>'])
    print('item deleted ')
if args['--show']:
    resalt,amount=show(args['<category>'])
    print(tabulate(resalt))
    print('amounts:  ',amount)                

