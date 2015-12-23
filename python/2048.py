#!/usr/bin/python

import random

class Game():

  def __init__(self):
    self.board = [[ 0 for x in xrange(4) ] for y in xrange(4)]
    pass

  def draw(self):
    for row in self.board:
      for x in row:
        print "%3d" % x,
      print

  def right(self):
    for y in xrange(4):
      for p in range(4)[::-1]:
        for q in range(0, p)[::-1]:
          if self.board[y][p] == 0 and self.board[y][q] == 0:
            continue
          if self.board[y][p] > 0 and self.board[y][q] == 0:
            continue
          elif self.board[y][p] == 0 and self.board[y][q] > 0:
            self.board[y][p], self.board[y][q] = self.board[y][q], self.board[y][p]
            break
          elif self.board[y][p] == self.board[y][q]:
            self.board[y][p], self.board[y][q] = self.board[y][p] + self.board[y][q], 0
            break

  def left(self):
    for y in xrange(4):
      for p in range(4):
        for q in range(p+1, 4):
          if self.board[y][p] == 0 and self.board[y][q] == 0:
            continue
          if self.board[y][p] > 0 and self.board[y][q] == 0:
            continue
          elif self.board[y][p] == 0 and self.board[y][q] > 0:
            self.board[y][p], self.board[y][q] = self.board[y][q], self.board[y][p]
            break
          elif self.board[y][p] == self.board[y][q]:
            self.board[y][p], self.board[y][q] = self.board[y][p] + self.board[y][q], 0
            break

  def down(self):
    for x in xrange(4):
      for p in range(4)[::-1]:
        for q in range(0, p)[::-1]:
          if self.board[p][x] == 0 and self.board[q][x] == 0:
            continue
          if self.board[p][x] > 0 and self.board[q][x] == 0:
            continue
          elif self.board[p][x] == 0 and self.board[q][x] > 0:
            self.board[p][x], self.board[q][x] = self.board[q][x], self.board[p][x]
            break
          elif self.board[p][x] == self.board[q][x]:
            self.board[p][x], self.board[q][x] = self.board[p][x] + self.board[q][x], 0
            break

  def up(self):
    for x in xrange(4):
      for p in range(4):
        for q in range(p+1, 4):
          if self.board[p][x] == 0 and self.board[q][x] == 0:
            continue
          if self.board[p][x] > 0 and self.board[q][x] == 0:
            continue
          elif self.board[p][x] == 0 and self.board[q][x] > 0:
            self.board[p][x], self.board[q][x] = self.board[q][x], self.board[p][x]
            break
          elif self.board[p][x] == self.board[q][x]:
            self.board[p][x], self.board[q][x] = self.board[p][x] + self.board[q][x], 0
            break

  def generate(self):
    blank = []
    for y in xrange(4):
      for x in xrange(4):
        if self.board[y][x] == 0:
          blank.append((x, y))
    if len(blank) > 0:
      x, y = random.choice(blank)
      self.board[y][x] = 2
    pass

if __name__ == '__main__':
  print 'main()'
  game = Game()

  while True:
    game.draw()
    d = raw_input()
    if d == 'j':
      game.left()
    elif d == 'k':
      game.down()
    elif d == 'l':
      game.right()
    elif d == 'i':
      game.up()
    game.generate()
