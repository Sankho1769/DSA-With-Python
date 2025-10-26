back_stack = []      
forward_stack = []   
current_page = "Home"

def visit_page(page):
    global current_page
    back_stack.append(current_page)
    current_page = page
    forward_stack.clear()
    print(f"Visited: {current_page}")

def go_back():
    global current_page
    if back_stack:
        forward_stack.append(current_page)
        current_page = back_stack.pop()
        print(f"Back to: {current_page}")
    else:
        print("No pages to go back to!")

def go_forward():
    global current_page
    if forward_stack:
        back_stack.append(current_page)
        current_page = forward_stack.pop()
        print(f"Forward to: {current_page}")
    else:
        print("No pages to go forward to!")

visit_page("Page A")
visit_page("Page B")
visit_page("Page C")
go_back()
go_back()
go_forward()
