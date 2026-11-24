def same(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    w2_li = []
    for i in w2:
        w2_li.append(i)
    w2_li.reverse()
    w2 = "".join(w2_li)
    print(w2)
    if w1 == w2:
        print("Words are the same!!")
    else:
        print("Words are not the same!!")


if __name__ == "__main__":
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")
    same(word1, word2)
