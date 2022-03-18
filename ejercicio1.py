vocales=['a','e','i','o','u']

print(vocales)

print(" ")

print({vocales[0]},{vocales[1]},sep="+")

print(" ")

for i in range(10):
    print(i,end="-")

print(" ")

for i in range(len(vocales)):

    print(f"{vocales[i]}")


print(" ")

for c in vocales:
    print(f"vocal:{c}")

    print(" ")

    for c in vocales :
  
      if c == 'b':

          break
else: 

 print("no se ha encontrado la b")

 

