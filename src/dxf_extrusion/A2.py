# issue 515

import cadquery as cq

result = (
    cq.importers.importDXF('src/dxf_extrusion/test.dxf')
    .wires().toPending()
    .offset2D(2,kind='intersection')
    .extrude(10)
    .faces('>Z')
    .chamfer(1)
)
