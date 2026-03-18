def bin_to_dec(binary:str) -> int:
  number:int = 0
  for digit in binary:
    number *= 2
    number += int(digit)
  return number


def dec_to_bin(decimal:int, bits:int=4) -> str:
  number:int = decimal
  binary:str = ""
  while number > 0:
    remainder:int = number % 2
    number = number // 2
    binary = str(remainder) + binary
  return str((bits - len(binary)) * "0") + binary

