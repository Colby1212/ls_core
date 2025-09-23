def rps(fist1, fist2):
    if fist1 == "rock":
        return "paper" if fist2 == "paper" else "rock"
    elif fist1 == "paper":
        return "scissors" if fist2 == "scissors" else "paper"
    else:
        return "rock" if fist2 == "rock" else "scissors"

#What does the following code output?

print(rps4(rps3(rps1("rock", "paper"), rps2("rock", "scissors")), "rock"))

(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))

layer 1 --> (rps4(rps3(rps1),(rps2)), rock)
layer 2 --> rps3("paper"), rps2("rock")
layer 3/4 --> rps1( "rock", "paper") rps2("rock", "scissors")


rps1 ==> "paper"
rps2 ==> "rock"
rps3 ==> "paper"
rps 4 ==> "paper"


This code outputs "paper". 