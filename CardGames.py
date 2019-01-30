# !/usr/bin/env python
# -*- coding: utf-8 -*-


"""
A 52 card set game
 Game Rules:
1. each player starts match with 4 cards in hand, a running card on table and the rest called the
    pick_set flipped downwards for picking.
2. the top card on table is called the running card
3. each card has a name which includes first_name and last_name. For example 10_of_clubs is a card name
    with 10 as first_name and clubs as the last_game.
4. a player can not throw cards of different first_name in a single except for 8 and queen cards
   combined with other type as elaborated below. see no. 6
5. there are five types in the 52 card set excluding jokers described below by their first names.
    ace = defender
    2, 3 = punisher
    4, 5, 6, 7, 9, 10 = normal
    8, queen = question
    king = kickback
    jack = skipper
    -------------------------------------------------
    each card carries some points with it as described below
    ace = 100
    2 = 50
    3 = 75
    4 = 4
    5 = 5
    6 = 6
    7 = 7
    8 = 8
    9 = 9
    10, jack, queen and king = 10

6. each card either accepts or denies another card to follow it depending on whether it is
    single throw or not.
    in a player's single throw, a player can throw a single card or more as long as
    they meet the following rules:
    Note: the last card to be thrown on the table is the running card
    -> a player can only throw a card on table that is can be accepted by the table's running card.
        to be accepted the card has to have the same first name as table's running card or the same
        last name as the table's running card. for example 7_of_diamonds is our running card,
        then 6_of_diamonds, 7_of_clubs are valid but 5_of_clubs isn't since either of it's two names
        matches the running card.
    -> no two normal cards of different first names can be thrown in a single throw
        for example 5_of_clubs and 5_of_spades is valid but 5_of_clubs and 6_of_clubs is invalid
        in a single throw.
    -> ace is valid on all cards i.e ace is accepted by all cards irrespective of their names
        for example, ace_of_diamonds can follow 4_of_clubs and 8_of_spades but the reverse is illegal.
    -> as long as question cards see rule no. 5 are valid on each other they can be combined irrespective
        of their first_names. for example [8_of_spades, queen_of_spades, queen_of_diamonds, 8_of_diamonds]
        can be thrown in a single throw; it is a valid set but [8_of_spades, queen_of_clubs, queen_of_diamonds,
        8_of_diamonds] is illegal/invalid set since card 1 and 2 have nothing in common. to make it valid,
        either throw 8_of_spades alone or combination of queen_of_clubs and queen_of_diamonds.
    -> if a player throws a card or more and the last card is a question, he/she has to answer the question by
        throwing another card that is accepted by the last card thrown. for example if the set
        [8_of_spades, queen_of_spades, queen_of_diamonds, 8_of_diamonds] is thrown he can either answer by
        any card with diamonds or ace in its name. if he does not have then he picks from pick set and the game
        moves to the next player.
        Note: no other type can be placed before question cards in a throw for example
        [8_of_spades, queen_of_spades, queen_of_diamonds, 8_of_diamonds, 6_diamonds, 6_clubs] is valid for
        a throw while [6_diamonds, 6_clubs, 8_of_spades, queen_of_spades, queen_of_diamonds, 8_of_diamonds]
        is invalid since question card follow a non-question one.
    -> if a player throws a punisher type card i.e 2 or 3, then the next player has to defend being punished
        by throwing the defender card i.e ace of any type or another punisher of the same first name. if he doesn't
        posses either of them, then he picks from pick_set n number of cards where n is the integer of punisher's
        first name. for example
        if punisher 3_of_clubs is thrown, then the next player can throw 3_of_diamonds or ace_of_spades or pick 3
        cards from pick_set if he can't defend himself. after this the punishment is over and the next player can throw
        another valid card since you can only punish
        the next player after you, so the next player can throw a card like 5_of_clubs or any other valid.
    -> if a player does not have a valid card to throw, then he picks a single card from the pick_set and
        the game moves to the next player.
    -> if a player throws a skipper type card i.e jack of any last name, then the next player has to accept being
        skipped or deny. If the next player doesn't have another skipper in his hands then he accepts being
        skipped and the game moves to his next player, if he has he can deny to be skipped by throwing it if
         he wishes so and the same procedure is applied on the next player. Note: you can only skip the
         next player following you to play.
    -> if a player throws a kickback type card i.e a king of any last name, then the direction of play is reversed
        to move in the opposite direction and the previous player to play now becomes the next player.
        for example if the game was moving in a clockwise direction then it will be reversed to move in
        counter clockwise direction.
    -> if a player plays his turn and the remaining cards in hands can be validly be thrown in a single move
        and they only include normal cards or combination of question and normal then he shouts 'GAME CARD'
        to alert other players that he is almost winning the match and waits for his next turn. if by chance
        his next turn his cards get accepted by the running card then he wins the match.
        Note: to win the match the player must have called game card in the previous move and throw all the
        cards in the hand in the next move and no other player should be 'CARDLESS'. No match can be won if
        any of the players is in 'CARDLESS' state i.e with no cards in hand.
        if he happens to throw a subset of the cards he has in his hand or pick from pick_set and he still be
        able to throw them all in his next turn to play the he has to call 'GAME CARD' again. if he can't
        he can choose to just remain silent or notify 'NOT GAME CARD'. if a players throws all the card
        that validly end match but didn't call the 'GAME CARD' then the match continues and the player says
        'CARDLESS' and waits to pick a card in the next turn.

     -> if a player throws all the cards in hand but the top card is not 'normal' then he says 'CARDLESS'
        and no other player can win the match when he is in this state. he then has to pick in the next turn
        and if valid call 'GAME CARD'. Otherwise if the top card is question, then he picks a card and if he
        picks a normal card then he claims 'GAME CARD' and wait for the next turn.
7. When the match is over, points are calculated and whoever will have hit maximum score set like 500, 1000
    is removed from the following matches. the last player to hit max score is the winner. PLayers try
    their best not to be caught with cards that have high score when each match ends.

=>> To use it in your local interpreter, you can uncomment the time.sleep lines to see the game in action.

    There are versions that slightly differ from this. Feel free tweak the code to fit whatever you fill like.
    Comments are welcomed. Enjoy playing........
"""

__author__ = "</Dan Rhamba>"
__copyright__ = "Copyright 2019, The Beyond Knowledge Project"
__credits__ = ["Mike Musina", "Dickson Ndukulu", "Steve Rhamba", "SoloLearn"]
__licence__ = None
__version__ = "1.0.1"
__maintainer__ = "</Dan Rhamba>"
__email__ = "dnlramba9@gmail.com"
__status__ = "Learning"

import random
from itertools import permutations

# print(__doc__)

# def dict object to store points of each card type in our game
dict_points = {"ace": 100, "2": 50, "3": 75, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "king": 10,
               "jack": 10, "queen": 10}


class Card:
    """Card object with name, first_name and last_name as properties and various methods"""

    def __init__(self, name: str):
        """name is cards name in the form first_name_of_last_name e.g ace_of_spades or 10_of_clubs"""
        self.name = name
        self.first_name = name.split('_of_')[0]
        self.last_name = name.split('_of_')[-1]

    def __str__(self):
        return f"Card({self.name})"

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    @property
    def type(self) -> str:
        """returns the type of Card object based on game rules"""
        if self.first_name in ["2", "3"]:
            return "punisher"
        elif self.first_name in ["8", 'queen']:
            return "question"
        elif self.first_name == "king":
            return "kickback"
        elif self.first_name == "jack":
            return "skipper"
        elif self.first_name == "ace":
            return "defender"
        elif self.first_name in ["4", "5", "6", "7", "9", "10"]:
            return "normal"
        else:
            raise AttributeError("Bad type....see code")

    @property
    def points(self) -> int:
        """Returns respective points as defined in dict_points"""
        return dict_points[self.first_name]

    def accepts(self, other) -> bool:
        """Returns true or false whether the passed card can validly follow our card"""
        if not isinstance(other, Card):
            raise TypeError("Passed argument is not an instance of class Card")
        if self.first_name == other.first_name or self.last_name == other.last_name:
            return True

        elif other.first_name == "ace":
            return True
        return False

    def valid_throw(self, other, last_throw) -> bool:
        """Returns true if other card can be thrown after calling card given it is
        the last throw or not"""
        if last_throw is None:
            # just check if it accepts
            return self.accepts(other)
        else:
            if self.first_name == "2" and other.first_name in ["2", "A"]:
                return True
            elif self.first_name == "3" and other.first_name in ["3", "A"]:
                return True
            else:
                return self.accepts(other)


class Table:
    """Creates Table object. see Table as playing table where cards are thrown/placed."""

    def __init__(self, table_cards: list = []):
        """table_cards is a list of cards for our table object."""
        self.table_cards = table_cards
        self.last_throw = None

    def __str__(self):
        if len(self.table_cards) < 5:
            return str([str(card) for card in self.table_cards])
        else:
            # due to screen size
            return str([str(card) for card in self.table_cards[-5:]])

    @property
    def size(self):
        """Returns the number of cards on table"""
        return len(self.table_cards)

    def add_card(self, card: Card):
        """Adds card to table's cards"""
        self.table_cards.append(card)

    @property
    def running_card(self) -> Card:
        """returns the card on top of table"""
        return self.table_cards[-1]


class Player:
    """Player object with properties and features of a common card player. Most game logic are defined here/"""

    def __init__(self, name: str, number: int, cards: list = [], running_points: int = 0, wins: int = 0,
                 matches_played: int = 0):
        """name: player's name, number: player's number, cards:[optional] player's card, running_points:[optional] 
        player's accumulated points of previous matches, wins: [optional] player's previous wins, matches_played:[
        optional] number of previous matches the player has participated."""

        self.name = name
        self.number = number
        self.hand = cards[:]
        self.current_points = sum([card.points for card in cards])
        self.running_points = running_points
        self.wins = wins
        self.matches_played = matches_played

    def __str__(self):
        details = f'''{"*"*70}\nname: {self.name}\nno.: {self.number}\ncurrent_points: {
        self.current_points}\nrunning_points: {
        self.running_points}\nwins: {
        self.wins}\nmatches_played: {self.matches_played}\ncards in hand: {[str(card) for card in self.hand]}\n{
        "*"*70}'''
        return details

    def update_points(self):
        """Updates players current points as per cards in hands"""
        self.current_points = sum([card.points for card in self.hand])

    def add_card(self, card: Card):
        """Adds card to players card"""
        if not isinstance(card, Card):
            raise ValueError("Can not add a non Card object to player's hand")
        self.hand.append(card)
        # Update points
        self.update_points()

    def pop_card(self, card_name: str) -> Card:
        """Removes card with the passed name and returns it.
         Raises ValueError if card does not exists in players
        cards."""
        card = self.hand.pop(self.hand.index(card_name))
        self.update_points()
        return card

    def remove_card(self, card: Card):
        """Removes card name inplace.
        Raises ValueError if card does not exists in players
        cards."""
        self.hand.remove(card)
        self.update_points()

    @property
    def size(self) -> int:
        """Returns the number of cards in player's hands"""
        return len(self.hand)

    @staticmethod
    def seq_points(seq: list) -> int:
        """Returns total points in seq"""
        sp = 0
        for card in seq:
            sp += dict_points[card.first_name]
        return sp

    def max(self, seqs: list, mode: str = 'points') -> list:
        """Returns the seq that has maximum points if mode is points otherwise the one that has maximum cards/items.
        mode can either be 'points' or 'items'. seqs is a list of lists"""
        mx = seqs[0]
        for seq in seqs:
            if mode == 'points':
                if self.seq_points(seq) > self.seq_points(mx):
                    mx = seq[:]
            elif mode == 'items':
                if len(seq) > len(mx):
                    mx = seq[:]
            else:
                raise ValueError('mode parameter not understood')

        return mx

    def defend_punishment(self, table: Table):
        """Defend player if previously thrown card is punisher"""
        if table.last_throw is not None:
            if table.last_throw[-1].first_name not in ['2', '3']:
                # not a punisher no need to defend so return 1
                return 1
            else:
                # get another punisher to defend
                valid = [card for card in self.hand if card.first_name == table.last_throw[-1].first_name]
                if valid:
                    # return all punishers found
                    return valid
                else:
                    # get a defender since no punishers found
                    valid = [card for card in self.hand if card.first_name == 'ace']
                    if valid:
                        # return only one... this can be changed to return all if you wish so
                        return [random.choice(valid)]  # but in a list
                # cannot defend hence return -1
                return -1
        else:
            return 0  # to show that last_throw is None

    @staticmethod
    def is_valid(seq) -> bool:
        """Returns True if the given sequence is valid, False otherwise.
        This can be used to verify if the table cards is following set rules.
        for a player's single throw validity, see Player.is_valid_seq"""
        for i in range(0, len(seq) - 1):
            if seq[i].accepts(seq[i + 1]) is False:
                return False
        return True

    @staticmethod
    def is_valid_seq(seq: list, table: Table) -> bool:
        """Unlike is_valid method, this one checks validity for players's single throw
        while the former checks for general card arrangement validity.
        If table is given then it has to be accepted by table too"""
        if table is not None:
            # if table cannot accept the first card in the sequence then return false
            if not table.running_card.accepts(seq[0]):
                return False
            # if it is a single item and table accepts it then it is valid
            elif len(seq) == 1 and table.running_card.accepts(seq[0]):
                return True
        else:
            # if seq has one card and table is none then any card is true
            if len(seq) == 1:
                return True

        # verify the rest
        c = 0
        for card in seq[1:]:
            # question card cannot come after a non-question
            if seq[c].type != 'question' and card.type == 'question':
                return False
            # card of different first names are invalid except for question cards
            elif seq[c].type != 'question' and seq[c].first_name != card.first_name:
                return False
            # if a card does not accept the next card then is invalid
            elif not seq[c].accepts(card):
                return False
            c += 1

        # has passed all checks, must be valid then
        return True

    @staticmethod
    def longest_normal_seq(seq) -> int:
        """Returns an integer showing the longest seq of normal cards in the passed sequence from far end.
        Useful in advancing player skills for deductions on best set to throw."""
        rev = reversed(seq)
        count = 0
        for card in rev:
            if card.type == 'normal':
                count += 1
            else:
                break
        return count

    @staticmethod
    def has_type(seq: list, _type) -> bool:
        """Returns True if the passed card type is present in the sequence False otherwise."""
        for card in seq:
            if card.type == _type:
                return True
        return False

    def separate_by_type(self) -> dict:
        """Separates cards in player's hand by type. and return dict object with keys as card's type name
        and values as cards of that type"""

        # separate cards in player's hand by type
        # put them in a dictionary
        dict_type = {'question': [card for card in self.hand if card.type == 'question'],
                     'punisher': [card for card in self.hand if card.type == 'punisher'],
                     'skipper': [card for card in self.hand if card.type == 'skipper'],
                     'kickback': [card for card in self.hand if card.type == 'kickback'],
                     'defender': [card for card in self.hand if card.type == 'defender']}

        # arrange the normal cards by their first_names
        normal = [card for card in self.hand if card.type == 'normal']
        normal_first_name = set([card.first_name for card in normal])

        # separate the normal by their first names too
        for fs in normal_first_name:
            dict_type[fs] = [card for card in self.hand if card.first_name == fs]

        return dict_type

    @staticmethod
    def permute_by_type(dict_of_types: dict) -> dict:
        """Permutes all possible permutations of each type and returns them as a copy
        of the passed dict only with values replaced by permuted values."""

        # reduce unnecessary permutations, permute each set separately
        # reduced time from 32 sec to 0.21 sec
        permuted_dict = {key: [] for key in dict_of_types}
        for key, value in dict_of_types.items():
            n = len(value)
            # go deeper to get all permutations possible
            while n:
                permuted_dict[key] += list(permutations(value, n))
                n -= 1
        return permuted_dict

    @staticmethod
    def flatten(permuted_dict: dict) -> list:
        """Flattens results of different permutations into single list"""

        flattened = []
        for key, value in permuted_dict.items():
            # we don't need to flatten the question types. dealt with later in chaining to others
            if key == 'question':
                continue
            for seq in value:
                flattened.append(seq)
        return flattened

    def chain_que_to_others(self, permuted_dict: dict, flattened, table: Table) -> list:
        """chains each set of question to flattened values and return those that are valid
        with respect to table.running_card"""
        chained = []
        for que in permuted_dict['question']:
            for ft in flattened:
                ch = list(que) + list(ft)
                # append those that are valid only
                if self.is_valid_seq(ch, table):
                    chained.append(ch)
        return chained

    def valid_set(self, table) -> list:
        """Permutes cards in player's hand and drops the invalid sequences and returns them in a list of lists. If
        table is None then they don't have to be accepted by table's running card."""

        # permute and extract all valid sequence that exist in players cards
        # due to the cost of permutation, we apply some cool tricks. see separate_by_type method

        dict_type = self.separate_by_type()
        permuted_dict = self.permute_by_type(dict_type)

        # flatten the non question
        flattened = self.flatten(permuted_dict)

        # chain question cards to non-question ones to get extra valid sets
        # then combine the compatible ones and add assign tem to valid found so far
        valid = self.chain_que_to_others(permuted_dict, flattened, table)

        # add valid seqs from flattened
        for ft in flattened:
            if self.is_valid_seq(ft, table) or self.has_type(ft, 'defender'):
                valid.append(list(ft))

        # drop invalid question seq and append valid ones to valid
        for que in permuted_dict['question']:
            if self.is_valid_seq(list(que), table):
                valid.append(que)
        return valid

    def get_by_type(self, valid: list, _type: str, mode: str = "points"):
        """returns card that has the given type by first returning questioned before pure
        based on mode which can be either be 'points' or 'items'.
        Note: there is no standard here, you can use your own way to make decisions on best sequence
        to pick."""

        if not valid:
            return None

        chosen = [seq for seq in valid if self.has_type(seq, 'question') and self.has_type(seq, _type)]
        if chosen:
            return self.max(chosen, mode=mode)

        chosen = [seq for seq in valid if self.has_type(seq, _type)]
        if chosen:
            return self.max(chosen, mode=mode)

    def best_chosen_sequence(self, table: Table, mode='points'):
        """takes a list of valid sequences and chooses the best based on parameter mode.
        mode can be 'points' for maximum points or 'items' for maximum items in the sequence."""
        valid = self.valid_set(table)

        # return none if we have no valid throw
        if not valid:
            return None

        # arranged by 'my priorities'
        types = ['punisher', 'skipper', 'kickback', 'defender', 'normal', 'question']
        best_choice = self.get_by_type(valid, types[0])
        c = 1

        # loop till we hit a better choice
        while not best_choice:
            # check by priority
            best_choice = self.get_by_type(valid, types[c], mode=mode)
            c += 1
        return best_choice

    def is_card(self) -> bool:
        """Returns true if player can call card false otherwise. see description "for calling card in doc."""
        # checking for card is irrespective of table card since you don't know in adavance which card
        # will be on top when the next turn comes.
        valid = self.valid_set(table=None)
        # these types can not win a match
        if self.has_type(self.hand, 'skipper') or self.has_type(self.hand, 'kickback') or self.has_type(self.hand,
                                                                                                        'defender') or self.has_type(
            self.hand, 'punisher'):
            return False

        # a seq without normal cards can not win a match
        if not self.has_type(self.hand, 'normal'):
            return False
        for vd in valid:
            # if there exists at least one permutation/seq that can be thrown in a single throw leaving the hand empty then it is valid
            if len(set(self.hand) - set(vd)) == 0:
                return True
        return False

    def has_valid(self, table: Table) -> bool:
        """Returns true if player has at least one valid card relative to table's running_card false otherwise."""
        for card in self.hand:
            if table.running_card.accepts(card):
                return True
        return False


class GamePlay:
    """Performs the logic of the game and checks on game rules."""
    def __init__(self, player_details: dict, max_score=100):
        """player_details is a dict with keys as player names and values as their respective numbers.
        Optional max_score is the minimum score needed to remove a player in a match."""
        self.player_details = player_details
        self.players = [Player(name, number) for name, number in player_details.items()]
        self.card_set = self.create_card_names()

        # put all cards in the pick_set before any distribution is done
        self.pick_set = [Card(card_name) for card_name in self.card_set]

        # create a table for the game
        self.table = Table()
        self.running_number = 1
        self.direction = 1  # can be either 1 or -1
        self.card_callers = []  # will append names of card callers here
        self.match_no = 1  # number of matches played
        self.game_round = 1  # number of refilling pick_set
        self.displaced = set()  # stores palyers removed from matches
        self.max_score = max_score

    @staticmethod
    def create_card_names():
        """Return the complete 52 card set names excluding jokers."""
        first_names = list(dict_points.keys())
        last_names = ['clubs', 'spades', 'diamonds', 'hearts']
        cards = [f'{fs}_of_{ls}' for fs in first_names for ls in last_names]
        random.shuffle(cards)
        return cards

    @property
    def card_calls(self) -> int:
        """return the number of players calling card"""
        return len(self.card_callers)

    def distribute_cards(self, n: int = 4):
        """Distributes n cards to each player and initializes the table card"""

        # if the game is running get all the cards from table and players and append them in pick_set for
        # fresh distribution
        print(f'Distributing card for match {self.match_no}\n')
        for player in self.players:
            self.pick_set += player.hand
            player.hand = []
        self.pick_set += self.table.table_cards
        self.table.table_cards = []

        # perform some shuffling
        random.shuffle(self.pick_set)

        for player in self.players:
            while player.size < n:
                player.add_card(self.pick_set.pop())

        # assign the starting card to table
        self.table.add_card(self.pick_set.pop())

        # assign the card on table as last throw
        self.table.last_throw = [self.table.running_card]

    def display_player(self):
        """Prints each player's info"""
        for player in self.players:
            print(player)

    def get_player(self, number: int) -> Player:
        """Returns Player object with the passed number."""
        for player in self.players:
            if player.number == number:
                return player
        raise ValueError('No player with the given number on the table')

    @property
    def size(self) -> int:
        """Returns the number of players in the game."""
        return len(self.players)

    def update_pick_set(self):
        """Ensures pick_set does not get empty by refilling it from table and shuffling it.
        Note: every refill increments the game_round by 1"""

        # we don't want pick_set to have less tahn 5 cards
        if len(self.pick_set) > 5:
            # update when necessary
            return
        sample = self.table.table_cards[:-1]
        self.pick_set += sample
        random.shuffle(self.pick_set)
        self.table.table_cards = [self.table.running_card]

        # increase game_round
        self.game_round += 1

    def next_number(self) -> int:
        """computes the next number/player to play based on general game playing rules."""

        if self.table.last_throw is None:
            n = 1
        elif self.table.last_throw[-1].type == 'skipper':
            next_player = self.get_player(self.running_number)
            if next_player.has_type(next_player.hand, 'skipper'):
                print('jump denied')
                n = 1
            else:
                n = 2
                print('jump accepted\n')
        elif self.table.last_throw[-1].type == 'kickback':
            n = 1
            self.direction = -1 if self.direction == 1 else 1
        else:
            n = 1

        if self.direction == 1:
            nx = (self.running_number + n) % self.size
            nx = self.size if nx == 0 else nx
            return nx
        elif self.direction == -1:
            nx = (self.running_number - n) % self.size
            nx = self.size if nx == 0 else nx
            return nx
        else:
            raise ValueError('Unknown direction value')

    def throw(self, player: Player, valid: list, text):
        """Perform player's throw operations"""
        print(f'Current Player: {player.name}\nCurrent No: {player.number}\n')
        self.table.last_throw = valid[:]
        for card in valid:
            print(text + f'{card.name}')
            player.remove_card(card)  # time.sleep(3)

    def quick_info(self, player: Player):
        """displays short player's info"""
        print('-' * 70)
        print(player)
        print(f'\n{player.name} cards before playing')
        print([card.name for card in player.hand])
        print(f'\nRunning card: {self.table.running_card.name}\n')
        print(f'Card callers: {self.card_callers}')

    def process_and_play(self, player: Player):
        """Makes reasonable deductions and comes up with decisions to play"""
        valid = player.defend_punishment(self.table)

        if type(valid) == list:
            self.throw(player, valid, f'Defending.....\nPlayer throwing \n')
            self.table.last_throw = valid[:]

        elif valid == -1:
            # player cannot defend so picks int(punisher.first_name) cards
            count = int(self.table.last_throw[-1].first_name)
            for i in range(count):
                player.add_card(self.pick_set.pop())
                print(f'{player.name} picking card {i+1}\n')
            # assign None to table.last_throw
            self.table.last_throw = None

        elif valid in [0, 1]:
            valid = player.best_chosen_sequence(self.table)
            if valid:
                self.throw(player, valid, f'{player.name} throwing \n\n')
                self.table.last_throw = valid[:]
            else:
                print(f'{player.name} picking card')
                self.table.last_throw = None
                player.add_card(self.pick_set.pop())
        else:
            raise ValueError('Developers attention needed')

        if self.table.last_throw is not None:
            self.table.table_cards += self.table.last_throw
            if self.table.last_throw[-1].type == 'question':
                print(f'filling the question\nplaying again')
                # time.sleep(3)
                self.play()
        return None

    def game_status_check(self, player: Player):
        """Performs necessary game checks, adjustments and updates based on each player's move"""
        if player.size == 0 and player.name in self.card_callers:
            print(f'{player.name} wins the match\n')
            player.wins += 1
            print('calculating players points.......')
            # time.sleep(5)
            for pl in self.players:
                pl.running_points += pl.current_points
            # print(self.text)
            self.display_player()

            # ans = input('Enter y to continue with game or n to exit game -> ').lower()
            # time.sleep(2)
            ans = 'y'
            if ans == 'y':
                # start game new match
                self.match_no += 1
                player.matches_played += 1
                print(f'match {self.match_no} starting\n')
                self.distribute_cards()
                self.display_player()

                # the last player to reach max_points wins
                min_points = [pl.running_points for pl in self.players if pl.running_points < self.max_score]
                if len(min_points) <= 1:
                    exit(0)
                self.play()
            elif ans == 'n':
                print('thank you for playing\n game end...')
                exit(0)
            else:
                print('unknown answer..game exits')
                exit(2)

        elif player.size == 0 and player.name not in self.card_callers:
            print(f'{player.name} goes card less\n')
        if player.is_card():
            print(f'{player.name} is calling GAME CARD!!!\n')
            self.card_callers.append(player.name)
            self.card_callers = list(set(self.card_callers))
        else:
            if player.name in self.card_callers:
                self.card_callers.remove(player.name)
        print(f'\n{player.name} cards after playing')
        print([card.name for card in player.hand])
        self.running_number = self.next_number()
        player.update_points()
        return None

    def play(self):
        # update pick_set if necessary
        self.update_pick_set()
        player = self.get_player(self.running_number)

        # display some player's info
        self.quick_info(player)

        # do some thinking and decision making
        self.process_and_play(player)

        # do some checks, adjustments and updates
        self.game_status_check(player)

        print('-' * 70)
        # time.sleep(5)
        return None


def main():
    # define players' details 
    player_details = {'Dan': 1, 'Mike': 2, 'Steve': 3, 'Dickson': 4}
    game_play = GamePlay(player_details)
    # initialize game by distributing card as per game rules
    game_play.distribute_cards()
    while True:
        game_play.play()


if __name__ == '__main__':
    main()

