class Bbox:
    def __init__(self, x0, y0, x1, y1):
        self._x0 = x0
        self._y0 = y0
        self._x1 = x1
        self._y1 = y1

    def __repr__(self):
        return f"(({self._x0}, {self._y0}), ({self._x1}, {self._y1}))"

    def __update_bbox(self):
        self._x0, self._y0 = self._y0, self._x0

    def __eq__(self, other):
        return self._x0 == other._x0 and self._y0 == other._y0


    def __add__(self, other):
        x0 = min(self._x0, other._x0)
        y0 = min(self._y0, other._y0)
        x1 = max(self._x1, other._x1)
        y1 = max(self._y1, other._y1)
        return Bbox(x0, y0, x1, y1)

    @staticmethod
    def distance(a0, b0, a1, b1):
        return ((a1 - a0) ** 2 + (b1 - b0) ** 2) ** 0.5

    @property
    def x0(self):
        self.__update_bbox()
        return self._x0

    @property
    def y0(self):
        self.__update_bbox()
        return self._y0

bbox_1 = Bbox(3, 5, 15, 18)
bbox_2 = Bbox(3, 5, 15, 18)
bbox_1._Bbox__update_bbox()
print(bbox_1)
# bbox_3 = bbox_1 + bbox_2
# print(bbox_3)
#
# if bbox_1 == bbox_2:
#     print("!!!!!!!!!!")
# print(bbox_1.distance(0,0,3,4))
# print(bbox_1.x0)
# print(bbox_1.y0)
# print(bbox_1.y0)
