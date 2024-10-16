# def chatbot():
#     print("Hello! I'm here to help you with your questions about The Entrepreneurship Network.")
#     print("You can ask me about the company, its vision, Pay After Placement, or anything else.")

#     que = {
#         1: "The Entrepreneurship Network",
#         2: "Free site for education, Free site for mentorship, Free site for resume building, Free site for influencer marketing, Free site for training, Free site for AI tools, Free site for idea to expansion",
#         3: "Delhi, India",
#         4: "Our vision is to revolutionize education through cutting-edge technology, creating an inclusive learning ecosystem that integrates innovative tools, personalized learning experiences, and global connectivity. By leveraging AI, data analytics, and immersive content, we inspire curiosity, cultivate critical thinking, and unlock the full potential of every learner.",
#         5: "Pay After Placement (PAP) is a payment model where students pay tuition fees after securing a job.",
#         6: "No upfront fees, repayment starts after securing a job with a minimum salary threshold.",
#         7: "The Entrepreneurship Network offers valuable insights into business planning and funding opportunities for your e-learning platform.",
#         8: "The repayment period is typically pre-determined but can vary depending on the agreement.",
#         9: "We offer internships in various development fields, including Frontend, Android, MERN Stack, Python, and Backend, providing hands-on experience and mentorship. Our programs focus on real-world projects to enhance skills and prepare participants for successful careers in tech.",
#         10: "To identify the demographic and market segment the company serves.",
#         11: "To understand the cultural foundation and ethical stance of the organization.",
#         12: "Our main goals in the next few years are to expand our service offerings, enhance technological capabilities, and strengthen industry partnerships to empower aspiring entrepreneurs and developers.",
#         13: "We've embraced flexibility by staying on top of industry trends and adjusting our services to meet evolving needs. Our team regularly collaborates to brainstorm fresh ideas and keep things exciting for our clients and interns!"
#     }

#     questions_list = {
#         1: "What is the name of the company?",
#         2: "What products or services does the company offer?",
#         3: "Where is the company headquartered?",
#         4: "What is the company's mission or vision?"
#     }

#     first_other_questions_list = {
#         5: "What is Pay After Placement?",
#         6: "How does Pay After Placement work?",
#         7: "Is it worth pursuing a course with TEN?",
#         8: "Can I choose how long I take to repay?"
#     }

#     second_other_questions_list = {
#         9: "What products or services does your company offer?",
#         10: "Who is your target audience or ideal customer?",
#         11: "What are the company’s key values or principles?",
#         12: "What are the main goals or objectives for the company in the next few years?",
#         13: "How has the company adapted to changes in the market or industry trends?"
#     }

#     def display_questions(q_list):
#         for num, question in q_list.items():
#             if question:
#                 print(f"{num}. {question}")

#     print("You can ask me by typing the question number (1-4) to get the answer.")
#     display_questions(questions_list)

#     shown_stages = {"stage1": False, "stage2": False}

#     while True:
#         if shown_stages["stage2"]:
#             user_input = input("Ask your question (type 'quit' to exit): ").strip().lower()
#         else:
#             user_input = input("Ask your question (type 'quit' to exit or type 'other' for more questions): ").strip().lower()
#             # print("\n")
#         if user_input == "quit":
#             print("Thank you for response.")
#             print("You can ask question here. How can I help?")
#             break

#         try:
#             question_number = int(user_input)

#             if 1 <= question_number <= 4 and not shown_stages["stage1"]:
#                 if que[question_number]:
#                     print(que[question_number])
#                 else:
#                     print("No information available for this question.")

#             elif 5 <= question_number <= 8 and shown_stages["stage1"] and not shown_stages["stage2"]:
#                 print(que[question_number])

          
#             elif 9 <= question_number <= 13 and shown_stages["stage2"]:
#                 print(que[question_number])

#             else:
#                 print("Please select a valid option or type 'other' to see more options.")

#         except ValueError:
          
#             if not shown_stages["stage1"] and user_input == "other":
#                 print("\nYou chose 'other', let's explore more options!")
#                 print("Here are more questions you can ask (5-8):")
#                 display_questions(first_other_questions_list)
#                 shown_stages["stage1"] = True

         
#             elif shown_stages["stage1"] and not shown_stages["stage2"] and user_input == "other":
#                 print("\nYou chose 'other' again! Let's move to more advanced questions.")
#                 print("Here are more questions you can ask (9-13):")
#                 display_questions(second_other_questions_list)
#                 shown_stages["stage2"] = True

#             else:
#                 print("Please type a valid question number or 'other' to see more questions.")

# chatbot()

# new code----------------------------------------------------------------------------------------------------------------------
def chatbot():
    print("👋 Hello! I'm here to assist you with questions about The Entrepreneurship Network.")
    print("You can ask me about the company 😊, its services, Pay After Placement, internships, and more.")

    questions = {
        1: "What is the name of the company?",
        2: "What products or services does the company 💬 offer?",
        3: "Where is the company headquartered?",
        4: "How do I apply for an internship 👈 ?",
        5: "What is Pay After Placement?",
        6: "How does Pay After Placement work?",
        7: "Can I see a list of 📚 courses available for beginners?",
        8: "Can I choose how long I take to repay?",
        9: "Who is your target audience or ideal customer?",
        10: "What are the company’s key values or principles?",
        11: "What are the main goals for the company in the next few years?",
        12: "How has the company adapted to market trends?",
        13: "What internships do you offer ⚡ ?"
    }

    answers = {
        1: "The Entrepreneurship 😊 Network",
        2: "We provide education 🎓, mentorship, training, and knowledge👩‍💻 about AI tools, along with influencer marketing and career-building programs.",
        3: "Delhi, India",
        4: "You can apply for internships through our career page 👉 : https://career.entrepreneurshipnetwork.net/",
        5: "Pay After Placement 💸 (PAP) is a model where students pay tuition fees only after securing a job.",
        6: "No upfront fees. Repayment starts after securing a job with a minimum salary threshold.",
        7: "We offer 21 courses. Check them out here👉 : https://ten-official.vercel.app/Courses",
        8: "The repayment period is usually pre-determined but can vary based on the agreement.",
        9: "Our target audience includes aspiring entrepreneurs, developers, and students looking to enhance their skills.",
        10: "Our key values include innovation,⚡ mentorship, and empowering entrepreneurs.",
        11: "Our goals are to expand services, enhance technology, and strengthen partnerships in the coming years.",
        12: "We adapt by staying updated with industry trends and evolving our services to meet current needs.",
        13: "We offer internships in areas such as 💻 Frontend, Android, MERN Stack, Python, and Backend."
    }

    def display_questions(start, end):
        for i in range(start, end+1):
            print(f"{i}. {questions[i]}")

    current_stage = 1
    while True:
        if current_stage == 1:
            print("\nPlease select a question from 1 to 4:")
            display_questions(1, 4)
        elif current_stage == 2:
            print("\nPlease select a question from 5 to 8:")
            display_questions(5, 8)
        elif current_stage == 3:
            print("\nPlease select a question from 9 to 13:")
            display_questions(9, 13)

        user_input = input("Enter the question number or type 'next' for more questions: ").strip().lower()

        if user_input == "quit":
            print("Thank you for using the chatbot. Goodbye!")
            break

        elif user_input == "next":
            if current_stage < 3:
                current_stage += 1
            else:
                print("You have reached the last set of questions.")
            continue

        try:
            question_number = int(user_input)
            if (current_stage == 1 and 1 <= question_number <= 4) or \
               (current_stage == 2 and 5 <= question_number <= 8) or \
               (current_stage == 3 and 9 <= question_number <= 13):
                print(answers[question_number])

                # Automatically quit after answering a question from 9-13
                if current_stage == 3 and 9 <= question_number <= 13:
                    print("You can ask 🤔 questions here.\nHow can I help?")
                    print("Did that answer help, or are you looking for something else?")
                    feedback = input("Thank you for your response 😇.\nDid that answer help? (yes/no): ").strip().lower()

                    if feedback == "yes":
                        print("I'm glad I could help 😎 ")
                    elif feedback == "no":
                        print("I'm sorry 😑 to hear that. Let me know if there's anything else I can assist with.")

                    break
            else:
                print("Invalid question number for this stage. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid question number or type 'next' for more questions.")

chatbot()

