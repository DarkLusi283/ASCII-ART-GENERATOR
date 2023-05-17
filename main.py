import pyfiglet

print('    ___   _____ ______________   ___    ____  ______')
print('   /   | / ___// ____/  _/  _/  /   |  / __ \/_  __/') 
print('  / /| | \__ \/ /    / / / /   / /| | / /_/ / / /   ')
print(' / ___ |___/ / /____/ /_/ /   / ___ |/ _, _/ / /    ')
print('/_/  |_/____/\____/___/___/  /_/  |_/_/ |_| /_/     ')
print(' ')
print(' ')
print('   _____________   ____________  ___  __________  ____ ')
print('  / ____/ ____/ | / / ____/ __ \/   |/_  __/ __ \/ __ \')
print(' / / __/ __/ /  |/ / __/ / /_/ / /| | / / / / / / /_/ /')
print('/ /_/ / /___/ /|  / /___/ _, _/ ___ |/ / / /_/ / _, _/ ')
print('\____/_____/_/ |_/_____/_/ |_/_/  |_/_/  \____/_/ |_|  ')
print('\n')
print('                                         >> V1.0           ')  
print('                                             >> By DarkLusifer            ')  
text = input("Enter your text: ")


print("Select a style that you want:")
print(" 1. Standard")
print(" 2. Slant")
print(" 3. 3D")
print(" 4. Banner")
print(" 5. Bubble")
print(" 6. Big")
print(" 7. Block")
print(" 8. Digital")
print(" 9. Mini")
print("10. SMShadow")
print("11. SMSlant")
print("12. SMScript")
print("13. Small"
print("14. Shadow")
print("15. Script")
print("16. Ivrit"
print("17. Lean"
style = int(input("Enter the number to select: "))


if style == 1:
    ascii_art = pyfiglet.figlet_format(text)
elif style == 2:
    ascii_art = pyfiglet.figlet_format(text, font="slant")
elif style == 3:
    ascii_art = pyfiglet.figlet_format(text, font="3-d")
elif style == 4:
    ascii_art = pyfiglet.figlet_format(text, font="banner")
elif style == 5:
    ascii_art = pyfiglet.figlet_format(text, font="bubble")
elif style == 6:
    ascii_art = pyfiglet.figlet_format(text, font="big")
elif style == 7:
    ascii_art = pyfiglet.figlet_format(text, font="block")
elif style == 8:
    ascii_art = pyfiglet.figlet_format(text, font="digital")
elif style == 9:
    ascii_art = pyfiglet.figlet_format(text, font="mini")
elif style == 10:
    ascii_art = pyfiglet.figlet_format(text, font="smshadow")
elif style == 11:
    ascii_art = pyfiglet.figlet_format(text, font="ivrit")
elif style == 12:
    ascii_art = pyfiglet.figlet_format(text, font="smscript")
elif style == 13:
    ascii_art = pyfiglet.figlet_format(text, font="small")
elif style == 14:
    ascii_art = pyfiglet.figlet_format(text, font="shadow")
elif style == 15:
    ascii_art = pyfiglet.figlet_format(text, font="script")
elif style == 16:
    ascii_art = pyfiglet.figlet_format(text, font="ivrit")
elif style == 17:
    ascii_art = pyfiglet.figlet_format(text, font="lean")
      
      
print(ascii_art)
