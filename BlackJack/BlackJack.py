import random

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    for suit in suits:
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))

        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_card(frame):
    next_card = deck.pop(0)
    deck.append(next_card)
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    return next_card


def score_hand(hand):
    score = 0
    ace = False
    for nextCard in hand:
        cardValue = nextCard[0]
        if cardValue == 1 and not ace:
            ace = True
            cardValue = 11
        score += cardValue
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    dealerScore = score_hand(dealerHand)
    while 0 < dealerScore < 17:
        dealerHand.append(deal_card(dealerCardFrame))
        dealerScore = score_hand(dealerHand)
        dealerScoreLabel.set(dealerScore)

    playerScore = score_hand(playerHand)
    if playerScore > 21:
        resultText.set("Dealer wins!")
    elif dealerScore > 21 or dealerScore < playerScore:
        resultText.set("Player Wins!")
    elif dealerScore > playerScore:
        resultText.set("Dealer Wins!")
    else:
        resultText.set("Draw!!!")


def deal_player():
    playerHand.append(deal_card(playerCardFrame))
    playerScore = score_hand(playerHand)

    playerScoreLabel.set(playerScore)
    if playerScore > 21:
        resultText.set("Dealer Wins!")


def mew_game():
    global dealerCardFrame
    global playerCardFrame
    global dealerHand
    global playerHand
    dealerCardFrame.destroy()
    dealerCardFrame = tkinter.Frame(cardFrame, background="green")
    dealerCardFrame.grid(row=0, column=1, sticky="ew", rowspan=2)
    playerCardFrame.destroy()
    playerCardFrame = tkinter.Frame(cardFrame, background="green")
    playerCardFrame.grid(row=2, column=1, sticky="ew", rowspan=2)
    resultText.set("")
    dealerHand = []
    playerHand = []
    deal_player()
    dealerHand.append(deal_card(dealerCardFrame))
    dealerScoreLabel.set(score_hand(dealerHand))
    deal_player()


def shuffle():
    random.shuffle(deck)


mainWindow = tkinter.Tk()
# Set up the screen and frames for the dealer and player
mainWindow.title("Black Jack")
mainWindow.geometry("640x480")
mainWindow.configure(background="green")
resultText = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=resultText)
result.grid(row=0, column=0, columnspan=3)

cardFrame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
cardFrame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

dealerScoreLabel = tkinter.IntVar()
tkinter.Label(cardFrame, text="Dealer", background="green", fg="White").grid(row=0, column=0)
tkinter.Label(cardFrame, textvariable=dealerScoreLabel, background="green", fg="white").grid(row=1, column=0)
# embedded frame to hold the card images
dealerCardFrame = tkinter.Frame(cardFrame, background="green")
dealerCardFrame.grid(row=0, column=1, sticky="ew", rowspan=2)

playerScoreLabel = tkinter.IntVar()
tkinter.Label(cardFrame, text="Player", background="green", fg="White").grid(row=2, column=0)
tkinter.Label(cardFrame, textvariable=playerScoreLabel, background="green", fg="White").grid(row=3, column=0)
# embedded frame to hold the card images
playerCardFrame = tkinter.Frame(cardFrame, background="green")
playerCardFrame.grid(row=2, column=1, sticky="ew", rowspan=2)

buttonFrame = tkinter.Frame(mainWindow)
buttonFrame.grid(row=3, column=0, columnspan=3, sticky="w")

dealerButton = tkinter.Button(buttonFrame, text="Dealer", command=deal_dealer)
dealerButton.grid(row=0, column=0)

playerButton = tkinter.Button(buttonFrame, text="Player", command=deal_player)
playerButton.grid(row=0, column=1, padx=10)

newGameButton = tkinter.Button(buttonFrame, text="New Game", command=mew_game)
newGameButton.grid(row=0, column=2, padx=10)

shuffleButton = tkinter.Button(buttonFrame, text="Shuffle", command=shuffle)
shuffleButton.grid(row=0, column=3)
# load cards
cards = []
load_images(cards)
print(cards)
# Create a new deck of cards and shuffle them
deck = list(cards)
shuffle()

# Create a lists to hold the hands
dealerHand = []
playerHand = []

mew_game()
mainWindow.mainloop()
