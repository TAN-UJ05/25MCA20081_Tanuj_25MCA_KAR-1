n=int(input())
for _ in range(n):
    size=int(input())
    s=list(input())
    freq={}
    for i in s:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    max_char=max(freq,key=freq.get)
    if freq[max_char]==len(s):
        print("".join(s))
        continue
    min_char=min((c for c in freq if c!=max_char),key=lambda x:freq[x])
    for i in range(size):
        if s[i]==min_char:
            s[i]=max_char
            break
    print("".join(s))
