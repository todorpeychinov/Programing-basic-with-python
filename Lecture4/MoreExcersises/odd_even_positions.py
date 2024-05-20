n = int(input())

oddsum = 0.00
oddmin = None
oddmax = None
evensum = 0.00
evenmin = None
evenmax = None

if n >= 2:
    num = float(input())
    oddsum += num
    oddmin = num
    oddmax = num
    num = float(input())
    evensum += num
    evenmin = num
    evenmax = num

elif n >= 1:
    num = float(input())
    oddsum += num
    oddmin = num
    oddmax = num


for i in range(3,n + 1):
    num = float(input())
    if i % 2 != 0:
        oddsum += num
        if num < oddmin:
            oddmin = num
        if num > oddmax:
            oddmax = num
    else:
        evensum += num
        if num < evenmin:
            evenmin = num
        if num > evenmax:
            evenmax = num



print(f"OddSum={oddsum:.2f},")

if oddmin == None:
    print("OddMin=No,")
else:
    print(f"OddMin={oddmin:.2f},")

if oddmax == None:
    print("OddMax=No,")
else:
    print(f"OddMax={oddmax:.2f},")

print(f"EvenSum={evensum:.2f},")

if evenmin == None:
    print("EvenMin=No,")
else:
    print(f"EvenMin={evenmin:.2f},")

if evenmax == None:
    print("EvenMax=No")
else:
    print(f"EvenMax={evenmax:.2f}")







