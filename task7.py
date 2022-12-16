print('NOT(X OR Y OR Z) = NOT X AND NOT Y AND NOT Z  | RESULT')
print('----------------------------------------------|-------')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            bool1 = not(x or y or z)
            bool2 = not x and not y and not z
            # print(x,y,z,bool1 == bool2)
            print(f'NOT({x} OR {y} OR {z}) = NOT {x} AND NOT {y} AND NOT {z}  | ',bool1 == bool2)

# print('NOT(X OR Y OR Z) = NOT X AND NOT Y AND NOT Z                          | RESULT')
# print('----------------------------------------------------------------------|-------')
# for x in False, True:
#     for y in False, True:
#         for z in False, True:
#             bool1 = not(x or y or z)
#             bool2 = not x and not y and not z
#             print(f'NOT({x} OR {y} OR {z}) = NOT {x} AND NOT {y} AND NOT {z}  | ',bool1 == bool2)
#             # print(x,y,"not({arg1:>5} or {arg2:>5})".format(arg1=x,arg2=y))
