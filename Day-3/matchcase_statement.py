#match = what you'r comaparing
#case = value or pattern to match againts
# _ = default case( like else)

#example

color = input("enter color:")

match color:
    case "red":
        print("stop")
    case "green":
        print("go")
    case "yellow":
        print("look")
    case _ :
        print("wrong color") 