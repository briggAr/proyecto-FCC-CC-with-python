import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **param):
    self.balls = []
    for ball in param:
      extend_list = [ball] * param[ball]
      self.balls.extend(extend_list)
    self.contents = self.balls

  def draw(self, amount):
    result = []
    self.contents = self.balls.copy()
    for _ in range(amount):
      random_choice = random.choice(self.contents)
      result.append(self.contents.pop(self.contents.index(random_choice)))

      if self.contents == []:
        self.contents = self.balls.copy()

    return result


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  counter = 0
  for _ in range(num_experiments):
    result = []
    result = hat.draw(num_balls_drawn)

    found = 0
    for ball in expected_balls:
      num_ball = result.count(ball)
      if num_ball >= expected_balls[ball]:
        found += 1
    if found == len(expected_balls):
      counter += 1

  return counter / num_experiments
