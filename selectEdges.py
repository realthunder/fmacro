#!/usr/bin/python
import FreeCAD,FreeCADGui,Part,DraftGeomUtils

def selectEdges():
    s = FreeCADGui.Selection.getSelectionEx()
    if not s:
        return

    edges = {}

    for ss in s:
        edgesIndex = {}
        for i,e in enumerate(ss.Object.Shape.Edges):
            edgesIndex[e.hashCode()] = i+1

        for sub in ss.SubObjects:
            if not isinstance(sub.Surface,Part.Plane):
                continue
            for f in ss.Object.Shape.Faces:
                if not DraftGeomUtils.isCoplanar([sub,f]):
                    continue
                for e in f.Edges:
                    h = e.hashCode()
                    if h in edges:
                        continue
                    edges[h] = [ss.Object,edgesIndex[h]]

    if not edges:
        return

    FreeCADGui.Selection.clearSelection()
    for e in edges.itervalues():
        FreeCADGui.Selection.addSelection(e[0],'Edge'+str(e[1]))


selectEdges()





