import random
player_life = 500
player_mana = 100
enemy_life = 50
enemies = []
enemy = []
game = True
print("\n\n---------> Seja bem vindo ao jogo das pancadas!! <---------\n\n")
num = int(input("Digite a quantidade de inimigos: "))
name = input("Digite o seu nome: ")
for x in range(1,num+1):
    enemy = [x,enemy_life]
    enemies.append(enemy)
while game == True:
    print("\n%s sua vida atual é %d."%(name,player_life))
    print("Sua mana atual é %d."%player_mana)
    escolha = int(input("Você deseja atacar (1) ou curar (2): "))
    if escolha == 1:
        atk = random.choice(enemies)
        bufetada = random.randint(10,15)
        atk[1]-=bufetada
        print("Você atacou o inimigo %d com %d de ataque."%(atk[0],bufetada))
        if atk[1]<=0:
            print("\nO inimigo %d morreu!\n"%atk[0])
            enemies.remove(atk)
    if escolha == 2:
        if player_mana >=10:
            cura = random.randint(10,15)
            player_life+=cura
            player_mana-=10
            if player_life > 500:
                player_life = 500
            print("Você se curou %d e sua vida é %d"%(cura,player_life))
        else:
            print("Você não tem mana suficiente")
    for y in enemies:
        acertou = bool(random.choice([1,0,1,1]))
        porradaenemy = random.randint(1,3)
        if acertou:
            player_life-=porradaenemy
            print("O inimigo %i acertou com %i de dano."%(y[0],porradaenemy))
        else:
            print("O inimigo %i errou."%y[0])
    if player_life <=0:
        print("\n\n=====  %s você morreu, GG!  =====\n\n"%name)
        break
    if len(enemies) == 0:
        print("\n\n--------->   %s   <---------"%name)
        print("------>  PARABÉNS!  <------\nVocê matou todos e ganhou o jogo!\n\n")
        break
    player_mana+=3
    if player_mana>100:
        player_mana=100
