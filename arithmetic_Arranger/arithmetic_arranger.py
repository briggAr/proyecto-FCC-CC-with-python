def arithmetic_arranger(problems, display=False):
  answer = []
  string, string2, string3 = [], [], []

  if len(problems) > 5:
    return "Error: Too many problems."
  for problem in problems:
    num1, op, num2 = problem.split()
    if op not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."
    if not (num1 + num2).isdigit():
      return "Error: Numbers must only contain digits."
    if len(num1) > 4 or len(num2) > 4:
      return "Error: Numbers cannot be more than four digits."

    #obtengo la solución
    # obtengo lo mismo si uso como valor int(num1) +/ int(num2) para cada llave
    operators = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
    answer_1 = str(operators[op](int(num1), int(num2)))

    #Numero de lineas divisorias. Numero mas largo + 2 (vacio y el operador)
    num_ = max(len(num1), len(num2)) + 2
    #Espacios vacios para el operando mas pequeño
    empty_space = abs(len(num1) - len(num2))

    #evaluando a que numero aplicar los espacios vacios
    if len(num1) < len(num2):
      num1 = ' ' * (empty_space) + num1
    else:
      num2 = ' ' * empty_space + num2

    #añado la cadena aplicada con espacios y lineas
    string.append(f'  {num1}')
    string2.append(f'{op} {num2}')
    string3.append(f'{"-"*num_}')
    answer.append(f'{" "*(abs(len(answer_1)-num_))}{answer_1}')
  #hago esa lista de cadenas un solo string
  string = '    '.join(string)
  string2 = '    '.join(string2)
  string3 = '    '.join(string3)
  answer = '    '.join(answer)

  #evaluando si se necesita retornar la solucion
  if display:
    arranged_problems = string + '\n' + string2 + '\n' + string3 + '\n' + answer
  else:
    arranged_problems = string + '\n' + string2 + '\n' + string3

  return arranged_problems
