import htmlData
import webbrowser

#get rid of the chinese characters
def my_filter(c):
    if c.isascii():
        return True
    else:
        return False

lnk2 = "".join(list(filter(my_filter, htmlData.lnk)))

count = 0
lnks = []


#put what follows the "href" in a list, till the next double quotation sign
def jotedown(j):
    tmp = []
    tmp.clear()
    for k in range(j, len(htmlData.lnk)):
        if htmlData.lnk[k] != '"':
            print(htmlData.lnk[k])
            tmp.append(htmlData.lnk[k])
        else:
            lnks.append("".join([str(x) for x in tmp]))
            return

#if it is, then call jotedown
def startCheck(x):
    s = "href"
    for i in range(len(s)):
        if htmlData.lnk[x + i] != s[i]:
            return
    else:
        jotedown(x + i + 3)
        return

#every time we find letter "h" we're going to check if it's the start of an "href" with startcheck
for x in range(len(htmlData.lnk)):
    if htmlData.lnk[x] == "h":
        startCheck(x)

# open the valid links
for l in lnks:
    if l != "#":
        print(l)
        webbrowser.open(l)