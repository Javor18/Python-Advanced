from collections import deque

bomb_effects = deque(int(x) for x in input().split(", "))
bomb_casings = deque(int(x) for x in input().split(", "))

datura_bombs_count = 0
cherry_bombs_count = 0
smoke_bombs_count = 0

filled_pouch = False

while bomb_effects and bomb_casings:

    bomb_effect = bomb_effects.popleft()
    bomb_casing = bomb_casings.pop()

    result = bomb_effect + bomb_casing

    if result == 40:

        datura_bombs_count += 1

    elif result == 60:

        cherry_bombs_count += 1

    elif result == 120:

        smoke_bombs_count += 1

    else:

        bomb_effects.appendleft(bomb_effect)
        bomb_casing -= 5
        bomb_casings.append(bomb_casing)

    if datura_bombs_count >= 3 and cherry_bombs_count >= 3 and smoke_bombs_count >= 3:

        filled_pouch = True

        break

if filled_pouch == True:

      print("Bene! You have successfully filled the bomb pouch!")

else:

    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")

else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")

else:
    print("Bomb Casings: empty")

print(f"Cherry Bombs: {cherry_bombs_count}")
print(f"Datura Bombs: {datura_bombs_count}")
print(f"Smoke Decoy Bombs: {smoke_bombs_count}")
