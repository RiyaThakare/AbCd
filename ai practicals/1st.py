def simple_reflex_agent(location, room_status):
    if room_status[location] == "Dirty":
        print(f"Room {location} is Dirty.")
        print("Action: SUCK")
        room_status[location] = "Clean"
    else:
        if location == "A":
            print("Room A is Clean.")
            print("Action: Move Right to Room B")
            location = "B" 
        elif location == "B":
            print("Room B is Clean.")
            print("Action: Move down to location C")
            location = "C"
        else:
            print("Room C is Clean.")
            print("Action: Move up to Room A")
            location = "A"
    return location, room_status 

location = input("Enter starting location(A/B/C): ").upper()
room_status ={
    "A": input("Enter status of room A: ").capitalize(),
    "B": input("Enter status of room B: ").capitalize(),
    "C": input("Enter status of room C: ").capitalize()
}
print("Initial location: ", location)
print("Status of ", location, ":", room_status[location])
print()
while True:
    location, room_status = simple_reflex_agent(location, room_status)
    if (room_status["A"] == "Clean" and
        room_status["B"] == "Clean" and
        room_status["C"] == "Clean"):
        print("All rooms are clean.")
        print("Action: No operation")
        break
