ball_x = 350
ball_y = 600
ball_inital_speed = 0
ball_inital_height = 600
ball_speed = sqrt(2 * 9.81 * ball_inital_height - 100)
time = 0
time_change = 0.3
gravity = -9.81
ground_height = 100


def setup():
    size(700, 700)

def draw():
    translate(0,700)
    scale(1,-1)
    
    # Clear the previous frame
    background(0, 0, 0)
    
    # Draw the ground
    stroke(255, 0, 0)
    line(0, ground_height, 700, ground_height)
    
    # Draw the ball
    fill(255, 255, 0)
    ellipse(ball_x, ball_y, 50, 50)
    
    # Update the ball's position
    update_object_position()
    
    
def update_object_position():
    global ball_y
    global time
    global ball_speed
    global ball_inital_speed
    global ball_inital_height
    
    ball_y = (ball_inital_speed * time) + (0.5 * gravity * (time ** 2)) + ball_inital_height
    time = time + time_change
    
    if ball_y - 25 <= ground_height:
        ball_inital_speed = ball_speed * 0.5
        ball_speed = ball_inital_speed
        time = 0 
        ball_y = 126
        ball_inital_height = 126

    
