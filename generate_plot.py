import plotly.express as px
import pandas as pd
import numpy as np  # Lisää tämä rivi

# 1. Mockup-datan generointi
data = {
    'Aika': pd.date_range(start='1/1/2024', periods=100, freq='D'),
    'Arvo': np.random.rand(100) * 100  # Käytä numpyta suoraan
}
df = pd.DataFrame(data)

# 2. Plotin luominen
fig = px.line(df, x='Aika', y='Arvo', title='Päivitetty plotti Mockup-datalla')

# 3. HTML-tiedoston päivittäminen
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reliability Website</title>
</head>
<body>
    <h1>Päivitetty plotti Mockup-datalla</h1>
    <div>
        {fig.to_html(full_html=False, include_plotlyjs='cdn')}
    </div>
</body>
</html>
"""

with open('index.html', 'w') as f:
    f.write(html_content)
