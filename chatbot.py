def greet(user_input):
    wlc_txt = ["hello","hi","hola"]
    return any(greeting in user_input.lower() for greeting in wlc_txt)

def chatbot(user_input):
    if greet(user_input):
       return "Hello i am chatbot how are you!"
    elif "fine" in user_input.lower():
        return "Thats good Keep working"
    elif "not" in user_input.lower():
        return "oh sorry to hear that! Still Keep trying"
    else:
        return "Did not understand that"

while True:
    user_input = input("You :")
    
    if user_input.lower() == 'exit':
        print("Chatbot: Have a great bye")
        break
    
    response = chatbot(user_input)
    print("Chatbot: ",response)
    

   

    