def chatbot():
    print("Hello! I'm here to help you with your questions about The Entrepreneurship Network.")
    print("You can ask me about the company, its vision, Pay After Placement, or anything else.")

    que = {
        1: "The Entrepreneurship Network",
        2: "Free site for education, Free site for mentorship, Free site for resume building, Free site for influencer marketing, Free site for training, Free site for AI tools, Free site for idea to expansion",
        3: "Delhi, India",
        4: "Our vision is to revolutionize education through cutting-edge technology, creating an inclusive learning ecosystem that integrates innovative tools, personalized learning experiences, and global connectivity. By leveraging AI, data analytics, and immersive content, we inspire curiosity, cultivate critical thinking, and unlock the full potential of every learner.",
        5: "Pay After Placement (PAP) is a payment model where students pay tuition fees after securing a job.",
        6: "No upfront fees, repayment starts after securing a job with a minimum salary threshold.",
        7: "The Entrepreneurship Network offers valuable insights into business planning and funding opportunities for your e-learning platform.",
        8: "The repayment period is typically pre-determined but can vary depending on the agreement.",
        9: "We offer internships in various development fields, including Frontend, Android, MERN Stack, Python, and Backend, providing hands-on experience and mentorship. Our programs focus on real-world projects to enhance skills and prepare participants for successful careers in tech.",
        10: "To identify the demographic and market segment the company serves.",
        11: "To understand the cultural foundation and ethical stance of the organization.",
        12: "Our main goals in the next few years are to expand our service offerings, enhance technological capabilities, and strengthen industry partnerships to empower aspiring entrepreneurs and developers.",
        13: "We've embraced flexibility by staying on top of industry trends and adjusting our services to meet evolving needs. Our team regularly collaborates to brainstorm fresh ideas and keep things exciting for our clients and interns!"
    }

    questions_list = {
        1: "What is the name of the company?",
        2: "What products or services does the company offer?",
        3: "Where is the company headquartered?",
        4: "What is the company's mission or vision?"
    }

    first_other_questions_list = {
        5: "What is Pay After Placement?",
        6: "How does Pay After Placement work?",
        7: "Is it worth pursuing a course with TEN?",
        8: "Can I choose how long I take to repay?"
    }

    second_other_questions_list = {
        9: "What products or services does your company offer?",
        10: "Who is your target audience or ideal customer?",
        11: "What are the company’s key values or principles?",
        12: "What are the main goals or objectives for the company in the next few years?",
        13: "How has the company adapted to changes in the market or industry trends?"
    }

    def display_questions(q_list):
        for num, question in q_list.items():
            if question:
                print(f"{num}. {question}")

    print("You can ask me by typing the question number (1-4) to get the answer.")
    display_questions(questions_list)

    shown_stages = {"stage1": False, "stage2": False}

    while True:
        if shown_stages["stage2"]:
            user_input = input("Ask your question (type 'quit' to exit): ").strip().lower()
        else:
            user_input = input("Ask your question (type 'quit' to exit or type 'other' for more questions): ").strip().lower()
            # print("\n")
        if user_input == "quit":
            print("Thank you for response.")
            print("You can ask question here. How can I help?")
            break

        try:
            question_number = int(user_input)

            if 1 <= question_number <= 4 and not shown_stages["stage1"]:
                if que[question_number]:
                    print(que[question_number])
                else:
                    print("No information available for this question.")

            elif 5 <= question_number <= 8 and shown_stages["stage1"] and not shown_stages["stage2"]:
                print(que[question_number])

          
            elif 9 <= question_number <= 13 and shown_stages["stage2"]:
                print(que[question_number])

            else:
                print("Please select a valid option or type 'other' to see more options.")

        except ValueError:
          
            if not shown_stages["stage1"] and user_input == "other":
                print("\nYou chose 'other', let's explore more options!")
                print("Here are more questions you can ask (5-8):")
                display_questions(first_other_questions_list)
                shown_stages["stage1"] = True

         
            elif shown_stages["stage1"] and not shown_stages["stage2"] and user_input == "other":
                print("\nYou chose 'other' again! Let's move to more advanced questions.")
                print("Here are more questions you can ask (9-13):")
                display_questions(second_other_questions_list)
                shown_stages["stage2"] = True

            else:
                print("Please type a valid question number or 'other' to see more questions.")

chatbot()
