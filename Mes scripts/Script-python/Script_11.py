ch="  salut tout le monde  "
print(len(ch))
ch1=ch.strip()
print(ch1)
print(len(ch1))
ch2=ch.lstrip()
print(ch2)
print(len(ch2))
ch3=ch.rstrip()
print(ch3)
print(len(ch3))
ch4="***salut***tout***le***monde***"
ch5=ch.strip("*")
print(ch5)
print(len(ch5))

ch6="***salut***tout***le***monde***"
ch7=ch.lstrip("*")
print(ch7)
print(len(ch7))
print(ch4.replace("*"," "))
print(ch4.replace(" "," "))

ch8="  SALUT  TOUT le monde  "
print(ch8.lower())
print(ch8.upper())
ch9="salut tout le monde le monde le monde "
print(ch9.count("monde"))
print(ch9.startswith("salut"))
print(ch9.endswith("monde"))
ch10="un-deux-trois-quatre-cinq-six "
print(ch10.split("-"))