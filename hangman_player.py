import hangman_creator

hangman = hangman_creator.Hangman('E:\\wordlist.txt')
hangman.chose_the_word()
hangman.fill_the_word_status()

while True:
    hangman.get_word_status()
    hangman.guess_the_letter()

    if(hangman.attems_remaining == 0):
        print('Out of Attemps The Game over! ''The Word Was',format((hangman.chosen_word)))
        break

    elif(hangman.chosen_word == ''.join(hangman.word_status) ):
        print("Hurray You Won The Game")
        break
