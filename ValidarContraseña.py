import re

password = "12Holaa@"
validador = re.search("(?=.*[A-Z]{1,2})(?=.*[a-z]{4,20})(?=.*[0-9]{2,10})(?=.*[@#$%&/?¿<>^-])",password)
print(validador)