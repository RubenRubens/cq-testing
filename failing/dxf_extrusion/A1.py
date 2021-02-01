# issue 515

import cadquery as cq

result = (
    cq.importers.importDXF('dxf_extrusion/test.dxf')
    .wires().toPending()
    .offset2D(2)
    .extrude(10)
    .faces('>Z')
    .chamfer(1)
)
