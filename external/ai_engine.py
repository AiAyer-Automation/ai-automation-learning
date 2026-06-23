
def smart_ai(text):
    # This is a mock function that simulates an AI response.
    # In a real implementation, this function would call an AI model or service.
    text_lower = text.lower()

    #task commend 
    if "add task" in text:
        task = text_lower.replace("add task:", "").strip()
        return {
            "action": "create_task",
            "task": task
        } 
    #explain
    if "flask" in text_lower:
        return "Flask is a lightweight web framework for Python that allows you to build web applications quickly and easily."
    if "python" in text_lower:
        return "Python is a versatile programming language known for its simplicity and readability."  
    if"bye" in text:
        return "Goodbye! Have a great day!" 
    return {
        "action": "unknown",
        "message": "I'm not sure how to respond to that."
    }