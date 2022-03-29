import turtle
def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count = 0
    while(n != 1):
        if(n % 2) == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
        count = count + 1
    print("The count is: " + str(count))
    return count

def graphing(n):
  window = turtle.Screen()
  draw = turtle.Turtle()
  max_data = turtle.Turtle()
  max_so_far = 0
  draw.speed(0)
  max_data.speed(0)
  window.setworldcoordinates(0, 0, 10, 10)
  iteration = 0
  for i in range(1, n+1):
    result = seq3np1(i)
    if (result > max_so_far):
      max_so_far = result
      iteration = i
      max_data.clear()
    window.setworldcoordinates(0,0,i+10,max_so_far+10)
    draw.goto(i, result)
    data = "maximum so far: iteration: " +str(iteration) + " result " + str(max_so_far)
    max_data.up()
    max_data.goto(0, max_so_far)
    max_data.down()
    max_data.write(data)
  window.exitonclick()

def main():
  upper_bound = int(input("Enter a postitive value for the upper bound of the range: "))
  if (upper_bound < 0):
    exit()
  for start in range(upper_bound):
    print(f"Current value of start is {start+1}")
    seq3np1(start+1)
  graphing(100)
main()
