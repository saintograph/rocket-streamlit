import streamlit as st
import numpy as np
from rocketpy import Environment, SolidMotor, Rocket, Flight
import datetime
import io
import contextlib
import matplotlib.pyplot as plt

tomorrow = datetime.date.today() + datetime.timedelta(days=1)

st.title('RocketPy Computations')

latitude = st.slider("Latitude", -90.00, 90.00)
longitude = st.slider("Longitude", -180.00, 179.00) # longitudes exclude 180
elevation = st.slider("Elevation", 0, 10000)

st.write("Latitude:", latitude, "Longitude:", longitude, "Elevation:", elevation)

env = Environment(latitude=latitude, longitude=longitude, elevation=elevation)

start_date = st.date_input('Select a date from the future', key='start')
st.write(int(start_date.strftime("%Y")), int(start_date.strftime("%m")), int(start_date.strftime("%d")))

env.set_date(
    (int(start_date.strftime("%Y")), int(start_date.strftime("%m")), int(start_date.strftime("%d")), 12)
)

env.set_atmospheric_model(type="Forecast", file="GFS")


# f = io.StringIO()

# with contextlib.redirect_stdout(f):
#     original_show = plt.show
#     plt.show = lambda: None

#     env.info()

#     plt.show = original_show

# output = f.getvalue()
# st.text(output)

# fig_nums = plt.get_fignums()

# if fig_nums:
#     for num in fig_nums:
#         fig = plt.figure(num)
#         st.pyplot(fig)
# else:
#     st.write("No plots were generated.")
if st.button("Run Simulation", type="primary"):
    f = io.StringIO()

    with contextlib.redirect_stdout(f):
        original_show = plt.show
        plt.show = lambda: None

        env.info()

        plt.show = original_show

    output = f.getvalue()
    st.text(output)

    fig_nums = plt.get_fignums()

    if fig_nums:
        for num in fig_nums:
            fig = plt.figure(num)
            st.pyplot(fig)
    else:
        st.write("No plots were generated.")
else:
    st.write("Press the button to run computations.")
