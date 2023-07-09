import random

game_display = input("¿Querés jugar? Y/N ")
game_display = game_display.lower()
options = ["piedra", "papel", "tijera"]
rounds = 1
user_wins = 0
pc_wins = 0

while game_display == "y":

   print("*"*10)
   print(f"Ronda: {rounds}")
   print("*"*10)
   
   user_option = input("¿Piedra, papel o tijera? ")
   user_option = user_option.lower()
  
   if not user_option in options:
     print("No existe esa opción")
    
   for i in range(1):
    pc_option = random.choice(options)
  
   if user_option == pc_option:
    print(f"Vos => {user_option} vs PC => {pc_option} = Empataron")
  
   elif user_option == "piedra":
  
    if pc_option == "papel":
      print(f"Vos => {user_option} vs PC => {pc_option} = Perdiste, papel gana a piedra")
      pc_wins += 1  
    else:
      print(f"Vos => {user_option} vs PC => {pc_option} = Ganaste, piedra gana a tijera")
      user_wins += 1  
   elif user_option == "papel":
    if pc_option == "piedra":
      print(f"Vos => {user_option} vs PC => {pc_option} = Ganaste, papel gana a piedra")
      user_wins +=1
    else:
      print(f"Vos => {user_option} vs PC => {pc_option} = Pediste, tijera gana a papel")
      pc_wins += 1
      
   elif user_option == "tijera":
    if pc_option == "piedra":
      print(f"Vos => {user_option} vs PC => {pc_option} = Perdiste, piedra gana a tijera")
      pc_wins += 1
    else: 
      print(f"Vos => {user_option} vs PC => {pc_option} = Ganaste, tijera gana a papel")
      user_wins += 1
  
   print(f"Vos:{user_wins}")
   print(f"PC:{pc_wins}")
   game_display = input("¿Querés jugar? Y/N")
   game_display = game_display.lower()
   rounds += 1

     
print("Gracias por participar")