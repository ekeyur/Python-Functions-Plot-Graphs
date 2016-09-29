
myfile = open('programmers_blues.txt')

words = myfile.read().lower().split()

hist = {}

for word in words:
    word = word.replace('.', '').replace('(', '').replace(')', '').replace(',','')
    hist[word] = hist.get(word,0) + 1

def f(k):
    return k[1]

#for i,j in hist.items():
#    print "%s: %d" % (i,j)

# sorting the histogram in descending order
# sorted_hist = sorted(hist.items(), key=lambda k: k[1], reverse = True)

#sorted_hist with not using lambda
sorted_hist = sorted(hist.items(), key=f, reverse=True)

# printing the most 10 used words.
for i in range(10):
    print sorted_hist[i]
