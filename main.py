def postfixare(infix):
  simboluri = {'*': 3, '.': 2, '+': 1}
  pofix, stiva = "", ""
  for c in infix:
    if c == '(':
      stiva = stiva + c
    elif c == ')':
      while stiva[-1] != '(':
        pofix = pofix + stiva[-1]
        stiva = stiva[:-1]
      stiva = stiva[:-1]
    elif c in simboluri:
      while stiva and simboluri.get(c, 0) <= simboluri.get(stiva[-1], 0):
        pofix, stiva = pofix + stiva[-1], stiva[:-1]
      stiva = stiva + c
    else:
      pofix = pofix + c

  while stiva:
    pofix, stiva = pofix + stiva[-1], stiva[:-1]

  return pofix




def doarLitere(sir):
    rez=""
    for x in sir:
        if x.islower() or x.isupper():
            rez+=x
    return rez



citire=input("Regex: ").strip()

litere=list(set((doarLitere(citire)+'l')))
regex=postfixare(citire)

s=[]
stiva=[]
start=0
end=1
cnt=-1
c1=0
c2=0
print(regex)
for i in regex:
    if i in litere:
        cnt=cnt+1
        c1=cnt
        cnt=cnt+1
        c2=cnt
        s.append({})
        s.append({})
        stiva.append([c1,c2])
        s[c1][i]=c2
    elif i=='*':
        r1, r2 = stiva.pop()
        cnt = cnt + 1
        c1 = cnt
        cnt = cnt + 1
        c2 = cnt
        s.append({})
        s.append({})
        stiva.append([c1, c2])
        s[c1]['l'] = (r1, r2)
        s[r1]['l'] = (r2, c2)
        if start == r1:
            start = c1
        if end == r2:
            end = c2
    elif i=='.':
        r11,r12=stiva.pop()
        r21,r22=stiva.pop()
        stiva.append([r21,r12])
        s[r22]['l']=r11
        if start==r11:start=r21
        if end==r22:end=r12
    else:
        cnt=cnt+1
        c1=cnt
        cnt=cnt+1
        c2=cnt
        s.append({})
        s.append({})
        r11,r12=stiva.pop()
        r21,r22=stiva.pop()
        stiva.append([c1,c2])
        s[c1]['l']=(r21,r11)
        s[r12]['l']=c2
        s[r22]['l']=c2
        if start==r11 or start==r21:
            start=c1
        if end==r22 or end==r12:
            end=c2


nfa={}
for nr,x in enumerate(s):
    nfa[nr]=x

print(nfa)
#print("Stare   Litera   Stare urm.")
for x in nfa:
    print(x,nfa[x])
    #print('q'+str(x)+"      ",*nfa[x],"     ",*['q'+str(x) for x in nfa[x].values()])
