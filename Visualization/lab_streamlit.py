import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier


st.sidebar.header('Choise bus number')
cities = pd.read_csv('data.csv')

def user_input_features():
    
    busnumber = st.sidebar.slider('2156','2470' )
    data = {'busnumber': busnumber}
    features = pd.DataFrame(cities)
    return features


fig = go.Figure(go.Scattermapbox(lat=cities['Latit'], lon=cities['Long']))
fig.update_layout(mapbox_style="open-street-map")
fig.show()

with open(cities, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count > 0:
            for i in range(0,len(buses)):
                if row['Number'] == data[i] :
                  
        line_count += 1
        
fig = go.Figure(go.Scattermapbox(lat=cities['Latit'], lon=cities['Long']))
fig.update_layout(mapbox_style="open-street-map")
st.write(fig.show())


# iris = datasets.load_iris()
# X = iris.data
# Y = iris.target
# clf = RandomForestClassifier()
# clf.fit(X, Y)
# prediction = clf.predict(df)
# prediction_proba = clf.predict_proba(df)
# st.write("""# Simple Iris Flower Prediction App This app predicts the **Iris flower** type!""")
# st.write(df)
# st.subheader('Class labels and their corresponding index number')
# st.write(iris.target_names)
# st.subheader('Prediction')
# st.write(iris.target_names[prediction])
# st.subheader('Prediction Probability')
# st.write(prediction_proba)

