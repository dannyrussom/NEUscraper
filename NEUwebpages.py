import htmlData
import webbrowser

def mfltr(c):
    if c.isascii():
        return True
    else:
        return False

lnk2 = "".join(list(filter(mfltr, htmlData.lnk)))

count = 0
lnks = []

def jotedown(j):
    print("we're in")
    tmp = []
    tmp.clear()
    for k in range(j, len(htmlData.lnk)):
        if htmlData.lnk[k] != '"':
            print(htmlData.lnk[k])
            tmp.append(htmlData.lnk[k])
        else:
            lnks.append("".join([str(x) for x in tmp]))
            print(tmp)
            return


def startCheck(x):
    s = "href"
    for i in range(len(s)):
        if htmlData.lnk[x + i] != s[i]:
            return
        #else:
            #print(lnk[x + i])
    else:
        #print("found", lnk[x + i],lnk[x + i + 1], lnk[x + i + 2], lnk[x + i + 3])
        jotedown(x + i + 3)
        return

for x in range(len(htmlData.lnk)):
    if htmlData.lnk[x] == "h":
        startCheck(x)


my_list = []

for l in lnks:
    if l != "#":
        my_list.append(l)
        print(l)
        
webbrowser.open("https://www.google.com")