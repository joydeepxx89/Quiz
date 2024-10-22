questions = [
    ["What is the capital of India?", "Assam", "Delhi", "Hyderabad", "Punjab", 2],
    ["How many continents are there in the world?", "7", "8", "2", "10", 1],
    ["Which element has the atomic number 1?", "Oxygen", "Helium", "Hydrogen", "Carbon", 3],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["Who wrote the play 'Romeo and Juliet'?", "Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain", 2],
    ["What is the capital of Japan?", "Beijing", "Seoul", "Bangkok", "Tokyo", 4],
    ["Which element is essential for the process of photosynthesis?", "Nitrogen", "Carbon Dioxide", "Oxygen", "Hydrogen", 2],
    ["In which year did the Titanic sink?", "1912", "1920", "1898", "1930", 1],
    ["What is the largest mammal in the world?", "African Elephant", "Blue Whale", "Giraffe", "Great White Shark", 2],
    ["Which of the following is a prime number?", "21", "33", "37", "49", 3],
    ["Which country hosted the 2016 Summer Olympics?", "China", "Brazil", "United Kingdom", "South Africa", 2],
    ["Who was the first person to walk on the moon?", "Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Michael Collins", 1],
    ["What is the chemical symbol for gold?", "Ag", "Au", "Pb", "Fe", 2]

]
levels = [1000, 2000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000]
money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\nQuestion for Rs.{levels[i]}")
    print(f"\n{question[0]}")
    print(f"1. {question[1]}  2. {question[2]}")
    print(f"3. {question[3]}  4. {question[4]}")
    
    reply = int(input("Enter your input (1-4) or 0 to quit: "))
    
    if reply == 0:
        money = levels[i-1] if i > 0 else 0
        break
    
    if reply == question[-1]:
        print(f"\nCorrect answer! You have won Rs.{levels[i]}")
        money = levels[i]  
    else:
        print("Wrong answer!")
        money = levels[i-1] if i > 0 else 0  
        break

print(f"\nYou are taking home Rs. {money}. Enjoy!")
