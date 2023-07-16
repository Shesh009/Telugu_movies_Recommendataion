import numpy as np
import pandas as pd
import streamlit as st

data=pd.read_csv("TeluguMovies_dataset.csv")
data["Movie"]=data["Movie"].values.astype(str)

data1=data[["Movie","Year","Genre","Rating","No.of.Ratings"]]

data2=data1[(data1["Year"]>2000) & (data1["No.of.Ratings"]>500)]
movies=data2["Movie"].values

st.title("MOVIE RECOMMENDATION SYSTEM")
mov_name=st.selectbox("MOVIE NAME",movies,index=0)
data3=data2[data2["Movie"]==mov_name]
x=data3['Rating'].iloc[0]
st.write(f"Rating : {x}")
data4=data2[(data2["Rating"]>=(x-0.1)) & (data2["Rating"]<=(x+0.1)) & (data2["Movie"]!=mov_name)].sort_values("No.of.Ratings",ascending=False)
mov=data4.Movie.values
rat=data4.Rating.values
year=data4.Year.values
genre=data4.Genre.values
st.header("Recommendations")
st.caption("Movies based on rating of movie selected")
col1,col2,col3,col4=st.columns(4)
col1.markdown(":red[Movie Name]")
col2.write(":blue[Year Released]")
col3.write(":green[Genre]")
col4.write(":orange[Rating]")

for i in range(0,5):
    cols=st.columns(4)
    cols[0].write(mov[i])
    cols[1].write(int(year[i]))    
    cols[2].write(genre[i])
    cols[3].write(rat[i])