import pandas as pd
import os

# Data for Page 6: Isolation Board V10 DB37 Female connector Pin Assignment
data_j1_j2 = [
    [1, 'O', 'X-Pulse(+)', 20, 'I', 'Z-ALM', 1, 'I', 'W-Pulse(+)', 20, 'O', 'DO2'],
    [2, 'O', 'X-Pulse(-)', 21, '', 'GND1', 2, 'I', 'W-Pulse(-)', 21, 'O', 'DO3'],
    [3, 'O', 'X-Dir(+)', 22, 'O', 'U-Pulse(+)', 3, 'I', 'W-Dir(+)', 22, 'O', 'DO4'],
    [4, 'O', 'X-Dir(-)', 23, 'O', 'U-Pulse(-)', 4, 'I', 'W-Dir(-)', 23, 'O', 'DO5'],
    [5, 'I', 'X-ORG', 24, 'O', 'U-Dir(+)', 5, 'I', 'W-ALM', 24, 'O', 'DO6'],
    [6, 'I', 'X-ALM', 25, 'O', 'U-Dir(-)', 6, 'I', 'W-ORG', 25, 'O', 'DO7'],
    [7, '', 'GND1', 26, 'I', 'U-ORG', 7, 'I', 'U-EL(+)', 26, 'O', 'DO8'],
    [8, 'O', 'Y-Pulse(+)', 27, 'I', 'U-ALM', 8, 'I', 'U-EL(-)', 27, 'O', '5V'],
    [9, 'O', 'Y-Pulse(-)', 28, '', 'GND1', 9, 'I', 'V-EL(+)', 28, '', 'GND1'],
    [10, 'O', 'Y-Dir(+)', 29, 'O', 'V-Pulse(+)', 10, 'I', 'V-EL(-)', 29, 'I', 'VCC2'],
    [11, 'O', 'Y-Dir(-)', 30, 'O', 'V-Pulse(-)', 11, 'I', 'DI1', 30, '', 'GND2'],
    [12, 'I', 'Y-ORG', 31, 'O', 'V-Dir(+)', 12, 'I', 'DI2', 31, 'I', 'VCC3'],
    [13, 'I', 'Y-ALM', 32, 'O', 'V-Dir(-)', 13, 'I', 'DI3', 32, '', 'GND3'],
    [14, '', 'GND1', 33, 'I', 'V-ORG', 14, 'I', 'DI4', 33, 'O', 'PWM'],
    [15, 'O', 'Z-Pulse(+)', 34, 'I', 'V-ALM', 15, 'I', 'DI5', 34, '', 'GND1'],
    [16, 'O', 'Z-Pulse(-)', 35, '', 'GND1', 16, 'I', 'DI6', 35, 'O', 'ANALOG'],
    [17, 'O', 'Z-Dir(+)', 36, 'O', '24V', 17, 'I', 'DI7', 36, '', 'GND1'],
    [18, 'O', 'Z-Dir(-)', 37, 'O', '5V', 18, 'I', 'DI8', 37, '', 'NC'],
    [19, 'I', 'Z-ORG', '', '', '', 19, 'O', 'DO1', '', '', '']
]
columns_j1_j2 = [
    'J1 Pin', 'J1 I/O', 'J1 Name', 'J1 Pin', 'J1 I/O', 'J1 Name',
    'J2 Pin', 'J2 I/O', 'J2 Function', 'J2 Pin', 'J2 I/O', 'J2 Function'
]
df_j1_j2 = pd.DataFrame(data_j1_j2, columns=columns_j1_j2)

# Page 6 Abbreviation Table
data_abbr = [
    ['Pulse', 'Clock output'],
    ['Dir', 'Direction output'],
    ['ORG', 'Origin signal or Home signal input'],
    ['ALM', 'Alaram signal input'],
    ['EL(+)', 'End limit Plus signal input'],
    ['EL(-)', 'End limit Minus signal input'],
    ['DI', 'General purpose digital input'],
    ['DO', 'General purpose digital output'],
    ['PWM', 'PWM Output'],
    ['ANALOG', 'Analog Output Voltage'],
    ['GND1', 'External power supply ground'],
    ['VCC2', 'External power supply require for Digital Output (5V to 24VDC)'],
    ['GND2', 'Ground for VCC2'],
    ['VCC3', 'External power supply require for End limit and digital input (5V to 24VDC)'],
    ['GND3', 'Ground for VCC3']
]
df_abbr = pd.DataFrame(data_abbr, columns=['Abbreviation', 'Description'])

# Page 7: Galvo Isolation Board V10 DB15 Female connector Pin Assignment
data_galvo = [
    [1, 'O', 'CLK (-)', 9, 'O', 'CLK (+)'],
    [2, 'O', 'SYNC(-)', 10, 'O', 'SYNC(+)'],
    [3, 'O', 'X (-)', 11, 'O', 'X (+)'],
    [4, 'O', 'Y (-)', 12, 'O', 'Y (+)'],
    [5, '', 'NC', 13, '', 'NC'],
    [6, '', 'NC', 14, '', 'NC'],
    [7, '', 'NC', 15, '', 'NC'],
    [8, '', 'NC', '', '', '']
]
columns_galvo = ['Pin No.', 'I/O', 'Name', 'Pin No.', 'I/O', 'Name']
df_galvo = pd.DataFrame(data_galvo, columns=columns_galvo)

output_file = r'd:\TeamDev\DLL_Galvo\Galvo_Scribing\Galvo_Studio - Copy\Galvo_info\ProSysV10_Pin_Assignments.xlsx'

with pd.ExcelWriter(output_file) as writer:
    df_j1_j2.to_excel(writer, sheet_name='Page 6 - J1 & J2', index=False)
    df_abbr.to_excel(writer, sheet_name='Page 6 - Abbreviations', index=False)
    df_galvo.to_excel(writer, sheet_name='Page 7 - Galvo DB15', index=False)

print(f"Created {output_file}")
