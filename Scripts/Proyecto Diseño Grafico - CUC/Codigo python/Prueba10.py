
resultado_final = [
    [
        {'Capa': 'Cotas', 'Cotas': [{'Identificador': '2EF', 'Valor Cota': 8.0, 'Puntos': '[(10.0, 25.0), (18.0, 25.0)]'},
                                     {'Identificador': '311', 'Valor Cota': 15.0, 'Puntos': '[(10.0, 25.0), (10.0, 10.0)]'},
                                     {'Identificador': '329', 'Valor Cota': 6.48, 'Puntos': '[(14.05, 10.15), (14.05, 16.63)]'},
                                     {'Identificador': '34A', 'Valor Cota': 3.9, 'Puntos': '[(10.15, 17.55), (14.05, 17.55)]'},
                                     {'Identificador': '362', 'Valor Cota': 6.33, 'Puntos': '[(14.05, 18.52), (14.05, 24.85)]'},
                                     {'Identificador': '383', 'Valor Cota': 2.9, 'Puntos': '[(14.95, 21.12), (17.85, 21.12)]'},
                                     {'Identificador': '3C0', 'Valor Cota': 6.6, 'Puntos': '[(18.0, 10.0), (18.0, 16.6)]'},
                                     {'Identificador': '3F0', 'Valor Cota': 7.5, 'Puntos': '[(18.0, 17.5), (18.0, 25.0)]'},
                                     {'Identificador': '44B', 'Valor Cota': 8.0, 'Puntos': '[(10.0, 10.0), (18.0, 10.0)]'}]},
    ],
    [
        {'Capa': 'Muro 15cm', 'Coordenadas': ['(18.0, 17.5)', '(18.0, 25.0)', '(10.0, 25.0)', '(10.0, 10.0)', '(18.0, 10.0)', '(18.0, 16.6)', '(17.85, 16.6)', '(17.85, 10.15)', '(10.15, 10.15)', '(10.15, 24.85)', '(17.85, 24.85)', '(17.85, 17.5)']},
    ],
    [
        {'Capa': 'Muro 10cm', 'Coordenadas': ['(13.95, 10.15)', '(14.05, 10.15)', '(14.05, 16.63)', '(13.95, 16.63)', '(13.95, 24.85)', '(14.05, 24.85)', '(14.05, 18.52)', '(13.95, 18.52)', '(14.05, 17.55)', '(14.05, 17.45)', '(10.15, 17.45)', '(10.15, 17.55)', '(14.95, 21.12)', '(14.95, 21.23)', '(17.85, 21.23)', '(17.85, 21.12)']},
    ]
]

for capa_resultados in resultado_final:
    for capa_seleccionada in capa_resultados:
        if capa_seleccionada['Capa'] == 'Cotas':
            for cota in capa_seleccionada['Cotas']:
                Identificador = cota['Identificador']
                LongitudCota = cota['Valor Cota']
                puntos = cota['Puntos']
                coordenadas_cota  = eval(puntos)
                (P1X1, P1Y1), (P2X2, P2Y2) = coordenadas_cota 
                for capa_verificar in resultado_final: 
                    for capa in capa_verificar:
                        if capa['Capa'] != 'Cotas':
                            nombre_capa = capa['Capa']
                            for coordenada1_capa in capa['Coordenadas']:
                                coordenada1_capa = eval(coordenada1_capa)
                                (C1X1, C1Y1) = coordenada1_capa
                                if C1X1 == P1X1 and C1Y1 ==P1Y1:
                                    for coordenada2_capa in capa['Coordenadas']:
                                        coordenada2_capa = eval(coordenada2_capa)
                                        (C2X2, C2Y2) = coordenada2_capa
                                        if C2X2 == P2X2 and C2Y2 == P2Y2:
                                            print(f"Capa: {nombre_capa}")
                                            print(f"Longitud de Cotas: {LongitudCota}")
                                            print(f"Se encontro conincidencia en el punto:{coordenadas_cota}\n las coordenas son: {coordenada1_capa} & {coordenada2_capa}")

