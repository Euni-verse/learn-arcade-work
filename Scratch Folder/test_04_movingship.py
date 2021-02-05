import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

def the_sea():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.CHARCOAL)

def hill():
    arcade.draw_arc_filled(290, 190, 130, 100, arcade.color.ONYX, 0, 180)

def lighthouse():

    # draw lighthouse roof
    arcade.draw_triangle_filled(290, 390, 320, 365, 260, 365, arcade.color.BRASS)

    # draw lighthouse top level
    arcade.draw_rectangle_filled(290, 350, 50, 30, arcade.color.BONE)

    # draw lighthouse bottom level
    arcade.draw_rectangle_filled(290, 280, 60, 100, arcade.color.BONE)

    # draw lighthouse top window
    arcade.draw_rectangle_filled(290, 348, 15, 15, arcade.color.EERIE_BLACK)

    # draw lighthouse two bottom windows
    arcade.draw_rectangle_filled(290, 305, 15, 15, arcade.color.EERIE_BLACK)
    arcade.draw_rectangle_filled(290, 270, 15, 15, arcade.color.EERIE_BLACK)

    # draw lighthouse balcony
    arcade.draw_rectangle_filled(290, 330, 60, 10, arcade.color.BRASS)

def lighthouse_light():
    # draw lighthouse light (right)
    arcade.draw_polygon_filled(((298, 340),
                                (298, 355),
                                (599, 450),
                                (599, 300)
                                ),
                                arcade.color.AERO_BLUE)
    # draw lighthouse light (left)
    arcade.draw_polygon_filled(((283, 340),
                                (283, 355),
                                (0, 450),
                                (0, 300)
                                ),
                                arcade.color.AERO_BLUE)

def sun(x, y):
    arcade.draw_circle_filled(x, y, 29, arcade.color.FLORAL_WHITE)

def cloud(x, y):
    """Draw the first cloud"""

    # draw a cloud
    arcade.draw_circle_filled(x + 70, y + 9, 13, arcade.color.CHARCOAL)
    arcade.draw_circle_filled(x + 50, y + 6, 10, arcade.color.CHARCOAL)
    arcade.draw_circle_filled(x + 60, y, 15, arcade.color.CHARCOAL)
    arcade.draw_circle_filled(x + 80, y, 15, arcade.color.CHARCOAL)
    arcade.draw_circle_filled(x + 40, y, 10, arcade.color.CHARCOAL)
    arcade.draw_circle_filled(x + 30, y, 15, arcade.color.CHARCOAL)
    arcade.draw_circle_filled(x + 10, y, 10, arcade.color.CHARCOAL)
    arcade.draw_circle_filled(x, y, 5, arcade.color.CHARCOAL)


def on_draw(delta_time):
    """Draw everything"""
    arcade.start_render()

    sun(500, on_draw.sun1_y)
    the_sea()
    lighthouse()
    lighthouse_light()
    hill()
    cloud(on_draw.cloud1_x, 400)
    cloud(on_draw.cloud2_x, 500)

    # sun going down
    on_draw.sun1_y -=1

    # clouds moving
    on_draw.cloud1_x += 1
    on_draw.cloud2_x -= 1

on_draw.sun1_y = 500
on_draw.cloud1_x = 50
on_draw.cloud2_x = 400

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Moving Ship")
    arcade.set_background_color(arcade.color.ETON_BLUE)

    # Call on_draw every 60th of a second
    arcade.schedule(on_draw, 1/60)

    arcade.run()

main()
