import random  # 練習2
import sys

import pygame as pg

delta = {
         pg.K_UP:(0, -1) ,
         pg.K_DOWN: (0, 1),
         pg.K_LEFT: (-1, 0),
         pg.K_RIGHT: (1, 0),
         }
 # 練習4

def check_bound(scr_rect: pg.rect, obj_rect: pg.rect) -> tuple[bool, bool]:
    """
    オブジェクトが画面内or画面買いを判定し、真理値タプルを返す関数
    引数1：画面SurfaceのRect
    引数2：こうかとんまたは爆弾SurfaceのRect
    戻り値：横方向縦方向のはみだし判定の結果
    """
    yoko, tate = True, True
    if obj_rect.left < scr_rect.left or scr_rect.right < obj_rect.right:
        yoko = False
    if obj_rect.top < scr_rect.top or scr_rect.bottom < obj_rect.bottom:
        tate = False
    return yoko, tate
# 練習5

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)

    tmr = 0
    bb_image = pg.Surface((20, 20))  # 練習1
    pg.draw.circle(bb_image, (255, 0, 0), (10, 10), 10)  # 練習1
    bb_image.set_colorkey((0, 0, 0))  # 練習1
    x, y = random.randint(0, 1600), random.randint(0, 900)  # 練習2
    screen.blit(bb_image, [x, y])  # 練習2
    vx, vy = +1, +1  # 練習3
    bb_rect = bb_image.get_rect()  # 練習3
    bb_rect.center = (x, y)  # 練習3
    kk_rect = kk_img.get_rect()  # 練習4
    kk_rect.center = (900, 400)   # 練習4

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0
        tmr += 1

        key_list = pg.key.get_pressed()  # 練習4
        for k, mv in delta.items():  # 練習4
            if key_list[k]:  # 練習4
                kk_rect.move_ip(mv)  # 練習4
        if check_bound(screen.get_rect(), kk_rect) != (True, True):  # 練習5
            for k, mv in delta.items():  # 練習5
                if key_list[k]:  # 練習5
                    kk_rect.move_ip(-mv[0], -mv[1])  # 練習5
        screen.blit(bg_img, [0, 0])  # 練習4
        bb_rect.move_ip(vx, vy)  # 練習3
        yoko, tate = check_bound(screen.get_rect(), bb_rect)  # 練習5
        if not yoko:  # 練習5
            vx *= -1  # 練習5
        if not tate:  # 練習5
            vy *= -1  # 練習5
        screen.blit(bb_image, bb_rect)  # 練習3
        screen.blit(kk_img, kk_rect)  # 練習4

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()