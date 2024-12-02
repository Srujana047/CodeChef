# cook your dish hereT = int(input())
for i in range(T):
    activity,origin = input().split()
    activity = int(activity)
    laddu = 0
    for i in range(activity):
        activites = input().split()
        if activites[0] == "CONTEST_WON":
            rank = int(activites[1])
            if rank <20:
                laddu += 300+20-rank
            else:
                laddu += 300
        elif activites[0] == "TOP_CONTRIBUTOR":
            laddu += 300
        elif activites[0] == "BUG_FOUND":
            laddu += int(activites[1])
        elif activites[0] == "CONTEST_HOSTED":
            laddu += 50
    if origin == "INDIAN":
        print(laddu//200)
    else:
        print(laddu//400)
