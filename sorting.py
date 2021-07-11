from operator import itemgetter


#%timeit {k: v for k,v in sorted(d.items(), key=itemgetter(1))}
{k: v for k,v in sorted(d.items(), key=itemgetter(1))
