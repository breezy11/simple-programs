import pygame as pg
import os

pg.init()

# Creates a windows for game
win = pg.display.set_mode((550, 550))

# Loads images
x = pg.image.load(os.path.join('res', 'x.jpg'))
o = pg.image.load(os.path.join('res', 'o.jpg'))

# Sets the title of window
pg.display.set_caption("Tic Tac Toe")

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

first = pg.draw.rect(win, (255, 255, 255), (0, 0, 180, 180))
second = pg.draw.rect(win, (255, 255, 255), (185, 0, 180, 180))
third = pg.draw.rect(win, (255, 255, 255), (370, 0, 180, 180))
fourth = pg.draw.rect(win, (255, 255, 255), (0, 185, 180, 180))
fifth = pg.draw.rect(win, (255, 255, 255), (185, 185, 180, 180))
sixth = pg.draw.rect(win, (255, 255, 255), (370, 185, 180, 180))
seventh = pg.draw.rect(win, (255, 255, 255), (0, 370, 180, 180))
eighth = pg.draw.rect(win, (255, 255, 255), (185, 370, 180, 180))
ninth = pg.draw.rect(win, (255, 255, 255), (370, 370, 180, 180))

run = True
won = False
draw_object = 'x'

first_open = True
second_open = True
third_open = True
fourth_open = True
fifth_open = True
sixth_open = True
seventh_open = True
eighth_open = True
ninth_open = True

def full_check():
    for row in board:
        for column in row:
            if column == 0:
                return False
    return True

def win_check(num):
    for row in board:
        for tile in row:
            if tile == num:
                continue
            else:
                break
        else:
            return True

    for column in range(3):
        for row in board:
            if row[column] == num:
                continue
            else:
                break
        else:
            return True

    for tile in range(3):
        if board[tile][tile] == num:
            continue
        else:
            break
    else:
        return True

    for tile in range(3):
        if board[tile][2 - tile] == num:
            continue
        else:
            break
    else:
        return True


while run:

    pg.time.delay(100)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                win.fill((0, 0, 0))
                first = pg.draw.rect(win, (255, 255, 255), (0, 0, 180, 180))
                second = pg.draw.rect(win, (255, 255, 255), (185, 0, 180, 180))
                third = pg.draw.rect(win, (255, 255, 255), (370, 0, 180, 180))
                fourth = pg.draw.rect(win, (255, 255, 255), (0, 185, 180, 180))
                fifth = pg.draw.rect(win, (255, 255, 255), (185, 185, 180, 180))
                sixth = pg.draw.rect(win, (255, 255, 255), (370, 185, 180, 180))
                seventh = pg.draw.rect(win, (255, 255, 255), (0, 370, 180, 180))
                eighth = pg.draw.rect(win, (255, 255, 255), (185, 370, 180, 180))
                ninth = pg.draw.rect(win, (255, 255, 255), (370, 370, 180, 180))
                first_open = True
                second_open = True
                third_open = True
                fourth_open = True
                fifth_open = True
                sixth_open = True
                seventh_open = True
                eighth_open = True
                ninth_open = True
                board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                won = False
                run = True
                draw_object = 'x'

        if event.type == pg.MOUSEBUTTONUP:
            pos = pg.mouse.get_pos()

            if won != True:
                if first.collidepoint(pos) and first_open:
                    if draw_object == 'x':
                        win.blit(x, (0, 0))
                        draw_object = 'o'
                        board[0][0] = 1
                    else:
                        win.blit(o, (0, 0))
                        draw_object = 'x'
                        board[0][0] = 2
                    first_open = False

                if second.collidepoint(pos) and second_open:
                    if draw_object == 'x':
                        win.blit(x, (185, 0))
                        draw_object = 'o'
                        board[0][1] = 1
                    else:
                        win.blit(o, (185, 0))
                        draw_object = 'x'
                        board[0][1] = 2
                    second_open = False

                if third.collidepoint(pos) and third_open:
                    if draw_object == 'x':
                        win.blit(x, (375, 0))
                        draw_object = 'o'
                        board[0][2] = 1
                    else:
                        win.blit(o, (375, 0))
                        draw_object = 'x'
                        board[0][2] = 2
                    third_open = False

                if fourth.collidepoint(pos) and fourth_open:
                    if draw_object == 'x':
                        win.blit(x, (0, 185))
                        draw_object = 'o'
                        board[1][0] = 1
                    else:
                        win.blit(o, (0, 185))
                        draw_object = 'x'
                        board[1][0] = 2
                    fourth_open = False

                if fifth.collidepoint(pos) and fifth_open:
                    if draw_object == 'x':
                        win.blit(x, (185, 185))
                        draw_object = 'o'
                        board[1][1] = 1
                    else:
                        win.blit(o, (185, 185))
                        draw_object = 'x'
                        board[1][1] = 2
                    fifth_open = False

                if sixth.collidepoint(pos) and sixth_open:
                    if draw_object == 'x':
                        win.blit(x, (370, 185))
                        draw_object = 'o'
                        board[1][2] = 1
                    else:
                        win.blit(o, (370, 185))
                        draw_object = 'x'
                        board[1][2] = 2
                    sixth_open = False

                if seventh.collidepoint(pos) and seventh_open:
                    if draw_object == 'x':
                        win.blit(x, (0, 370))
                        draw_object = 'o'
                        board[2][0] = 1
                    else:
                        win.blit(o, (0, 370))
                        draw_object = 'x'
                        board[2][0] = 2
                    seventh_open = False

                if eighth.collidepoint(pos) and eighth_open:
                    if draw_object == 'x':
                        win.blit(x, (185, 370))
                        draw_object = 'o'
                        board[2][1] = 1
                    else:
                        win.blit(o, (185, 370))
                        draw_object = 'x'
                        board[2][1] = 2
                    eighth_open = False

                if ninth.collidepoint(pos) and ninth_open:
                    if draw_object == 'x':
                        win.blit(x, (370, 370))
                        draw_object = 'o'
                        board[2][2] = 1
                    else:
                        win.blit(o, (370, 370))
                        draw_object = 'x'
                        board[2][2] = 2
                    ninth_open = False
                    
    pg.display.update()
    pg.time.delay(100)

    if win_check(1):
        won = True
        win.fill((0, 0, 0))
        font1 = pg.font.Font(None, 50)
        font2 = pg.font.Font(None, 26)
        text = font1.render("Player One has won", True, (255, 255, 255))
        play_again = font2.render("Press space to play again", True, (255, 255 ,255))
        win.blit(text, [120, 200])
        win.blit(play_again, [160, 450])
    elif win_check(2):
        won = True
        win.fill((0, 0, 0))
        font1 = pg.font.Font(None, 50)
        font2 = pg.font.Font(None, 26)
        text = font1.render("Player Two has won", True, (255, 255, 255))
        play_again = font2.render("Press space to play again", True, (255, 255, 255))
        win.blit(text, [120, 200])
        win.blit(play_again, [160, 450])

    elif full_check():
        won = True
        win.fill((0, 0, 0))
        font1 = pg.font.Font(None, 70)
        font2 = pg.font.Font(None, 26)
        text = font1.render("Draw", True, (255, 255, 255))
        play_again = font2.render("Press space to play again", True, (255, 255, 255))
        win.blit(text, [200, 200])
        win.blit(play_again, [160, 450])

    pg.display.update()

pg.quit()
