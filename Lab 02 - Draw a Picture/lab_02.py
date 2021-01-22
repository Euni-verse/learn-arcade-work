"""This is code for a nice drawing"""

# import arcade library
import arcade

# create a window
arcade.open_window(600, 600, "Lighthouse")

# set background color
arcade.set_background_color(arcade.color.ETON_BLUE)

# start drawing
arcade.start_render()

# draw ground
arcade.draw_lrtb_rectangle_filled(0, 599, 200, 0, arcade.color.EERIE_BLACK)

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
arcade.draw_arc_filled(290, 200, 130, 110, arcade.color.CHARCOAL, 0, 180)

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






# end drawing
arcade.finish_render()

# keep the drawing window open
arcade.run()
