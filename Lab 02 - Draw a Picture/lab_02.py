"""This is code for a nice drawing"""

# import arcade library
import arcade

# create a window
arcade.open_window(600, 600, "Lighthouse")

# set background color
arcade.set_background_color(arcade.color.ETON_BLUE)

# start drawing
arcade.start_render()

# draw ground (once was EERIE_BLACK)
arcade.draw_lrtb_rectangle_filled(0, 599, 195, 0, arcade.color.CHARCOAL)


# draw light arcade.draw_lrtb_rectangle_filled(0, 599, 400, 300, arcade.color.AERO_BLUE)

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

# draw a hill
arcade.draw_arc_filled(290, 190, 130, 100, arcade.color.ONYX, 0, 180)

# draw lighthouse light (right + left)
arcade.draw_polygon_filled(((298, 340),
                            (298, 355),
                            (599, 450),
                            (599, 300)
                            ),
                            arcade.color.AERO_BLUE)
arcade.draw_polygon_filled(((283, 340),
                            (283, 355),
                            (0, 450),
                            (0, 300)
                            ),
                            arcade.color.AERO_BLUE)

# draw a sun
arcade.draw_circle_filled(500, 500, 29, arcade.color.FLORAL_WHITE)

# draw a cloud (bottom of the sun)
arcade.draw_circle_filled(395, 449, 13, arcade.color.CHARCOAL)
arcade.draw_circle_filled(375, 446, 10, arcade.color.CHARCOAL)
arcade.draw_circle_filled(385, 440, 15, arcade.color.CHARCOAL)
arcade.draw_circle_filled(405, 440, 15, arcade.color.CHARCOAL)
arcade.draw_circle_filled(365, 440, 10, arcade.color.CHARCOAL)
arcade.draw_circle_filled(355, 440, 15, arcade.color.CHARCOAL)
arcade.draw_circle_filled(335, 440, 10, arcade.color.CHARCOAL)
arcade.draw_circle_filled(325, 440, 5, arcade.color.CHARCOAL)


# draw a cloud (to the left of the sun)
arcade.draw_circle_filled(475, 499, 14, arcade.color.CHARCOAL)
arcade.draw_circle_filled(455, 496, 10, arcade.color.CHARCOAL)
arcade.draw_circle_filled(465, 490, 11, arcade.color.CHARCOAL)
arcade.draw_circle_filled(485, 490, 8, arcade.color.CHARCOAL)
arcade.draw_circle_filled(445, 490, 10, arcade.color.CHARCOAL)
arcade.draw_circle_filled(435, 490, 8, arcade.color.CHARCOAL)
arcade.draw_circle_filled(496, 490, 10, arcade.color.CHARCOAL)
arcade.draw_circle_filled(508, 490, 6, arcade.color.CHARCOAL)

# draw a cloud (to the right of the sun)
arcade.draw_circle_filled(565, 499, 12, arcade.color.CHARCOAL)
arcade.draw_circle_filled(545, 496, 9, arcade.color.CHARCOAL)
arcade.draw_circle_filled(555, 490, 12, arcade.color.CHARCOAL)
arcade.draw_circle_filled(575, 490, 14, arcade.color.CHARCOAL)
arcade.draw_circle_filled(535, 490, 10, arcade.color.CHARCOAL)
arcade.draw_circle_filled(525, 490, 6, arcade.color.CHARCOAL)
arcade.draw_circle_filled(520, 490, 5, arcade.color.CHARCOAL)

# draw cloud one (far left)
arcade.draw_circle_filled(75, 469, 10, arcade.color.CHARCOAL)
arcade.draw_circle_filled(55, 466, 12, arcade.color.CHARCOAL)
arcade.draw_circle_filled(65, 460, 15, arcade.color.CHARCOAL)
arcade.draw_circle_filled(85, 460, 12, arcade.color.CHARCOAL)
arcade.draw_circle_filled(45, 460, 9, arcade.color.CHARCOAL)
arcade.draw_circle_filled(35, 460, 5, arcade.color.CHARCOAL)
arcade.draw_circle_filled(96, 460, 10, arcade.color.CHARCOAL)
arcade.draw_circle_filled(110, 460, 8, arcade.color.CHARCOAL)

# draw cloud one (middle)
arcade.draw_circle_filled(175, 499, 10, arcade.color.CHARCOAL)
arcade.draw_circle_filled(155, 496, 14, arcade.color.CHARCOAL)
arcade.draw_circle_filled(165, 490, 15, arcade.color.CHARCOAL)
arcade.draw_circle_filled(185, 490, 11, arcade.color.CHARCOAL)
arcade.draw_circle_filled(145, 490, 7, arcade.color.CHARCOAL)
arcade.draw_circle_filled(135, 490, 9, arcade.color.CHARCOAL)
arcade.draw_circle_filled(196, 490, 10, arcade.color.CHARCOAL)
arcade.draw_circle_filled(210, 490, 5, arcade.color.CHARCOAL)

# draw waves (left)
arcade.draw_arc_outline(30, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(40, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(50, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(60, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(70, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(80, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(90, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(100, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(110, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(120, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(130, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(140, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(150, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(160, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(170, 180, 10, 5, arcade.color.BONE, 0, 180)

arcade.draw_arc_outline(110, 160, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(120, 160, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(130, 160, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(140, 160, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(150, 160, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(160, 160, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(170, 160, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(180, 160, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(190, 160, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(200, 160, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(210, 160, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(220, 160, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(230, 160, 10, 5, arcade.color.BONE, 0, 180)

arcade.draw_arc_outline(150, 140, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(160, 140, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(170, 140, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(180, 140, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(190, 140, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(200, 140, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(210, 140, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(220, 140, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(230, 140, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(240, 140, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(250, 140, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(260, 140, 10, 5, arcade.color.BONE, 0, 180)

arcade.draw_arc_outline(70, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(80, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(90, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(100, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(110, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(120, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(130, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(140, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(150, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(160, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(170, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(180, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(190, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(200, 120, 10, 5, arcade.color.BONE, 0, 180)

arcade.draw_arc_outline(20, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(30, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(40, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(50, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(60, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(70, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(80, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(90, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(100, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(110, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(120, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(130, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(140, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(150, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(160, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(170, 100, 10, 5, arcade.color.BONE, 0, 180)

arcade.draw_arc_outline(50, 80, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(60, 80, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(70, 80, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(80, 80, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(90, 80, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(100, 80, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(110, 80, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(120, 80, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(130, 80, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(140, 80, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(150, 80, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(160, 80, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(170, 80, 10, 5, arcade.color.BONE, 0, 180)

arcade.draw_arc_outline(150, 60, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(160, 60, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(170, 60, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(180, 60, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(190, 60, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(200, 60, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(210, 60, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(220, 60, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(230, 60, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(240, 60, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(250, 60, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(260, 60, 10, 5, arcade.color.BONE, 0, 180)

arcade.draw_arc_outline(70, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(80, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(90, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(100, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(110, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(120, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(130, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(140, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(150, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(160, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(170, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(180, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(190, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(200, 40, 10, 5, arcade.color.BONE, 0, 180)

arcade.draw_arc_outline(20, 20, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(30, 20, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(40, 20, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(50, 20, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(60, 20, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(70, 20, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(80, 20, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(90, 20, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(100, 20, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(110, 20, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(120, 20, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(130, 20, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(140, 20, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(150, 20, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(160, 20, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(170, 20, 10, 5, arcade.color.BONE, 0, 180)

# draw waves (right)

arcade.draw_arc_outline(420, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(430, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(440, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(450, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(460, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(470, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(480, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(490, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(500, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(510, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(520, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(530, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(540, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(550, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(560, 180, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(570, 180, 10, 5, arcade.color.BONE, 0, 180)

arcade.draw_arc_outline(470, 160, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(480, 160, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(490, 160, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(500, 160, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(510, 160, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(520, 160, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(530, 160, 10, 5, arcade.color.BONE, 0, 180)

arcade.draw_arc_outline(430, 140, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(440, 140, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(450, 140, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(460, 140, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(470, 140, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(480, 140, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(490, 140, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(500, 140, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(510, 140, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(520, 140, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(530, 140, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(540, 140, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(550, 140, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(560, 140, 10, 5, arcade.color.BONE, 0, 180)

arcade.draw_arc_outline(340, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(350, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(360, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(370, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(380, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(390, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(400, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(410, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(420, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(430, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(440, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(450, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(460, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(470, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(480, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(490, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(500, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(510, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(520, 120, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(530, 120, 10, 5, arcade.color.BONE, 0, 180)

arcade.draw_arc_outline(430, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(440, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(450, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(460, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(470, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(480, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(490, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(500, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(510, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(520, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(530, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(540, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(550, 100, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(560, 100, 10, 5, arcade.color.BONE, 0, 180)

arcade.draw_arc_outline(370, 80, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(380, 80, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(390, 80, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(400, 80, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(410, 80, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(420, 80, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(430, 80, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(440, 80, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(450, 80, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(460, 80, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(470, 80, 10, 5, arcade.color.BONE, 0, 180)

arcade.draw_arc_outline(380, 60, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(390, 60, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(400, 60, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(410, 60, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(420, 60, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(430, 60, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(440, 60, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(450, 60, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(460, 60, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(470, 60, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(480, 60, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(490, 60, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(500, 60, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(510, 60, 10, 5, arcade.color.BONE, 0, 180)

arcade.draw_arc_outline(450, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(460, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(470, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(480, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(490, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(500, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(510, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(520, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(530, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(540, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(550, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(560, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(570, 40, 10, 5, arcade.color.BONE, 0, 180)
arcade.draw_arc_outline(580, 40, 10, 5, arcade.color.BONE, 0, 180)





# end drawing
arcade.finish_render()

# keep the drawing window open
arcade.run()
