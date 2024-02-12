from PIL import Image
import random
import math

G_cluster = {}

#pick random init mean value from the rgb list
def initRandomMean(k, colors):
    mean = []
    
    for i in range(0, k):
        randomPick = random.choice(list(colors.values()))
        if randomPick not in mean:
            mean.append(randomPick)
        else:
            while True:
                randomPick = random.choice(list(colors.values()))
                if randomPick not in mean:
                    mean.append(randomPick)
                    break
    return mean

def recompute(k, colors, mean_):
    cluster = {} #cluster[pixel] = minDistanceRgb
    distance = []

    #compupte distance and calssify into cluster
    for pixel in colors:
        for j in range(0, len(mean_)):
            #print(colors[pixel])
            d = math.dist(colors[pixel], mean_[j])
            distance.append(d)
            #print(d)
        #print(distance.index(min(distance)))
        cluster[pixel] = distance.index(min(distance))
        distance.clear()
        #print("color[", i, "] cluster is ", colors[i], "= S", cluster[colors[i]]+1)
        #print("____________")

    global G_cluster
    G_cluster.clear()
    G_cluster = cluster

    cluster4mean = [(0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)]
    sizeM = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    for a in cluster:
        #print(a)
        S = cluster[a]
        if S == 0:
            sizeM[0] += 1
            cluster4mean[0] = tuple(map(lambda i, j: i + j, cluster4mean[0], colors[a]))
        if S == 1:
            sizeM[1] += 1
            cluster4mean[1] = tuple(map(lambda i, j: i + j, cluster4mean[1], colors[a]))
        if S == 2:
            sizeM[2] += 1
            cluster4mean[2] = tuple(map(lambda i, j: i + j, cluster4mean[2], colors[a]))
        if S == 3:
            sizeM[3] += 1
            cluster4mean[3] = tuple(map(lambda i, j: i + j, cluster4mean[3], colors[a]))
        if S == 4:
            sizeM[4] += 1
            cluster4mean[4] = tuple(map(lambda i, j: i + j, cluster4mean[4], colors[a]))
        if S == 5:
            sizeM[5] += 1
            cluster4mean[5] = tuple(map(lambda i, j: i + j, cluster4mean[5], colors[a]))
        if S == 6:
            sizeM[6] += 1
            cluster4mean[6] = tuple(map(lambda i, j: i + j, cluster4mean[6], colors[a]))
        if S == 7:
            sizeM[7] += 1
            cluster4mean[7] = tuple(map(lambda i, j: i + j, cluster4mean[7], colors[a]))
        if S == 8:
            sizeM[8] += 1
            cluster4mean[8] = tuple(map(lambda i, j: i + j, cluster4mean[8], colors[a]))
        if S == 9:
            sizeM[9] += 1
            cluster4mean[9] = tuple(map(lambda i, j: i + j, cluster4mean[4], colors[a]))

    for a in range(0, k):
        if sizeM[a] != 0.0:
            cluster4mean[a] = tuple(map(lambda item: item / sizeM[a], cluster4mean[a]))
            mean_[a] = cluster4mean[a]

    return mean_
    

def KMean(k, colors, mean):
    preMean = mean[:]
    mean_ = mean[:]
    iteration = 0
    #print("iteration: ", iteration)
    #print(preMean)
    mean_ = recompute(k, colors, mean_)

    while preMean != mean_:
        preMean = mean_[:]
        iteration += 1
        #print("iteration: ", iteration)
        mean_ = recompute(k, colors, mean_)
        #print(preMean)

    return mean_

picture = Image.open(r"G:\mat345\Project4\MonsterInc.jpg")
width, height = picture.size
colors = {} #colors[pixel] = rgb
#store rgb colors resulted from k-mean algorhtims
colors_k3 = []
colors_k4 = []
colors_k5 = []
colors_k6 = []
colors_k7 = []
colors_k8 = []
colors_k9 = []
colors_k10 = []

#Read RGB info and setup the data set
for x in range(width):
    for y in range(height):
        pixel = x, y
        colors[pixel] = picture.getpixel(pixel)
        #colors.append(picture.getpixel(pixel))
        
#k = 3
colors_k3 = initRandomMean(3, colors)
colors_k3 = KMean(3, colors, colors_k3)
k_mean3 = []
for i in colors_k3:
    k_mean3.append(tuple(map(int, i)))

picture_k3 = Image.new("RGB", (width, height), (255, 0, 0))
pix = picture_k3.load()

for x in range(width):
    for y in range(height):
        pixel = x, y
        S = G_cluster[pixel]
        if S == 0:
            rgb = k_mean3[0]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[0])
        if S == 1:
            rgb = k_mean3[1]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[1])
        if S == 2:
            rgb = k_mean3[2]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])

picture_k3.save('MonsterInc_k3.jpg' , 'JPEG')
#k = 4
colors_k4 = initRandomMean(4, colors)
colors_k4 = KMean(4, colors, colors_k4)

k_mean4 = []
for i in colors_k4:
    k_mean4.append(tuple(map(int, i)))

picture_k4 = Image.new("RGB", (width, height), (255, 0, 0))
pix = picture_k4.load()

for x in range(width):
    for y in range(height):
        pixel = x, y
        S = G_cluster[pixel]
        if S == 0:
            rgb = k_mean4[0]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[0])
        if S == 1:
            rgb = k_mean4[1]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[1])
        if S == 2:
            rgb = k_mean4[2]
            pix[pixel] = rgb
        if S == 3:
            rgb = k_mean4[3]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])

picture_k4.save('MonsterInc_k4.jpg' , 'JPEG')
#k = 5
colors_k5 = initRandomMean(5, colors)
colors_k5 = KMean(5, colors, colors_k5)

k_mean5 = []
for i in colors_k5:
    k_mean5.append(tuple(map(int, i)))

picture_k5 = Image.new("RGB", (width, height), (255, 0, 0))
pix = picture_k5.load()

for x in range(width):
    for y in range(height):
        pixel = x, y
        S = G_cluster[pixel]
        if S == 0:
            rgb = k_mean5[0]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[0])
        if S == 1:
            rgb = k_mean5[1]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[1])
        if S == 2:
            rgb = k_mean5[2]
            pix[pixel] = rgb
        if S == 3:
            rgb = k_mean5[3]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
        if S == 4:
            rgb = k_mean5[4]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
picture_k5.save('MonsterInc_k5.jpg' , 'JPEG')
#k = 6
colors_k6 = initRandomMean(6, colors)
colors_k6 = KMean(6, colors, colors_k6)

k_mean6 = []
for i in colors_k6:
    k_mean6.append(tuple(map(int, i)))

picture_k6 = Image.new("RGB", (width, height), (255, 0, 0))
pix = picture_k6.load()

for x in range(width):
    for y in range(height):
        pixel = x, y
        S = G_cluster[pixel]
        if S == 0:
            rgb = k_mean6[0]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[0])
        if S == 1:
            rgb = k_mean6[1]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[1])
        if S == 2:
            rgb = k_mean6[2]
            pix[pixel] = rgb
        if S == 3:
            rgb = k_mean6[3]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
        if S == 4:
            rgb = k_mean6[4]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
        if S == 5:
            rgb = k_mean6[5]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])

picture_k6.save('MonsterInc_k6.jpg' , 'JPEG')

#k = 7
colors_k7 = initRandomMean(7, colors)
colors_k7 = KMean(7, colors, colors_k7)

k_mean7 = []
for i in colors_k7:
    k_mean7.append(tuple(map(int, i)))

picture_k7 = Image.new("RGB", (width, height), (255, 0, 0))
pix = picture_k7.load()

for x in range(width):
    for y in range(height):
        pixel = x, y
        S = G_cluster[pixel]
        if S == 0:
            rgb = k_mean7[0]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[0])
        if S == 1:
            rgb = k_mean7[1]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[1])
        if S == 2:
            rgb = k_mean7[2]
            pix[pixel] = rgb
        if S == 3:
            rgb = k_mean7[3]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
        if S == 4:
            rgb = k_mean7[4]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
        if S == 5:
            rgb = k_mean7[5]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
        if S == 6:
            rgb = k_mean7[6]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
picture_k7.save('MonsterInc_k7.jpg' , 'JPEG')
#k = 8
colors_k8 = initRandomMean(8, colors)
colors_k8 = KMean(8, colors, colors_k8)

k_mean8 = []
for i in colors_k8:
    k_mean8.append(tuple(map(int, i)))

picture_k8 = Image.new("RGB", (width, height), (255, 0, 0))
pix = picture_k8.load()

for x in range(width):
    for y in range(height):
        pixel = x, y
        S = G_cluster[pixel]
        if S == 0:
            rgb = k_mean8[0]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[0])
        if S == 1:
            rgb = k_mean8[1]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[1])
        if S == 2:
            rgb = k_mean8[2]
            pix[pixel] = rgb
        if S == 3:
            rgb = k_mean8[3]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
        if S == 4:
            rgb = k_mean8[4]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
        if S == 5:
            rgb = k_mean8[5]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
        if S == 6:
            rgb = k_mean8[6]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
        if S == 7:
            rgb = k_mean8[7]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
picture_k8.save('MonsterInc_k8.jpg' , 'JPEG')
#k = 9
colors_k9 = initRandomMean(9, colors)
colors_k9 = KMean(9, colors, colors_k9)

k_mean9 = []
for i in colors_k9:
    k_mean9.append(tuple(map(int, i)))

picture_k9 = Image.new("RGB", (width, height), (255, 0, 0))
pix = picture_k9.load()

for x in range(width):
    for y in range(height):
        pixel = x, y
        S = G_cluster[pixel]
        if S == 0:
            rgb = k_mean9[0]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[0])
        if S == 1:
            rgb = k_mean9[1]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[1])
        if S == 2:
            rgb = k_mean9[2]
            pix[pixel] = rgb
        if S == 3:
            rgb = k_mean9[3]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
        if S == 4:
            rgb = k_mean9[4]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
        if S == 5:
            rgb = k_mean9[5]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
        if S == 6:
            rgb = k_mean9[6]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
        if S == 7:
            rgb = k_mean9[7]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
        if S == 8:
            rgb = k_mean9[8]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
picture_k9.save('MonsterInc_k9.jpg' , 'JPEG')
#k = 10
colors_k10 = initRandomMean(10, colors)
colors_k10 = KMean(10, colors, colors_k10)

k_mean10 = []
for i in colors_k10:
    k_mean10.append(tuple(map(int, i)))

picture_k10 = Image.new("RGB", (width, height), (255, 0, 0))
pix = picture_k10.load()

for x in range(width):
    for y in range(height):
        pixel = x, y
        S = G_cluster[pixel]
        if S == 0:
            rgb = k_mean10[0]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[0])
        if S == 1:
            rgb = k_mean10[1]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[1])
        if S == 2:
            rgb = k_mean10[2]
            pix[pixel] = rgb
        if S == 3:
            rgb = k_mean10[3]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
        if S == 4:
            rgb = k_mean10[4]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
        if S == 5:
            rgb = k_mean10[5]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
        if S == 6:
            rgb = k_mean10[6]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
        if S == 7:
            rgb = k_mean10[7]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
        if S == 8:
            rgb = k_mean10[8]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
        if S == 9:
            rgb = k_mean10[9]
            pix[pixel] = rgb
            #picture_k3[pixel].append(colors_k3[2])
picture_k10.save('MonsterInc_k10.jpg' , 'JPEG')