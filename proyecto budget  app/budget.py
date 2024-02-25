class Category:

  def __init__(self, category):
    self.ledger = []
    self.category = category

  def __str__(self):
    budget = self.category.center(30, '*') + '\n'
    total = f'Total: {self.get_balance()}'
    for dict in self.ledger:
      amount = dict["amount"]
      description = dict["description"]
      budget += "{:<23}{:>7.2f}\n".format(description[:23], amount)
    budget += total
    return str(budget)

  def deposit(self, amount, description=''):
    new_deposit = {"amount": amount, "description": description}
    self.ledger.append(new_deposit)

  def check_funds(self, amount):
    return amount <= self.get_balance()

  def withdraw(self, amount, description=''):
    if self.check_funds(amount):
      new_withdraw = {"amount": -amount, "description": description}
      self.ledger.append(new_withdraw)
      return True
    else:
      return False

  def get_balance(self):
    return sum(dict["amount"] for dict in self.ledger)

  def transfer(self, amount, ad_category):
    if self.check_funds(amount):
      new_deposit = {
          "amount": amount,
          "description": f'Transfer from {self.category}'
      }
      new_withdraw = {
          "amount": -amount,
          "description": f'Transfer to {ad_category.category}'
      }
      self.ledger.append(new_withdraw)
      ad_category.ledger.append(new_deposit)
      return True
    else:
      return False


def create_spend_chart(categories):
  percentage = list(range(100, -10, -10))
  o_amount = []
  categories_num = []
  spent = []
  c_amount = []
  # recorro para sacar los porcentajes
  for category in categories:
    spent.append(
        abs(
            sum(dict["amount"] for dict in category.ledger
                if dict["amount"] < 0)))
    categories_num.append(len(category.category))

  #defino el total gastado y la categoria de nombre mas largo
  max_category = max(categories_num)
  total = sum(spent)

  # hago los f strings para el nombre
  for category in categories:
    string_c = f'{category.category}{" "* (max_category-len(category.category))}'
    c_amount.append(string_c)

  #defino los primeros elementos
  chart = 'Percentage spent by category\n'
  lines = f'    {"-" * (len(categories) * 3 + 1)}\n'
  names_categories = ''

  #string de porcentaje con "o"
  for p in range(len(percentage)):
    chart += f'{str(percentage[p]).rjust(3, " ")}| '

    for position in range(len(categories)):
      percent = int((spent[position] * 10) / total) + 1
      o_amount.append(f'{" "*(len(percentage)-percent)}{"o"*percent}')

      chart += f'{o_amount[position][p]}  '
    chart += "\n"
  chart += lines

  for i in range(max_category):
    names_categories += "     "
    for category in range(len(categories)):
      names_categories += f'{c_amount[category][i]}  '
    names_categories += "\n"
  chart += names_categories[:-1]

  return chart
