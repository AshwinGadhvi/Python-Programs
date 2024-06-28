# Online Python-3 Compiler (Interpreter)
import pandas as pd
import matplotlib.pyplot as plt

# Create a dataframe with disease information
disease_data = {
    'Disease': [
        'Phytophthora Blight', 'Verticillium Wilt', 'Bacterial Wilt',
        'Fusarium Wilt', 'Anthracnose', 'Whitefly', 'Spider mites',
        'Fruit Rot', 'Leaf spot', 'Powdery Mildew', 'Root knot nematode',
        'Stem Canker', 'Black Mold', 'Gray Mold', 'Southern Blight',
        'Stem Rot', 'Leaf Curl', 'Mosaic Virus', 'Damping off'
    ],
    'Causal Organism': [
        'Phytophthora capsici', 'Verticillium dahliae',
        'Ralstonia solanacearum', 'Fusarium oxysporum',
        'Colletotrichum gloeosporioides', 'Bemisia tabaci',
        'Tetranychus urticae', 'Botrytis cinerea', 'Alternaria solani',
        'Leveillula taurica', 'Meloidogyne incognita', 'Diaporthe helianthi',
        'Aureobasidium pullulans', 'Botrytis cinerea', 'Sclerotium rolfsii',
        'Sclerotinia sclerotiorum', 'Begomovirus', 'Cucumber mosaic virus',
        'Pythium spp.'
    ],
    'Optimum Temperature Range': [
        '20-30°C', '20-25°C', '30-35°C', '25-30°C', '24-28°C', '24-27°C',
        '24-27°C', '18-25°C', '20-25°C', '20-25°C', '28-32°C', '24-27°C',
        '18-24°C', '15-25°C', '28-30°C', '20-25°C', '25-30°C', '20-28°C',
        '20-25°C'
    ],
    'Optimum Humidity Range': [
        '90% or higher', '80% or higher', '70-90%', 'Low humidity',
        'High humidity', '50-60%', '60-70%', '90% or higher', '80-90%',
        '60-80%', '60-70%', '80% or higher', '90% or higher', '90% or higher',
        '60-80%', '80-90%', '60-70%', '60-80%', 'High humidity'
    ],
    'Climate Preference': [
        'Warm and humid', 'Cool and moist', 'Warm and humid', 'Hot and dry',
        'Warm and humid', 'Warm and humid', 'Hot and dry', 'Cool and humid',
        'Warm and moist', 'Warm and dry', 'Warm and humid', 'Warm and humid',
        'Cool and humid', 'Cool and humid', 'Warm and humid', 'Cool and moist',
        'Warm and dry', 'Warm and moist', 'Warm and moist'
    ]
}

df = pd.DataFrame(disease_data)

# Create a bar chart for optimum temperature range
plt.bar(df['Disease'], df['Optimum Temperature Range'])
plt.xticks(rotation=90)
plt.ylabel('Temperature (°C)')
plt.title('Optimum Temperature Range for Eggplant Diseases')

# Create a bar chart for optimum humidity range
plt.bar(df['Disease'], df['Optimum Humidity Range'])
plt.xticks(rotation=90)
plt.ylabel('Humidity (%)')
plt.title('Optimum Humidity Range for Eggplant Diseases')

# Create a horizontal bar chart for climate preference
plt.barh(df['Disease'], df['Climate Preference'])
plt.xlabel('Climate Preference')
plt.title('Climate Preference for Eggplant Diseases')

plt.show()