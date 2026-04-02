for a in range(2,10):
    print("#  %d단  #"%(a),end="    ")
print()
for a in range(1,10):
    for b in range(2,10):
        print("%d X %d = %2d"%(b,a,a*b),end="   ")
    print()
