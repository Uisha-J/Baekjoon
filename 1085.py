x, y, w, h = map(int,input().split())

shortcutx = int(0)
shortcuty = int(0)

if x <= (w / 2):
    shortcutx = x
else:
    shortcutx = w - x
    
if y <= (h / 2):
    shortcuty = y
else:
    shortcuty = h - y

if shortcutx >= shortcuty:
    print(shortcuty)
else:
    print(shortcutx)
