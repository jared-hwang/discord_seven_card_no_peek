reds = {
    2: '<:pokertwored:805279427960242197>',
    3: '<:pokerthreered:805279190890577921>',
    4: '<:pokerfourred:805279427961159681>',
    5: '<:pokerfivered:805279190650716171>',
    6: '<:pokersixred:805278976607518731>',
    7: '<:pokersevenred:805279428544430110>',
    8: '<:pokereightred:805279191812800513>',
    9: '<:pokerninered:805279192261591090>',
    10: '<:pokertenred:805279145776250883>',
    11: '<:pokerjackred:805277442394030090>',
    12: '<:pokerqueenred:805279192064327680>',
    13: '<:pokerkingred:805279428250173441>',
    14: '<:pokeracered:805279428372463646>',
    1: '<:pokeracered:805279428372463646>'
}
blacks = {
    2: '<:pokerthreeblack:805277247057035264>',
    3: '<:pokerthreeblack:805277247057035264>',
    4: '<:pokerfourblack:805277492809039922>',
    5: '<:pokerfiveblack:805279118656405554>',
    6: '<:pokersixblack:805277514833592372>',
    7: '<:pokersevenblack:805278944499597362>',
    8: '<:pokereightblack:805279018987290654>',
    9: '<:pokernineblack:805279190650847273>',
    10: '<:pokertenblack:805277465420759070>',
    11: '<:pokerjackblack:805279428224745492>',
    12: '<:pokerqueenblack:805279063777214496>',
    13: '<:pokerkingblack:805279192123965460>',
    14: '<:pokeraceblack:805279428149248001>',
    1: '<:pokeraceblack:805279428149248001>'
}
suits = {
    'hearts': '<:pokerhearts:805279428116217857>',
    'clubs': '<:pokerclubs:805279428330520627>',
    'diamonds': '<:pokerdiamonds:805279428895965214>',
    'spades': '<:pokerspades:805279428266557470>'
}
hand_order = {
    'royal flush': 10,
    'straight flush': 9, 
    'four of a kind': 8,
    'full house': 7,
    'flush': 6,
    'straight': 5,
    'three of a kind': 4,
    'two pair': 3,
    'pair': 2,
    'high card': 1
}


def get_emoji_top(val, suit):
    if suit == 'clubs' or suit == 'spades':
        return blacks[val]
    else:
        return reds[val]

def get_emoji_bottom(val, suit):
    return suits[suit]

    