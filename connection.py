from flask import Flask, request, jsonify

app = Flask(__name__)

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

@app.route('/get-response', methods=['POST'])
def get_response():
    user_message = request.json.get('message')
    
    # Here, you can implement logic based on the user message
    if user_message.isdigit() and int(user_message) in answers:
        response = answers[int(user_message)]
    else:
        response = "I'm not sure how to respond to that. Please ask about the company or choose a question number."

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
