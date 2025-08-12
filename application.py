import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI & Jobs", layout="centered")
st.markdown(
    """
    <h1 style='color:#87CEFA;'>Як штучний інтелект змінює сферу праці</h1>
    <p style='color:#708090; font-size:20px;'>Цей сайт створений на основі наукового дослідження, проведеного шістьма дівчатами в рамках проєкту ReuseScience. Ми провели ґрунтовний аналіз, зробили опитування та вивчили багато інших даних, щоб дослідити ризики автоматизації різних професій.</p>
    <h3 style='color:#00CED1;'>Дослідження ризиків автоматизації професій</h3>
    """,
    unsafe_allow_html=True
)





try:
    df = pd.read_csv("thefull.csv", sep=';', header=1, on_bad_lines='skip', encoding='utf-8')
except Exception as e:
    st.error(f"Помилка при читанні CSV: {e}")
    st.stop()

df.columns = df.columns.str.strip()  # видаляємо пробіли з назв колонок



profession = st.selectbox("Оберіть професію:", df['Професія'].unique())

row = df[df['Професія'] == profession].iloc[0]

risk = row['Рівень ризику']
advice = row['Порада']
projection = row['Прогноз']

st.subheader(f"Професія: {profession}")
st.write(f"**Рівень ризику:** {risk}")

if risk == "Високий":
    st.error("⚠️ Високий ризик автоматизації")
elif risk == "Середній":
    st.warning("ℹ️ Середній ризик автоматизації")
elif risk == "Низький":
    st.success("✅ Низький ризик автоматизації")


if '-' in advice:
    bold_part, rest = advice.split('-', 1)
    advice_formatted = f"**{bold_part.strip()}** - {rest.strip()}"
else:
    advice_formatted = advice

st.markdown(
    f"""
    <div style="background-color:#1b263b;padding:15px;border-radius:10px;margin-top:10px">
        <h4 style="margin-bottom:5px; color:#ffffff">💡 Порада</h4>
        <p style="font-size:16px; color:#ffffff">{advice_formatted}</p>
    </div>
    <div style="background-color:#0d1f0d;padding:15px;border-radius:10px;margin-top:10px">
        <h4 style="margin-bottom:5px; color:#f0f0f0">📊 Прогноз</h4>
        <p style="font-size:16px; color:#f0f0f0">{projection}</p>
    </div>
    """,
    unsafe_allow_html=True
)








