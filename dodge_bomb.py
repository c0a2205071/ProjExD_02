import random  #練習2
import sys

import pygame as pg


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)

    tmr = 0
    bb_image = pg.Surface((20, 20))  #練習1
    pg.draw.circle(bb_image, (255, 0, 0), (10, 10), 10)  #練習1
    bb_image.set_colorkey((0, 0, 0))  #練習1
    x, y = random.randint(0, 1600), random.randint(0, 900)  #練習2
    screen.blit(bb_image, [x, y])  #練習2
    vx, vy = +1, +1  #練習3
    bb_rect = bb_image.get_rect()  #練習3
    bb_rect.center = (x, y)  #練習3

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0
        tmr += 1
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        bb_rect.move_ip(vx, vy)  #練習3
        screen.blit(bb_image, bb_rect)

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()