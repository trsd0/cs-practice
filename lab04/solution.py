
def winner(names: list[str], scores: list[float]) -> str:
    best_index = 0
    for i in range(1, len(scores)):
        if scores[i] > scores[best_index]:
            best_index = i
    return names[best_index]

def average(scores: list[float]) -> float:
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores), 2)

def ranking(names: list[str], scores: list[float]) -> list[str]:
    indices = list(range(len(names)))
    sorted_indices = sorted(indices, key=lambda i: scores[i], reverse=True)
    return [names[index] for index in sorted_indices]

def above_average(names: list[str], scores: list[float]) -> list[str]:
    above_names = []
    avr = average(scores)
    for i in range(len(scores)):
        if scores[i] > avr:
            above_names.append(names[i])
    return above_names










    

    









    
           


       



