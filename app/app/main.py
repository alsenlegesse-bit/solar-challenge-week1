import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Solar Dashboard", layout="wide")
st.title("☀️ Solar Energy Dashboard")
st.write("Comparing solar potential in West Africa")

data = {
    'Country': ['Benin', 'Sierra Leone', 'Togo'],
    'Average_GHI': [450, 420, 480],
    'Average_Temperature': [28, 26, 30]
}
df = pd.DataFrame(data)

st.subheader("Solar Data by Country")
st.dataframe(df)

st.subheader("Solar Potential Comparison")
fig, ax = plt.subplots()
df.plot(x='Country', y='Average_GHI', kind='bar', ax=ax)
plt.ylabel('GHI (W/m²)')
st.pyplot(fig)

st.success("Dashboard Working! 🎉")
