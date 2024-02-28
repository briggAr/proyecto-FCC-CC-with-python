def add_time(start, duration, day=''):
  week = [
      "monday", "tuesday", "wednesday", "thursday", "friday", "saturday",
      "sunday"
  ]
  hour, schedule = start.split()
  hour, minutes = hour.split(":")
  plus_hours, plus_minutes = duration.split(":")

  #paso a horario militar
  if schedule == "PM":
    hour = int(hour) + 12
    if hour == 24:
      hour = 0
      schedule = "AM"
  #hallo las horas finales en horario militar
  sum_hours = int(hour) + int(plus_hours)

  #hallo los minutos finales:
  final_minutes = int(minutes) + int(plus_minutes)
  if final_minutes >= 60:
    sum_hours += final_minutes // 60
    final_minutes = final_minutes % 60

  if final_minutes < 10:
    final_minutes = '0' + str(final_minutes)

  #cambio de horario
  days = sum_hours // 24
  final_hour = sum_hours % 24

  if final_hour > 12:
    final_hour = sum_hours - 12
    schedule = 'PM'
  elif final_hour == 12:
    schedule = 'PM'
  else:
    schedule = 'AM'

  if final_hour == 0:
    final_hour = 12

  #anuncio adicional#
  day_announcement = ''
  if days == 1:
    day_announcement = ' (next day)'
  elif days > 1:
    day_announcement = ' (' + str(days) + ' days later)'

  if day != '':
    day = day.lower()
    ind = week.index(day)
    day = (days + ind) % 7
    day = ", " + (week[day]).capitalize()

  #respuesta final
  answer = f'{final_hour}:{final_minutes} {schedule}{day}{day_announcement}'
  return answer
