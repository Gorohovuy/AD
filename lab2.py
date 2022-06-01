from spyre import server
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Lab1(server.App):
    title = "NOAA data vizualization"
    
    inputs = [{"type":'dropdown',
               "label": 'NOAA data dropdown',
               "options": [{"label": "VCI", "value":"VCI"},
                           {"label": "TCI", "value":"TCI"},
                           {"label": "VHI", "value":"VHI"}],
               "key": 'ticker',
               "action_id": "update_data"},
               {"type": 'dropdown',
                "key": "region",
                "label": "Region",
                "options": [{"label": "Черкаська", "value":"Черкаська"},
                           {"label": "Чернівська", "value":"Чернівська"},
                           {"label": "Чернівецька", "value":"Чернівецька"},
                           {"label": "Кримська", "value":"Кримська"},
                           {"label": "Дніпропетровська", "value":"Дніпропетровська"},
                           {"label": "Донецька", "value":"Донецька"},
                           {"label": "Івано-Франківська", "value":"Івано-Франківська"},
                           {"label": "Харківська", "value":"Харківська"},
                           {"label": "Херсонська", "value":"Херсонська"},
                           {"label": "Хмельницька", "value":"Хмельницька"},
                           {"label": "Київська", "value":"Київська"},
                           {"label": "Київ", "value":"Київ"},
                           {"label": "Кіровоградська", "value":"Кіровоградська"},
                           {"label": "Луганська", "value":"Луганська"},
                           {"label": "Львівська", "value":"Львівська"},
                           {"label": "Миколаївська", "value":"Миколаївська"},
                           {"label": "Одеська", "value":"Одеська"},
                           {"label": "Полтавська", "value":"Полтавська"},
                           {"label": "Рівенська", "value":"Рівенська"},
                           {"label": "Севастопіль", "value":"Севастопіль"},
                           {"label": "Сумська", "value":"Сумська"},
                           {"label": "Тернопільська", "value":"Тернопільська"},
                           {"label": "Закарпатська", "value":"Закарпатська"},
                           {"label": "Вінницька", "value":"Вінницька"},
                           {"label": "Волинська", "value":"Волинська"},
                           {"label": "Запорізька", "value":"Запорізька"},
                           {"label": "Житомирська", "value":"Житомирська"}],
                           "action_id": "update_data"},
                {"type": "text",
                 "key": "range",
                 "label": "Week-range",
                 "value": "9-10",
                 "action_id": "simple_html_output"},
                 {"type":"text",
                 "key": "year",
                 "label": "Input year range",
                 "value": "2000-2005",
                 "action_id": "simple_html_output"}]
            
    controls = [{    "type" : "hidden",
                    "id" : "update_data"}]

    tabs = ["Plot", "Table"]

    outputs = [{ "type" : "plot",
                    "id" : "plot",
                    "control_id" : "update_data",
                    "tab" : "Plot"},
                { "type" : "table",
                    "id" : "table_id",
                    "control_id" : "update_data",
                    "tab" : "Table",
                    "on_page_load" : True }]

    def getData(self, params):
        ticker = params["ticker"]
        rang = params["range"].split("-")
        region = params["region"]
        year = params["year"].split("-")
        url = "https://raw.githubusercontent.com/Gorohovuy/AD/master/rar.csv"
        df = pd.read_csv(url, index_col=0)
        df_res = df[(df["region"] == region) &
                     (df["Year"] >= int(year[0])) &
                     (df["Year"] <= int(year[1])) &
                     (df["Week"] >= int(rang[0])) &
                     (df["Week"] <= int(rang[1]))][["Year", "Week",ticker]]
        print(ticker, rang, region)
        return df_res

    def getPlot(self, params):
        ticker = params["ticker"]
        df = self.getData(params)
        plt.figure(figsize=(14,9))
        return sns.barplot(x="Year", y=ticker, hue="Week", data=df)
    
app = Lab1()
app.launch(port=8888)



