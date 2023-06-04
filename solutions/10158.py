w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

precycle = w - x
xt = t % (w * 2)
if xt <= precycle:
    x += xt
elif precycle < xt <= precycle + w:
    x = w - (xt - precycle)
else:
    x = xt - (precycle + w)

precycle = h - y
yt = t % (h * 2)
if yt <= precycle:
    y += yt
elif precycle < yt <= precycle + h:
    y = h - (yt - precycle)
else:
    y = yt - (precycle + h)

print(x, y)
