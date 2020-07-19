import time
import random
future_villan = ["Robots", "Cyber-Aliens", "Apes"]
past_villan = ["Dinosour", "Dragon", "Nagini"]
other_dimension = ["Thanos", "Joker", "Ultron"]
f_v = random.choice(future_villan)
p_v = random.choice(past_villan)
o_d = random.choice(other_dimension)


def delay(msge):
    print(msge)
    time.sleep(2)


def intro():
    delay("you wake up early for the test")
    delay("you eat your breakfast then go to the lab")
    delay("today is the big day")
    delay("today,you test")
    delay("THE TIME MACHINE")


def play_again():
    while True:
        again = input("do you want to play again (y)/(n)")
        if again == "y":
            game()
            break
        elif again == "n":
            delay("goodbye")
            break
        else:
            print("sorry i do not understand,choose (y) or (n)")


def future():
    delay("you feel dizzy for a sec,then")
    delay("now you are in the future")
    delay("you felt something strange that there is no people in streets")
    delay("after wandring for some time you realized that"
          " the "+f_v+"has taken over the planet\n")
    while True:
        save_them = input("you know there is still people living in burrows"
                          ",save them or go back\n"
                          "1.save them\n"
                          "2.go back\n")
        if save_them == "1":
            while True:
                fight = input("would you choose to fight or make peace\n"
                              "1.fight\n"
                              "2.peace\n")
                if fight == "1":
                    delay("you gather all humans left and launch an attack on"
                          " the "+f_v+" creatures who killed our people")
                    delay("but they have a lot of weapons"
                          " and they are much more than you")
                    delay("you lost the war and the last human was killed"
                          " by the "+f_v+" leader because of you")
                    delay("                              GAME IS OVER")
                    break
                elif fight == "2":
                    delay("you managed to meet with the "+f_v+" leader")
                    delay("you convinced him somehow that humans could be "
                          "useful if they lived with them and worked together")
                    delay("you made a deal with "+f_v+" that saved humanity")
                    delay("                          CONGRATULATIONS YOU WON")
                    break
                else:
                    delay("sorry,choose wisely between 1 and 2")
            break
        elif save_them == "2":
            time_travel()
            break
        else:
            delay("sorry,try again")
    play_again()


def past():
    delay("you feel a little bit dizzy")
    delay("then you find yourself in a desert")
    delay("while you were looking for water and food you found a great "+p_v)
    delay("too bad it saw you too")
    delay("you started running for your life\n")
    hard_choice = input("your device fell from you and broke down\n"
                        "get it or no (y)/(n)").lower()
    if hard_choice == "y":
        percent = random.randint(1, 10)
        if percent > 7:
            delay("you got the device")
            delay("and ran away safely")
            delay("you are finally safe")
            delay("you managed to fix the device and went back safely")
            delay("YOU WON but,go back check other solutions")
        else:
            delay("before you even think to act the "+p_v+" ate you alive")
            print("                                          GAME IS OVER")
    elif hard_choice == "n":
        delay("you ran away from the "+p_v)
        delay("you hid in a small cave")
        delay("you found 2 types of metal:\niron and rusty iron-like metal\n")
        while True:
            weapon = input("which metal will you use"
                           "\n1.iron\n2.rusty iron-like metal")
            if weapon == "1":
                delay("you made a great weapon")
                delay("you went back to the "+p_v+" nest")
                delay("you killed the "+p_v+" and got the device back")
                delay("then you went home safely")
                print("                       CONGRATULATIONS YOU WON")
                break
            elif weapon == "2":
                delay("the second you touched the metal you"
                      " started to burn and suffered alot before dying")
                delay("         YOU LOST,I BET YOU DIDN'T SEE THAT COMING")
                break
            else:
                delay("sorry try again and choose 1 or 2\n")
    else:
        delay("WOW,you discoverd that magical word")
        delay("now the "+p_v+" is dead")
        delay("you are safe")
        delay("CONGRATULATIONS FOR WINNING AND"
              " DISCOVRING THE MAGICAL WORD ("+hard_choice+")")
    play_again()


def the_unknown_dimension():
    delay("what have you done")
    delay("your input doesn't match any of the time lines")
    delay("the time machine threw you to an unknown dimension")
    delay("you found yourself in a dimension "
          "where the ruler of the worlds is "+o_d)
    delay("the great villan "+o_d+" knew that you came from other dimension\n")
    while True:
        trap = input("he invited you to his place\n1.go\n2.stay\n")
        if trap == "1":
            delay("you went to meet him and he started to speak with you")
            delay("he asked you about his current place in your dimension\n")
            while True:
                lie = input("will you lie to him or tell the "
                            "truth\n1.lie\n2.tell truth")
                if lie == "1":
                    delay("he thanks you and provides you with the"
                          " tools needed to go back to your dimension")
                    delay("but he sends one of his people"
                          " after you to see if you were a liar")
                    delay("and that man finds out and kill you")
                    delay("            YOU LOST BECAUSE YOU LIED")
                    break
                elif lie == "2":
                    delay("you tell him the hard truth about his fate")
                    delay("he gives the order to kill you")
                    delay("you still have a chance of living\n")
                    while True:
                        betrayel = input("you live if you told him how"
                                         " to save himself in"
                                         " your deminsionn\n"
                                         "will you betray "
                                         "your world(y)/(n)??").lower()
                        if betrayel == "y":
                            delay("YOU LIVED but LOST YOUR HUMANITY")
                            break
                        elif betrayel == "n":
                            delay("YOU DIED AS A HERO WHO "
                                  "REFUSED TO BETRAY HIS PEOPLE")
                            break
                        else:
                            delay("choose wether to betray or die (y)/(n)")
                    break
                else:
                    delay("sorry,choose 1 or 2")
            break
        elif trap == "2":
            delay("you thought that the villan"
                  " will never find you in your new hideout")
            delay("but he did and sent assassins to finish you off")
            delay("the device you are making is not finished yet")
            delay("there is a high percentage "
                  "of dying in a very painful way\n")
            while True:
                surrender = input("will you try the device or surrender to"
                                  " the assassins and die in merciful way\n"
                                  "1.try device\n"
                                  "2.surrender to death")
                if surrender == "1":
                    percentage = random.randint(0, 100)
                    if percentage > 70:
                        delay("the device worked")
                        delay("you went back home safely")
                        delay("         YOU MANAGED TO LIVE,CONGRATS")
                    else:
                        delay("you died in a very painful way")
                        delay("your particles is detaching from each other")
                        delay("                     YOU DIED PAINFULLY")
                    break
                elif surrender == "2":
                    delay("the assassins comes and kill you mercifully")
                    delay("                     YOU DIED MERCIFULLY")
                    break
                else:
                    delay("please choose 1 or 2")
            break
    else:
        delay("please choose 1 or 2")
    play_again()


def time_travel():
    t_line = input("which time do you want to travel to??\n"
                   "1.future\n"
                   "2.past\n")
    if t_line == "1":
        future()
    elif t_line == "2":
        past()
    else:
        the_unknown_dimension()


def game():
    intro()
    time_travel()
game()
