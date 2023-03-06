
def oooops(inp):
    try:
        val = int(inp)
    except ValueError:
        val = len(inp)
    s = 'A'
    i = 0
    while i != val:
        s += inp[2]
        i += 1
    return s

print(oooops("abc"))
print(oooops("abcdefghi"))
try:
    print(oooops("a"))
except:
    print("Erro: IndexError")
print(oooops("008"))
try:    
    print(oooops("8"))
except:
    print("Erro: IndexError")


#print(oooops("-11"))
print("Erro: Loop infinito")
