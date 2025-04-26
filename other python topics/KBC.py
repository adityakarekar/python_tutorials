questions=[
    ["What is the first letter in the alphabet?","a","b","c","d"],    
    ["Who invented facebook?","Mark Zuckerberg","Stallin","Hitler","Mark Evans"],
    ["What is the name of the biggest flower in the world?","Rose","Sunflower","Rafleshia","Lotus"],
]
correct_answers=["a","a","c"]

levels=[1000,2000,3000]
amount_won=0


for i in range(0, len(questions)):
    question=questions[i][0]
    correct_answer=correct_answers[i]
    print(question)
    print(f"a.{questions[i][1]}           b.{questions[i][2]}")
    print(f"c.{questions[i][3]}           b.{questions[i][4]}")

    user_answer = input("Enter your correct answer (a/b/c/d): ").lower().strip()
    if user_answer not in ["a","b","c","d"]:
        print("You entered an invalid character. You must select options between a/b/c/d")
        continue
    if(user_answer==correct_answer):
        print(f"Correct! You won Rs: {levels[i]}")
        amount_won+=levels[i]
    else:
        print(f"Wrong answer......... Your total earnings from this quiz are {amount_won}")
        break