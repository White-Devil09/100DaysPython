# In this program we will implement KBC (Kaun Banega Crorepati)

Questions = ['1.The International Literacy Day is observed on','2.The language of Lakshadweep. a Union Territory of India, is','3.In which group of places the Kumbha Mela is held every twelve years?','4.Bahubali festival is related to','5.Which day is observed as the World Standards  Day?']

options = ['A.Sep 8  B.Nov 28  C.May 2  D.Sep 22','A.Tamil  B.Hindi  C.Malayalam  D.Telugu','A.Ujjain. Purl; Prayag. Haridwar  B.Prayag. Haridwar, Ujjain,. Nasik  C.Rameshwaram. Purl, Badrinath. Dwarika  D.Chittakoot, Ujjain, Prayag,\'Haridwar','A.Islam  B.Hinduism  C.Buddhism  D.Jainism','A.June 26  B.Oct 14  C.Nov 15  D.Dec 2']

Answers = ['a','c','b','d','b']

prize = ["0","10,00,000","30,00,000","50,00,000","70,00,000"]

for i in range(len(Questions)):
    print(Questions[i])
    print(options[i])
    ans = input("Enter your answer : ").lower()
    if ans== Answers[i] :
        if i == len(Questions)-1:
            print("\nCongrats you won 1 crore")
        else:
            print("Congrats! Let's move to next question\n")
    else:
        print(f"\nSorry! Your answer is wrong\nCorrect answer is {Answers[i].upper()}")
        print(f"You won prize money of {prize[i]}/-")
        break
