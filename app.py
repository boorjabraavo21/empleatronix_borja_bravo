import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Importamos el Dataframe
employees = pd.read_csv("./employees.csv")

# Mostramos todos los empleados
st.title("EMPLEATRONIX")
st.text("Todos los datos sobre los empleados en una aplicación")
st.dataframe(employees)

st.divider()

# Creamos la gráfica con sus diferentes opciones
col1, col2, col3 = st.columns(3)

color = col1.color_picker(label="Elige un color para las barras", value="#0083F9")
name_toggle = col2.toggle("Mostrar el nombre", value=True)
salary_toggle = col3.toggle("Mostrar sueldo en la barra")

fig, ax = plt.subplots()
barh = ax.barh(y=employees['full name'], width=employees['salary'], color=color)
ax.set_xlim(right=employees["salary"].max() + 500)

if name_toggle:
    ax.set_yticks(range(len(employees['full name'])))
    ax.set_yticklabels(employees["full name"])
else:
    ax.set_yticks(range(len(employees['full name'])))
    ax.set_yticklabels([])

bar_labels = []
if salary_toggle:
    labels = [f"{salary}€" for salary in employees["salary"]]
    bar_labels = ax.bar_label(ax.containers[0], labels=labels, padding=5)
else:
    for label in bar_labels:
        label.remove()

# Mostramos la gráfica
st.pyplot(fig)