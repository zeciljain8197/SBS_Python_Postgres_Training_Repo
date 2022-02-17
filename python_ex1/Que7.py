# Perform operations with all the Bitwise Operators

(a, b) = map(int, input().split())
bitor = a | b
bitand = a & b
bitnot = ~a
bitxor = a ^ b
bitrs = a >> 1
bitls = a << 2

print(bitor,'\n',bitand,'\n',bitnot,'\n',bitxor,'\n',bitrs,'\n',bitls )
