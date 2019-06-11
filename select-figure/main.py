# -*- coding: utf-8 -*-
# pylint: disable=unsubscriptable-object, too-many-locals
from __future__ import print_function
from __future__ import absolute_import
from os.path import dirname, join

from bokeh.layouts import layout
import bokeh.models as bmd
from bokeh.io import curdoc

#html = bmd.Div(
#    text=open(join(dirname(__file__), "static", "table.html")).read(),
#    width=960)
#curdoc().add_root(layout([html]))

# Put the tabs in the current document for display
curdoc().title = "AIRSS structures"
curdoc().template_variables["figures"] = [
    ["2", "Volume <i>vs</i> Enthalpy (number of atoms legend)"],
    ["3", "Volume <i>vs</i> Pressure (number of atoms legend)"],
    ["4", "Volume <i>vs</i> Pressure (enthalpy legend)"]
]
