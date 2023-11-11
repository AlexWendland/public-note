---
aliases:
  - object
  - Objects
  - objects
chatgpt: false
created: 2023-07-11
last_edited: 2023-07-11
publish: true
tags: programming, oop
type: theory
---
# Object

An object keeps data behind an interface. It makes its internal variables private. Then exposes setter functions that allow people to edit in there preferred way. It also has getter functions to provide the methods to get at the data how they would like to access it.

The following would be a [[Data structure|data structure]].
```python
class point:
	x : float
	y : float

	def init(self, x: float, y: float):
		self.x = x
		self.y = y
```

Whereas the following would be an object.
```python
import math

class point:
	_x : float
	_y : float

	def init(self, x: float, y: float):
		self.set_cartesian(x, y)

	def set_cartesian(self, x: float, y: float):
		self._x = x
		self._y = y

	@classmethod
	def from_cartesian(cls, x: float, y: float):
		return cls(x,y)

	def get_cartesian(self):
		return self._x, self._y

	def set_polar(self, radius: float, theta: float)
		self._x, self._y = self.convert_polar_to_cartesian(radius, theta)

	@classmethod
	def from_polar(cls, radius: float, theta: float):
		x, y = convert_polar_to_cartesian(radius, theta)
		return cls(x,y)


	def convert_polar_to_cartesian(self, radius: float, theta: float)
		self._x = radius*math.sin(theta)
		self._y = radius*math.cos(theta)

	def get_polar(self):
		...
```

Whilst this might look quite similar, the purpose of the class variables `_x` and `_y` is not to be accessed by code outside of the point class. You only access or edit data through the interface you define. We do this so the interface can stay fixed but the implementation could change. In this example if we wanted to switch from storing points in cartesian to polar, we could do so without the user ever knowing.
