PyQt-скрипт с игрой про волка, козу и капусту. Чтобы перемещаться через реку, кликайте левой кнопкой мыши по изображениям волка, козы и капусты.

Запуск из папки WolfGoatCabbageProblem:

$ python main.py

Ниже немного псевдокода, описывающего алгоритм работы скрипта (на сигналах и слотах).

_________________________

mouse press on the creature

send.signalToFarmer() --->

_________________________

---> catch.signalToFarmer
{
  if (farmer.state == 0)
  then { send.farmerStateIs0() -> }
  else { send.farmerStateIs1() -> }

  farmer.changeState()
}

_________________________

-> catch.farmerStateIs0()
{
  if (creature.state == 0)
  then { creature.changeState() }
}

checkWin()

_________________________

-> catch.farmerStateIs1()
{
  if (creature.state == 1)
  then { creature.changeState() }
}

checkWin()

__________________________
