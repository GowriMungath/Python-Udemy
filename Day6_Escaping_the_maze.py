def turn_right():
     turn_left();
     turn_left();
     turn_left();
        
while front_is_clear():
    move()
turn_left()
      
        
while at_goal()!=True:
    if right_is_clear()==True:
        turn_right();
        move();
    elif front_is_clear():
        move();
    else:
        turn_left();
   
