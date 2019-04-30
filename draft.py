import random

def recursiveRename(numberedList):
    renamedList = []
    cardListFile = open("main_cube.txt","r")
    cardList = cardListFile.readlines()
    for entry in numberedList:
        if isinstance(entry, (list,)):
            renamedList.append(recursiveRename(entry))
        else:
            renamedList.append(cardList[entry].split("\n")[0])
    return renamedList

def makePacks(cubeSize, drafters, packs, cards):
    draftsize = drafters * packs * cards
    draftpool = random.sample(range(cubeSize), draftsize)
    print(draftpool)
    draft = []
    n = 0
    for i in range(packs):
        round = []
        draft.append(round)
        for j in range(drafters):
            pack = []
            round.append(pack)
            for k in range(cards):
                pack.append(draftpool[n])
                n += 1
    return draft


def score(card, perspective):
    return 0

def adjustScore(card, remainingPack, perspective):

    return


class draftPerspective:
    def __init__(self):
        self.human = False
        self.cardsTaken = []
        self.cardsSeen = []


def draftPacks(draft, drafters):
    draftPerspectives = []
    for i in range(drafters):
        draftPerspectives.append(draftPerspective())
    left = True
    for draftRound in draft:
        while draftRound[0]:
            drafterNumber = 0
            for pack in draftRound:
                scoredPack = []
                for card in pack:
                    scoredPack.append(score(card, draftPerspectives[drafterNumber]))
                bestCardIndex = 0
                draftPerspectives[drafterNumber].cardsTaken.append(pack.pop(bestCardIndex))
                cards
                drafterNumber += 1
            temp = draftRound.pop()
            draftRound.insert(0, temp)
            left = not left
    print(draftPerspectives)
    for drafter in draftPerspectives:
        print(drafter.cardsTaken)
        print(recursiveRename(drafter.cardsTaken))


def main():
    draft = makePacks(450, 8, 3, 15)
    print(draft)
    print(recursiveRename(draft))
    draftPacks(draft, 8)


if __name__ == "__main__":
    main()
