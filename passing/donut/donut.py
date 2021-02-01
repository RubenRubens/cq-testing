# issue 259

import cadquery as cq

result = cq.Workplane('XY').circle(10).revolve(360, [-30,0,0], [-30,1,0])
