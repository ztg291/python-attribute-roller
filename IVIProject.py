import time
import random
name = input("What would you like your username to be? ")
time.sleep(1)
while True:
    change_username = input("Would you like to change your username? ")
    if change_username.lower() == "yes":
        time.sleep(1)
        name = input("What would you like your new username to be? ")
        time.sleep(1)
    elif change_username.lower() == "no":
        time.sleep(1)
        print(f"Welcome {name}!")
        break
    else:
        print("Please enter yes or no.")

retry_count = 6
print("You will have 6 different attributes to roll for using the 1d20 dice.")
time.sleep(3)
print("The attributes are: Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma.")
time.sleep(3)
print("If you are curious what each one does please refer to the trello board for more information.")
time.sleep(3)
print("You will be granted a total of 6 rerolls for your attributes, so use them wisely.")
time.sleep(3)

strength = 0
dexterity = 0
constitution = 0
intelligence = 0
wisdom = 0
charisma = 0

while True:
    start_attributes = input("Are you ready to roll for your attributes? ")
    if start_attributes.lower() == "yes":
        time.sleep(1)
        print("Rolling for your attributes...")
        time.sleep(3)
        strength = random.randint(1, 20)
        dexterity = random.randint(1, 20)
        constitution = random.randint(1, 20)
        intelligence = random.randint(1, 20)
        wisdom = random.randint(1, 20)
        charisma = random.randint(1, 20)
        print(f"Strength: {strength}")
        print(f"Dexterity: {dexterity}")
        print(f"Constitution: {constitution}")
        print(f"Intelligence: {intelligence}")
        print(f"Wisdom: {wisdom}")
        print(f"Charisma: {charisma}")
        break
    elif start_attributes.lower() == "no":
        time.sleep(2)
        print("Please type 'yes' when you are ready to roll for your attributes.")
        time.sleep(2)
    else:
        time.sleep(1)
        print("Please enter yes or no.")

while retry_count > 0:
    attempt_retry = input(f"You have {retry_count} rerolls. Would you like to reroll any of your attributes? (yes/no) ")
    if attempt_retry.lower() == "yes":
        time.sleep(2)
        choose_attribute_reset = input("Which attribute would you like to reroll? ").strip().lower()
        time.sleep(2)
        if choose_attribute_reset == "strength":
            strength = random.randint(1, 20)
            print(f"Strength has been rerolled to: {strength}")
            time.sleep(2)
            retry_count -= 1
        elif choose_attribute_reset == "dexterity":
            dexterity = random.randint(1, 20)
            print(f"Dexterity has been rerolled to: {dexterity}")
            time.sleep(2)
            retry_count -= 1
        elif choose_attribute_reset == "constitution":
            constitution = random.randint(1, 20)
            print(f"Constitution has been rerolled to: {constitution}")
            time.sleep(2)
            retry_count -= 1
        elif choose_attribute_reset == "intelligence":
            intelligence = random.randint(1, 20)
            print(f"Intelligence has been rerolled to: {intelligence}")
            time.sleep(2)
            retry_count -= 1
        elif choose_attribute_reset == "wisdom":
            wisdom = random.randint(1, 20)
            print(f"Wisdom has been rerolled to: {wisdom}")
            time.sleep(2)
            retry_count -= 1
        elif choose_attribute_reset == "charisma":
            charisma = random.randint(1, 20)
            print(f"Charisma has been rerolled to: {charisma}")
            time.sleep(2)
            retry_count -= 1
        else:
            time.sleep(2)
            print("Please choose one of the six attributes to reroll.")
            time.sleep(2)

    elif attempt_retry.lower() == "no":
        time.sleep(1)
        print("You have chosen to keep your current attributes.")
        time.sleep(1)
        break
    else:
        time.sleep(2)
        print("Please enter yes or no.")
        time.sleep(2)


print("Your final attributes are...")
time.sleep(3)
print(f"Strength: {strength}")
print(f"Dexterity: {dexterity}")
print(f"Constitution: {constitution}")
print(f"Intelligence: {intelligence}")
print(f"Wisdom: {wisdom}")
print(f"Charisma: {charisma}")

