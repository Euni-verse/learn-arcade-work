""" This is a drawing
"""

# import arcade library
import arcade

# open a drawing window
arcade.open_window(600, 600, "Drawing Example")

# set the background color
arcade.set_background_color(arcade.color.BITTERSWEET)

# get ready to draw
arcade.start_render()

# draw a rectangle
# left of 0, right of 599, top of 300, bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.color.APRICOT)

# draw a tree trunk
# center of x-100, y-320
# width of 20
# height of 60
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.color.BISTRE)

# draw a rectangle outline
arcade.draw_rectangle_outline(100, 320, 20, 60, arcade.color.BLACK_BEAN)

# tree top - circle
# center of 100, 350, radius of 30 pixels
arcade.draw_circle_filled(100, 350, 30, arcade.color.BITTER_LIME)

# draw another tree, with an ellipse for the top
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.color.BISTRE)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.color.BITTER_LIME)

# draw another tree, with a trunk and arc for the top
# arc is centered at (300, 340) with a width of 60 and height of 100
# the starting angle is 0, and ending angle is 180
arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.color.BISTRE)
arcade.draw_arc_filled(300, 340, 60, 100, arcade.color.BITTER_LIME, 0, 180)

# draw an arc
arcade.draw_arc_outline(400, 200, 10, 5, arcade.color.BURGUNDY, 0, 180)

# draw another tree with a trunk and triangle
# triangle is made of these points:
# (400, 400), (370, 320), (430, 320)
arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.color.BISTRE)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.color.BITTER_LIME)

# draw a tree using a polygon with a list of points
arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.color.BISTRE)
arcade.draw_polygon_filled(((500, 400),
                            (480, 360),
                            (470, 320),
                            (530, 320),
                            (520, 360)
                            ),
                            arcade.color.BITTER_LIME)

# draw a sun
arcade.draw_circle_filled(500, 550, 10, arcade.color.YELLOW)

arcade.draw_circle_outline(500, 550, 20, arcade.color.YELLOW, 3)
arcade.draw_circle_outline(500, 550, 30, arcade.color.YELLOW, 3)


# draw rays to the left, right, up, and down
# the last number is the line width
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)

# diagonal rays
arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)

# text
# the text to draw is the first paramater
# x and y location is the next
# followed by color and font size
arcade.draw_text("Plant a Tree!",
                200, 200,
                arcade.color.CATALINA_BLUE, 24)







# finish drawing
arcade.finish_render()

# keep the drawing window open
arcade.run()
