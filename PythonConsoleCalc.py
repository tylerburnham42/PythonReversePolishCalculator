command_weights = {
    "(": 1,
    "+": 2,
    "-": 2,
    "*": 3,
    "/": 3,
    }
command_functions = {
    "+": lambda x,y : x+y,
    "-": lambda x,y : x-y,
    "*": lambda x,y : x*y,
    "/": lambda x,y : x/y,
    }

def is_float(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def convert_to_postfix(expression_list):
    """ This function takes a list of split strings and converts
        it into a reverse polish notation expression.
        The algorighm is the Shunting-yard algorithm it can be found here:
        https://en.wikipedia.org/wiki/Shunting-yard_algorithm """

    stack = []
    rpn = []
    for item in expression_list:
        
        if(is_float(item)):
            rpn.append(float(item))

        elif(item == "("):
            stack.append(item)
            

        elif(item == ")"):
                    
            #Pop all the opperators untill the "(" is found 
            while(len(stack) and stack[-1] != "("):
                rpn.append(stack.pop())
                
            #Remove the '('
            stack.pop()

        #Check if the item is an opperator
        elif(item in command_weights):

            #If the item on top of the stack is less then the current
            #add the item to the rpn list
            while(len(stack) and command_weights[item] <= command_weights[stack[-1]]):
                rpn.append(stack.pop())
                
            stack.append(item)

    #Add any remaining opperations left on the stack
    while(len(stack)):
        rpn.append(stack.pop())

    return rpn

def evalulate_postfix(postfix_list):
    """ This is a fuction to take a mixed list of floats and
    opperations represented as characters in reverse polish notation
    such as [1,2,"+"] and find teh result. The algorthm was taken from:
    https://en.wikipedia.org/wiki/Reverse_Polish_notation """
    
    stack = []
    for item in postfix_list:
        if(type(item) == float):
            stack.append(item)
            
        else:
            if(len(stack) < 2):
                print("Invalid Expression")
                return 0
            
            value_one = stack.pop()
            value_two = stack.pop()
            result = command_functions[item](value_two,value_one)
            stack.append(result)

    if not len(stack):
        print("Invalid Expression")
        return 0

    return stack[0]
    
if __name__ == '__main__':
    expression_list = input().strip().split(" ")
    postfix_list = convert_to_postfix(expression_list)
    result = evalulate_postfix(postfix_list)
    print(result)

