quiz = [
    {
        "Question": "What is the capital of Germany?",
        "Answer": "berlin",
        "feedback": "The correct answer is berlin"
    },
    {
        "Question": "What is the capital of Netherlands?",
        "Answer": "amsterdam",
        "feedback": "The correct answer is amsterdam"
    },
    {
        "Question": "What is the capital of Russia?",
        "Answer": "moscow",
        "feedback": "The correct answer is moscow"
    },
    {
        "Question": "What is the capital of Greece?",
        "Answer": "athens",
        "feedback": "The correct answer is athens"
    },
    {
        "Question": "What is the capital of France?",
        "Answer": "paris",
        "feedback": "The correct answer is paris"
    },
    {
        "Question": "What is the capital of Italy?",
        "Answer": "rome",
        "feedback": "The correct answer is rome"
    },
    {
        "Question": "What is the capital of Norway?",
        "Answer": "oslo",
        "feedback": "The correct answer is oslo"
    },
    {
        "Question": "What is the capital of Sweden?",
        "Answer": "stockholm",
        "feedback": "The correct answer is stockholm"
    },
    {
        "Question": "What is the capital of Spain?",
        "Answer": "madrid",
        "feedback": "The correct answer is madrid"
    },
    {
        "Question": "What is the capital of Portugal?",
        "Answer": "lisbon",
        "feedback": "The correct answer is lisbon"
    },
    
]

score = 0
for i, q in enumerate(quiz):
    print(f"\nQuestion {i+1}: {q['Question']}")

    answer = input("Whats your answer? ").lower()

    if answer == q['Answer']:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
        print(q['feedback'])

print(f"\nYour final score is {score} out of {len(quiz)}")


