designFile = "E:/STM_TOP_BOARD_GENERIC/PDNAnalyzer_Output/PCB2/odb.tgz"

powerNets = ["3V3"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("P1", "19"), ("P1", "18"), ("P1", "2") ],
"ground_pins": [ ("P1", "17"), ("P1", "3") ],
"voltage": 3.3,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("U1", "172"), ("U1", "171"), ("U1", "159"), ("U1", "149"), ("U1", "136"), ("U1", "127"), ("U1", "103"), ("U1", "91"), ("U1", "82"), ("U1", "72"), ("U1", "62"), ("U1", "49"), ("U1", "36"), ("U1", "23"), ("U1", "15"), ("U1", "6") ],
"ground_pins": [ ("U1", "158"), ("U1", "148"), ("U1", "135"), ("U1", "126"), ("U1", "113"), ("U1", "102"), ("U1", "90"), ("U1", "71"), ("U1", "61"), ("U1", "37"), ("U1", "22"), ("U1", "14") ],
"current": 0.0001,
"Rpin": 13714.2857142857,
}
,
{
"id": "2",
"type": "load",
"power_pins": [ ("U2", "49"), ("U2", "43"), ("U2", "27"), ("U2", "14"), ("U2", "9"), ("U2", "3"), ("U2", "1") ],
"ground_pins": [ ("U2", "54"), ("U2", "52"), ("U2", "46"), ("U2", "41"), ("U2", "28"), ("U2", "12"), ("U2", "6") ],
"current": 0.0001,
"Rpin": 7000,
}
,
{
"id": "3",
"type": "load",
"power_pins": [ ("U3", "8") ],
"ground_pins": [ ("U3", "4") ],
"current": 0.0001,
"Rpin": 1000,
}
]


voltage_regulators = []


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.8, 'Thickness': 1.27E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.05, 'Thickness': 8.89E-05},
        {'name': 'LAYER_1', 'Conductivity': 47000000, 'Thickness': 1.75E-05},
        {'name': 'SUBSTRATE-2', 'DielectricConstant': 4.6, 'Thickness': 0.000365},
        {'name': 'LAYER_3', 'Conductivity': 47000000, 'Thickness': 1.75E-05},
        {'name': 'SUBSTRATE-3', 'DielectricConstant': 4.25, 'Thickness': 0.00012954},
        {'name': 'LAYER_4', 'Conductivity': 47000000, 'Thickness': 1.75E-05},
        {'name': 'SUBSTRATE-4', 'DielectricConstant': 4.6, 'Thickness': 0.000365},
        {'name': 'LAYER_2', 'Conductivity': 47000000, 'Thickness': 1.75E-05},
        {'name': 'SUBSTRATE-5', 'DielectricConstant': 4.05, 'Thickness': 8.89E-05},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.8, 'Thickness': 1.27E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
