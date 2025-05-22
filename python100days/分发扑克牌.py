# 扑克

def create_poker():
    charlist = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    colorlist = ['♠', '♥', '♣', '♦']
    poker = [color + char for color in colorlist for char in charlist] 
    poker.append('小王')
    poker.append('大王')
    print("创造扑克:")
    print(poker)

    return poker

def shuffle_poker(poker):
    import random
    random.shuffle(poker)
    print("洗牌:")
    print(poker)
    return poker


class User:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
    
    def show_cards(self):
        print(f"{self.name}的牌: {', '.join(self.cards)}")
    
    

poker = create_poker()
poker = shuffle_poker(poker)
user1 = User("小明", poker[:13])
user2 = User("小红", poker[13:26])
user3 = User("小刚", poker[26:39])
user1.show_cards()
user2.show_cards()
user3.show_cards()
