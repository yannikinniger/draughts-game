from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush


def draw_circle(rect_width, rect_height, x_offset, y_offset, painter, color):
    """
    Draws a circle on the Widget the painter belongs to
    :param rect_width: Width of the rectangle the circle should be drawn to
    :param rect_height: Height of the rectangle the circle should be drawn to
    :param x_offset: x offset from the top left rectangle
    :param y_offset: y offset from the top left rectangle
    :param painter: QPainter to draw the rectangle
    :param color: Color the circle should be filled with
    """
    size_reduction = 5
    painter.setBrush(QBrush(color))
    painter.save()
    painter.translate(x_offset, y_offset)

    circle_width = rect_width - size_reduction * 2
    circle_height = rect_height - size_reduction * 2
    painter.drawEllipse(size_reduction, size_reduction, circle_width, circle_height)
    painter.restore()


def draw_rect(rect_width, rect_height, x_offset, y_offset, painter, color):
    """
    Draws a rectangle on the Widget the painter belongs to
    :param rect_width: Width of the rectangle to be drawn
    :param rect_height: Height of the rectangle to be drawn
    :param x_offset: x offset from the top left rectangle
    :param y_offset: y offset from the top left rectangle
    :param painter: QPainter to draw the rectangle
    :param color: Color to fill the rectangle with
    """
    painter.save()
    painter.translate(x_offset, y_offset)
    painter.fillRect(0, 0, rect_width, rect_height, color)
    painter.restore()
