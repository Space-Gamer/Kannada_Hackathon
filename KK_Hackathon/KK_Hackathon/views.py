import time

from django.shortcuts import render
from django.http import HttpResponse
from .tr_mod import translate
from .q_gen import questionset

name = "NONE"
qno = 0
score = 0
ans = ''
res = ()
highscores = {'Noob': 0, 'Pro': 0, 'Gamer': 0, 'Ninja': 0, 'Legend': 0}


def start(request):
    global score
    score = 0
    return render(request, "start.html")


# def home_submit(request):
#     global name
#     name = request.GET.get('name')
#     print(name)
#     # return HttpResponse("Success")
#     return render(request, "quest.html")


def quest(request):
    name_l = request.GET.get('name', 'None')
    if name_l != 'None':
        global name
        name = name_l
        print(name)
    global res
    res = questionset()
    global ans
    ans = str(res[2].index(res[1].text))
    params = {'question': res[0], 'o0': res[2][0], 'o1': res[2][1], 'o2': res[2][2], 'o3': res[2][3], 'score': score}
    return render(request, "quest.html", params)


def answer(request):
    global score
    params = {'question': res[0], 'o0': res[2][0], 'o1': res[2][1], 'o2': res[2][2], 'o3': res[2][3], 'score': score}
    user_ans = request.GET.get('choice', '0')
    if user_ans == ans:
        score += 1
        params[f"o{ans}"] = params[f"o{ans}"] + "✅"
        params['score'] = score
    else:
        params[f"o{ans}"] = params[f"o{ans}"] + "✅"
        params[f"o{user_ans}"] = params[f"o{user_ans}"] + "❌"
    return render(request, "answer.html", params)


def results(request):
    # ans = request.GET.get('choice', 'None')
    global qno
    qno += 1
    # print(ans)
    if qno < 5:
        global res
        res = questionset()
        global ans
        ans = str(res[2].index(res[1].text))
        params = {'question': res[0], 'o0': res[2][0], 'o1': res[2][1], 'o2': res[2][2], 'o3': res[2][3],
                  'score': score}
        return render(request, "quest.html", params)
    else:
        qno = 0
        global highscores
        if name in highscores:
            if score > highscores[name]:
                highscores[name] = score
        else:
            highscores[name] = score
        return render(request, "results.html", {'score': score, 'name': name})


def high_score(request):
    h_lst = [[k, v] for k, v in highscores.items()]
    h_lst.sort(key=lambda x: x[1], reverse=True)
    params = {'n1': h_lst[0][0], 's1': h_lst[0][1], 'n2': h_lst[1][0], 's2': h_lst[1][1], 'n3': h_lst[2][0],
              's3': h_lst[2][1], 'n4': h_lst[3][0], 's4': h_lst[3][1], 'n5': h_lst[4][0], 's5': h_lst[4][1]}
    return render(request, "high_score.html", params)


def end(request):
    return render(request, "start.html")