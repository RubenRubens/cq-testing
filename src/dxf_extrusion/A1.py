# issue https://github.com/CadQuery/cadquery/issues/515

import cadquery as cq

result = (
    cq.importers.importDXF('src/dxf_extrusion/test.dxf')
    .wires().toPending()
    .offset2D(2)
    .extrude(10)
    .faces('>Z')
    .chamfer(1)
)
