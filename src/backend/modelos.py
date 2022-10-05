
from datetime import datetime, timedelta

from modelo_geral import ModeloGeral, ModeloGeralPeriodo

import pickle
import joblib

# scaler
with open("./modelos/SCALER_file", "rb") as f:
    SCALER = pickle.load(f)

# # load knn models
# with open("./modelos/KNN_Fid_file", "rb") as f:
#     knn_fid = pickle.load(f)

# with open("./modelos/KNN_Rat_file", "rb") as f:
#     knn_rat = pickle.load(f)

# with open("./modelos/KNN_Share_file", "rb") as f:
#     knn_share = pickle.load(f)

# KNN_MODELO = ModeloGeral(knn_rat, knn_fid, knn_share)

# load knn models
lgbm_rat = joblib.load('./modelos/lgbm_rat.pkl')

lgbm_share = joblib.load('./modelos/lgbm_share.pkl')

# KNN_MODELO = ModeloGeral(knn_rat, knn_fid, knn_share)
LGBM_MODELO = ModeloGeralPeriodo(lgbm_rat, lgbm_share)


def convert_single_input(data_hora, feriado, categoria):
    category_map = {'Categoria_CARROS E MOTORES': 0, 'Categoria_CULINARIO': 0, 'Categoria_DEBATE': 0, 'Categoria_DOCUMENTARIO': 0, 'Categoria_EDUCATIVO': 0, 'Categoria_ENTREVISTA': 0, 'Categoria_ESPORTE': 0, 'Categoria_FEMININO': 0, 'Categoria_FILME': 0, 'Categoria_FUTEBOL': 0, 'Categoria_GAME SHOW': 0, 'Categoria_HUMORISTICO': 0, 'Categoria_JORNALISMO': 0,
                    'Categoria_MINISSERIE': 0, 'Categoria_MUSICAL': 0, 'Categoria_NOVELA': 0, 'Categoria_OUTROS': 0, 'Categoria_POLITICO': 0, 'Categoria_PREMIACAO': 0, 'Categoria_REALITY SHOW': 0, 'Categoria_RELIGIOSO': 0, 'Categoria_REPORTAGEM': 0, 'Categoria_RURAL': 0, 'Categoria_SERIES': 0, 'Categoria_SHOW': 0, 'Categoria_SORTEIO': 0, 'Categoria_TELE VENDAS': 0}

    dicionario_hora = {'6:00:00': 6, '6:05:00': 6, '6:10:00': 6, '6:15:00': 6.25, '6:20:00': 6.25, '6:25:00': 6.25, '6:30:00': 6.5, '6:35:00': 6.5, '6:40:00': 6.5, '6:45:00': 6.75, '6:50:00': 6.75, '6:55:00': 6.75, '7:00:00': 7, '7:05:00': 7, '7:10:00': 7, '7:15:00': 7.25, '7:20:00': 7.25, '7:25:00': 7.25, '7:30:00': 7.5, '7:35:00': 7.5, '7:40:00': 7.5, '7:45:00': 7.75, '7:50:00': 7.75, '7:55:00': 7.75, '8:00:00': 8, '8:05:00': 8, '8:10:00': 8, '8:15:00': 8.25, '8:20:00': 8.25, '8:25:00': 8.25, '8:30:00': 8.5, '8:35:00': 8.5, '8:40:00': 8.5, '8:45:00': 8.75, '8:50:00': 8.75, '8:55:00': 8.75, '9:00:00': 9, '9:05:00': 9, '9:10:00': 9, '9:15:00': 9.25, '9:20:00': 9.25, '9:25:00': 9.25, '9:30:00': 9.5, '9:35:00': 9.5, '9:40:00': 9.5, '9:45:00': 9.75, '9:50:00': 9.75, '9:55:00': 9.75, '10:00:00': 10, '10:05:00': 10, '10:10:00': 10, '10:15:00': 10.25, '10:20:00': 10.25, '10:25:00': 10.25, '10:30:00': 10.5, '10:35:00': 10.5, '10:40:00': 10.5, '10:45:00': 10.75, '10:50:00': 10.75, '10:55:00': 10.75, '11:00:00': 11, '11:05:00': 11, '11:10:00': 11, '11:15:00': 11.25, '11:20:00': 11.25, '11:25:00': 11.25, '11:30:00': 11.5, '11:35:00': 11.5, '11:40:00': 11.5, '11:45:00': 11.75, '11:50:00': 11.75, '11:55:00': 11.75, '12:00:00': 12, '12:05:00': 12, '12:10:00': 12, '12:15:00': 12.25, '12:20:00': 12.25, '12:25:00': 12.25, '12:30:00': 12.5, '12:35:00': 12.5, '12:40:00': 12.5, '12:45:00': 12.75, '12:50:00': 12.75, '12:55:00': 12.75, '13:00:00': 13, '13:05:00': 13, '13:10:00': 13, '13:15:00': 13.25, '13:20:00': 13.25, '13:25:00': 13.25, '13:30:00': 13.5, '13:35:00': 13.5, '13:40:00': 13.5, '13:45:00': 13.75, '13:50:00': 13.75, '13:55:00': 13.75, '14:00:00': 14, '14:05:00': 14, '14:10:00': 14, '14:15:00': 14.25, '14:20:00': 14.25, '14:25:00': 14.25, '14:30:00': 14.5, '14:35:00': 14.5, '14:40:00': 14.5, '14:45:00': 14.75, '14:50:00': 14.75, '14:55:00': 14.75, '15:00:00': 15, '15:05:00': 15, '15:10:00': 15, '15:15:00': 15.25, '15:20:00': 15.25, '15:25:00': 15.25, '15:30:00': 15.5, '15:35:00': 15.5, '15:40:00': 15.5, '15:45:00': 15.75, '15:50:00': 15.75, '15:55:00': 15.75, '16:00:00': 16, '16:05:00': 16, '16:10:00': 16, '16:15:00': 16.25, '16:20:00': 16.25, '16:25:00': 16.25, '16:30:00': 16.5, '16:35:00': 16.5, '16:40:00': 16.5, '16:45:00': 16.75, '16:50:00': 16.75, '16:55:00': 16.75, '17:00:00': 17, '17:05:00': 17, '17:10:00': 17, '17:15:00': 17.25, '17:20:00': 17.25, '17:25:00': 17.25, '17:30:00': 17.5, '17:35:00': 17.5, '17:40:00': 17.5, '17:45:00': 17.75, '17:50:00': 17.75, '17:55:00': 17.75, '18:00:00': 18,
                       '18:05:00': 18, '18:10:00': 18, '18:15:00': 18.25, '18:20:00': 18.25, '18:25:00': 18.25, '18:30:00': 18.5, '18:35:00': 18.5, '18:40:00': 18.5, '18:45:00': 18.75, '18:50:00': 18.75, '18:55:00': 18.75, '19:00:00': 19, '19:05:00': 19, '19:10:00': 19, '19:15:00': 19.25, '19:20:00': 19.25, '19:25:00': 19.25, '19:30:00': 19.5, '19:35:00': 19.5, '19:40:00': 19.5, '19:45:00': 19.75, '19:50:00': 19.75, '19:55:00': 19.75, '20:00:00': 20, '20:05:00': 20, '20:10:00': 20, '20:15:00': 20.25, '20:20:00': 20.25, '20:25:00': 20.25, '20:30:00': 20.5, '20:35:00': 20.5, '20:40:00': 20.5, '20:45:00': 20.75, '20:50:00': 20.75, '20:55:00': 20.75, '21:00:00': 21, '21:05:00': 21, '21:10:00': 21, '21:15:00': 21.25, '21:20:00': 21.25, '21:25:00': 21.25, '21:30:00': 21.5, '21:35:00': 21.5, '21:40:00': 21.5, '21:45:00': 21.75, '21:50:00': 21.75, '21:55:00': 21.75, '22:00:00': 22, '22:05:00': 22, '22:10:00': 22, '22:15:00': 22.25, '22:20:00': 22.25, '22:25:00': 22.25, '22:30:00': 22.5, '22:35:00': 22.5, '22:40:00': 22.5, '22:45:00': 22.75, '22:50:00': 22.75, '22:55:00': 22.75, '23:00:00': 23, '23:05:00': 23, '23:10:00': 23, '23:15:00': 23.25, '23:20:00': 23.25, '23:25:00': 23.25, '23:30:00': 23.5, '23:35:00': 23.5, '23:40:00': 23.5, '23:45:00': 23.75, '23:50:00': 23.75, '23:55:00': 23.75, '24:00:00': 24, '24:05:00': 24, '24:10:00': 24, '24:15:00': 24.25, '24:20:00': 24.25, '24:25:00': 24.25, '24:30:00': 24.5, '24:35:00': 24.5, '24:40:00': 24.5, '24:45:00': 24.75, '24:50:00': 24.75, '24:55:00': 24.75, '25:00:00': 25, '25:05:00': 25, '25:10:00': 25, '25:15:00': 25.25, '25:20:00': 25.25, '25:25:00': 25.25, '25:30:00': 25.5, '25:35:00': 25.5, '25:40:00': 25.5, '25:45:00': 25.75, '25:50:00': 25.75, '25:55:00': 25.75, '26:00:00': 26, '26:05:00': 26, '26:10:00': 26, '26:15:00': 26.25, '26:20:00': 26.25, '26:25:00': 26.25, '26:30:00': 26.5, '26:35:00': 26.5, '26:40:00': 26.5, '26:45:00': 26.75, '26:50:00': 26.75, '26:55:00': 26.75, '27:00:00': 27, '27:05:00': 27, '27:10:00': 27, '27:15:00': 27.25, '27:20:00': 27.25, '27:25:00': 27.25, '27:30:00': 27.5, '27:35:00': 27.5, '27:40:00': 27.5, '27:45:00': 27.75, '27:50:00': 27.75, '27:55:00': 27.75, '28:00:00': 28, '28:05:00': 28, '28:10:00': 28, '28:15:00': 28.25, '28:20:00': 28.25, '28:25:00': 28.25, '28:30:00': 28.5, '28:35:00': 28.5, '28:40:00': 28.5, '28:45:00': 28.75, '28:50:00': 28.75, '28:55:00': 28.75, '29:00:00': 29, '29:05:00': 29, '29:10:00': 29, '29:15:00': 29.25, '29:20:00': 29.25, '29:25:00': 29.25, '29:30:00': 29.5, '29:35:00': 29.5, '29:40:00': 29.5, '29:45:00': 29.75, '29:50:00': 29.75, '29:55:00': 29.75}
    # data_hora deve ser de 5 em 5 min
    data_format = "%Y-%m-%dT%H:%M"
    data_convertido = datetime.strptime(data_hora, data_format)

    hora = data_convertido.hour

    if hora < 6:
        hora = hora + 24
        data_convertido = data_convertido - timedelta(days=1)

    minuto = data_convertido.minute

    if minuto == 0:
        minuto = "00"

    dia = data_convertido.day
    ano = data_convertido.year
    mes = data_convertido.month
    dia_semana = data_convertido.weekday()

    hora_inicio = f"{hora}:{minuto}:00"

    hora_inicio = dicionario_hora[hora_inicio]

    categoria_nome = "Categoria_" + categoria
    category_map[categoria_nome] = 1

    current_x = [hora_inicio, dia_semana, mes, dia, feriado]

    for i in category_map.values():
        current_x.append(i)
    return current_x
