# # # # # #question 1:
# # # # # # while True:
# # # # # #     age=int(input("enter your age:"))
# # # # # #     if age <18:
# # # # # #         print("you are minor")
# # # # # #     elif age>18 and age<60: 
# # # # # #         print("you are adult")  
# # # # # #     elif age>60:
# # # # # #         print("you are a senior citizen")
# # # # # #     else:
# # # # # #         print("stop")    


# # # # # #question2:
# # # # # # while (userinput:=input('Enter a input: '))!='bus':
# # # # # #     print('waiting')
# # # # # # else:
# # # # # #     print('wait is over')


# # # # ##question3:

# # # # # while True:
# # # # #     user_input = input("Enter the name of a fruit: ")
# # # # #     if user_input == "apple":
# # # # #         print("You got it!")
# # # # #         break
# # # # #     else:
# # # # #         print("Try again")


# # # # # # #question5
# # # # # # Ratings = ['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']
# # # # # # content_rating={}
# # # # # # i=0
# # # # # # while i<len(Ratings):
# # # # # #     if Ratings[i] in content_rating:
# # # # # #         content_rating[Ratings[i]]=content_rating.get(Ratings[i],0)+1
# # # # # #     else:
# # # # # #         content_rating[Ratings[i]]=1
# # # # # #     i+=1        
# # # # # # print(content_rating)


# # # # # #question6
# # # # # import random 
# # # # # number=random.randint(1, 10)
# # # # # attempts=0
# # # # # print("Guess the number between 1 and 10!")
# # # # # while True:
# # # # #     guess=int(input("Your guess: "))
# # # # #     attempts+=1
# # # # #     if guess<number:
# # # # #         print("Too low, try higher.")
# # # # #     elif guess>number:
# # # # #         print("Too high, try lower.")
# # # # #     else:
# # # # #         print(f"Nice! The number was {number}.")
# # # # #         print(f"You got it in {attempts} attempts.")
# # # # #     break


# # # # #question7
# # # # correct_username ="admin"
# # # # correct_password ="1234"
# # # # attempts =0
# # # # while attempts <3:
# # # #     username=input("Enter username: ")
# # # #     password=input("Enter password: ")
# # # #     if username==correct_username and password==correct_password:
# # # #         print("Login successful")
# # # #         break
# # # #     else:
# # # #         print("Invalid credentials, try again.")
# # # #         attempts=attempts + 1
# # # # if attempts==3:
# # # #     print("Too many failed attempts.")


# # # #question8
# # # import random
# # # while True:
# # #     num1=random.randint(1, 30)
# # #     num2=random.randint(1, 30)
# # #     answer=int(input(f"What is {num1} x {num2}? (type 'exit' to stop): "))
# # #     if answer=="exit":
# # #         print("Quiz ended.")
# # #         break
# # #     if int(answer)==num1*num2:
# # #         print("Correct!")
# # #     else:
# # #         print("Incorrect, try again.")

# # #question9
# # while True:
# #     user_input=input("Enter a number (or type 'exit' to stop): ")

# #     if user_input=="exit":
# #         print("Program ended.")
# #         break
# #     num=int(user_input)
# #     if num<=1:
# #         print("The number is not prime.")
# #     else:
# #         is_prime=True
# #         for i in range(2, num):
# #             if num % i==0:
# #                 is_prime=False
# #                 break
# #         if is_prime:
# #             print("The number is prime.")
# #         else:
# #             print("The number is not prime.")


# # question10
# secret_word = "python"
# while True:
#     guess=input("Guess the secret word (or type 'quit' to exit): ")
#     if guess=="quit":
#         print("Program exited.")
#         break
#     if guess==secret_word:
#         print("Congratulations, you guessed the word!")
#         break
#     else:
#         print("Incorrect, try again.")


# # question11
count=0
while count<3:
    name=input("Enter a name: ")
    if name=="good luck":
        count=count+1
        if count<3:
            print("You typed the same word", count, "times.")
        else:
            print("You typed good luck three times.")