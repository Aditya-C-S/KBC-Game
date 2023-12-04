import pyfiglet# pyfiglet is a module used to generate large text for titles etc

# Generate large ASCII art text for the title using the "big" font
title_ascii_art = pyfiglet.figlet_format("KON   BANEGA CROREPATI", font="big")

# Print the title
print(title_ascii_art.center(500))

def check_answers(question, answer, reward):
    print(question)
    user_answer = input("Enter your answer (or press 'q' to quit): \n")

    if user_answer.lower() == 'q':
        if total_reward >= 2500000:# checkpoint 3
            print(f"You chose to quit. You won {min(total_reward, 2500000)} rupees. 🏆💰\n Better luck next time \n")
            exit()
        elif total_reward >= 500000:# checkpoint 2
            print(f"You chose to quit. You won {min(total_reward, 500000)} rupees.🏆💰\n Better luck next time \n")
            exit()
        elif total_reward >= 40000:# checkpoint 1
            print(f"You chose to quit. You won {min(total_reward, 40000)} rupees. 🏆💰\n Better luck next time \n")
            exit()
        else:
            print("You chose to quit. You won 0 rupees. 😢\n")
            exit()

    if user_answer.lower() == answer.lower():
        print(f"Correct Answer! 🎉 You won {reward} rupees. 💰\n")
        return True
    else:
        print(f"Wrong Answer! 😞 You lost {reward} rupees. Your disqualified. 🚫\n")
        return False

questions = [
    ('''Question no 1, for 1000 rupees: 
    Who is the president of India?
    A) Narendra Modi 

    B) Nirmala Sitharaman 

    C) Droupadi Murmu 

    D) Amit Shah  ''', "c", 1000),
    (''' Question no 2, for 2000 rupees:
    Which gas is used for the preparation of Soda water?

    A) Oxygen 

    B) Carbon Dioxide 

    C) Ammonia 

    D) Hydrogen ''', "b", 2000),
    (''' Question no 3, for 5000 rupees:
    Tsunamis are not caused by
    A) Hurricanes 

    B) Earthquakes 

    C) Undersea landslides 

    D) Volcanic eruptions ''', "a", 5000),
    (''' Question no 4, for 10000 rupees:
    Which planet is closest to the sun?
    A) Mercury 

    B) Venus 

    C) Earth 

    D) Mars ''', "a", 10000),
    (''' Question no 5, for 20000 rupees:
    Which one of the following is the smallest continent?
    A) Australia

    B) Africa 

    C) Antarctica 

    D) Asia ''', "a", 20000),
    (''' Question no 6, for 50000 rupees:
    Which one of the following is the longest river in the world?
    A) Amazon 

    B) Nile 

    C) Yangtze 

    D) Mississippi ''', "b", 50000),
    ('''Question no 7, for 1 lakh:
    Which one of the following ports is the oldest port in India?
    A) Mumbai Port 

    B) Chennai Port 

    C) Kolkata Port 

    D) Vishakhapatnam Port ''', "b", 100000),
    ( '''Question no 8, for 5 lakhs:
    India lies in which of the following hemispheres?

    A) Southern and Western

    B) Southern and Eastern

    C) Northern and Western

    D) Northern and Eastern''' ,'d',500000),
('''Question no 9, for 10 lakhs:
    Which of the following is an anti-diabetic drug?

    A) Insulin

    B) Aspirin

    C) Penicillin

    D) None of the Above''',"a",1000000),
    ( ''' Question no 10, for 25 lakhs:
    How many times an adult breathes approximately in one minute?

    A) 71-78

    B) 16-18

    C) 100-110

    D) 30-35''',"b",2500000),
    ('''Question no 11, for 50 lakhs:
    Who was the first person to get bharat ratna from karnataka?
    A) Kempegowda

    B) Dr Rajkumar

    C) Dr Vishveshvaraya

    D) Rahul dravid ''' ,"c",5000000),
    (''' The LAST QUESTION , for 1 crore:
    The answer is really big? 
    A)THE ANSWER

    B)Really big

    C)An elephant

    D)The data given is insufficient ''',"a",10000000)
]

total_reward = 0

for i, (question, answer, reward) in enumerate(questions):
    if i == len(questions) - 1:
        # Check if it's the last question and the user answered it correctly
        if check_answers(question, answer, reward):
            print("CONGRATULATIONS! You became a CROREPATI! 🥳🎊")
            print(f"Here is your {10000000} rupees. ENJOY!! 💸🎉")
        else:
            exit()
    else:
        if not check_answers(question, answer, reward):
            exit()
        total_reward += reward



