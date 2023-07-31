def hanoiTower(disks,start,end,mid):
    if disks==0:
        return
    else:
        hanoiTower(disks-1, start, mid, end)
        print("Moving disk",disks,"from",start,"to",end)
        hanoiTower(disks-1, mid, end,start)
        

# disks, start, end, mid
hanoiTower(3,"Django","Flask","Jinja")