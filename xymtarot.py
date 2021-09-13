import discord
from discord.ext import commands
import os
import random
from stayup import stayup

botto = commands.Bot(command_prefix = '*')

dice = [1,2,3,4,5,6]

minArcana = ['Wands', 'Pentacles', 'Cups', 'Swords']

majArcana = ['The Fool', 'The Magician', 'The High Priestess', 'The Empress', 'The Emperor', 'The Hierophant', 'The Lovers', 'The Chariot', 'Strength', 'The Hermit', 'Wheel of Fortune', 'Justice', 'The Hanged Man', 'Death', 'Temperance', 'The Devil', 'The Tower', 'The Star', 'The Moon', 'The Sun', 'Judgement', 'THE WORLD']

class TarotCard:
  def __init__(self, arcana, num):
    self.arcana = arcana
    self.num = num

class Deck:
  def __init__(self):
    self.newDeck = []
    self.generateDeck()

  def generateDeck(self):
    minorA = [TarotCard(minArcana, num) for minArcana in minArcana for num in range(1,15)]
    majorA = [TarotCard(majArcana, num) for num, majArcana in enumerate(majArcana)]
    generated = minorA + majorA
    for x in generated:
      self.newDeck.append(x)

  def shufflecards(self):
    random.shuffle(self.newDeck)

  def reveal(self):
    for c in self.newDeck:
      c.flipCard()

  def drawTarot(self):
    return self.newDeck.pop()
  
class Player:
  def __init__(self):
    self.hand = []
    self.strhand = []
  
  def playerDraw(self, deck):
    self.hand.append(deck.drawTarot())
    return self
  
  def showUserHand(self):
    for card in self.hand:
      card.orientation = random.choice(['Upright', 'Reversed'])
      faceupcard = card.orientation + ', ' + str(card.arcana) + ' of ' + str(card.num)
      self.strhand += [faceupcard]
    return '\n'.join(self.strhand)

  def playerHand(self, deck):
    self.hand.append(deck.drawTarot())
    self.hand.append(deck.drawTarot())
    self.hand.append(deck.drawTarot())
    return self

@botto.event
async def on_ready():
  print('Logged in as {0.user}'.format(botto))

@botto.command()
async def draw(ctx):
  user = Player()
  deck = Deck()
  deck.shufflecards()
  user.playerHand(deck)
  playerhand = user.showUserHand()
  await ctx.send(f'Welcome to Xym Tarot Reading. The 3 cards drawn represents your: past, present, and future. This is your tarot reading for today:\n{playerhand}\nMay you have great fortune, {ctx.author.name}. Thank you.')

  
@botto.command()
async def test(ctx):
  await ctx.channel.send('testing')

stayup()
botto.run(os.getenv('TOKEN'))


