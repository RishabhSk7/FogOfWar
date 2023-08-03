import json
from descartes import PolygonPatch
from matplotlib import pyplot as plt
from mpl_interactions import ioff, panhandler, zoom_factory
import streamlit as st

with open("Uttarakhand.geojson") as file:
    data = json.load(file)

#print(data.keys())
geometry = data["features"]
fig = plt.figure() 
ax = fig.gca()
print(ax)
plt.show()
for x in geometry:

    ax.add_patch(PolygonPatch(x["geometry"], fc="#6699cc", ec="#6699cc", alpha=0.5, zorder=2))
    ax.axis('scaled')

st.pyplot(fig)