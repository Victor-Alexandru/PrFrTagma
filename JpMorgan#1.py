def solution(sentence):
    sentence = sentence.split()
    for i in  range (0,len(sentence)):
        if sentence[i][0].isalpha():
            sentence[i] = sentence[i].capitalize()


    return " ".join(sentence)


print(solution("Hello world A Letter"))