import PySimpleGUI as sg
import pandas as pd

sg.theme('DarkGreen4')
EXCEL_FILE = 'Pendaftaran.xlsx'

data_frame = pd.read_excel(EXCEL_FILE)

layout = [
    [sg.Text('Masukkan Data Kamu : ')],
    [sg.Text('Nama', size=(15, 1)), sg.InputText(key='NAMA')],
    [sg.Text('No. HP', size=(15, 1)), sg.InputText(key='No. HP')],
    [sg.Text('Alamat', size=(15, 1)), sg.Multiline(key='Alamat')],
    [sg.Text('Tanggal Lahir', size=(15, 1)), sg.InputText(key='Tanggal Lahir'),
     sg.CalendarButton('Kalender', target='Tanggal Lahir', format=('%d-%m-%Y'))],
    [sg.Text('Jenis Kelamin', size=(15, 1)), sg.Combo(['Pria', 'Wanita'], key='Jenis Kelamin')],
    [sg.Text('Hobi', size=(15, 1)),
     sg.Checkbox('Belajar', key='Belajar'),
     sg.Checkbox('Menonton', key='Menonton'),
     sg.Checkbox('Musik', key='Musik')],

    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]

window = sg.Window('Form Pendaftaran', layout)

def clear_input():
    for key in values:
        window[key]('')
    return None

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'EXIT':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        new_data = pd.DataFrame([values])
        data_frame = data_frame._append(new_data, ignore_index=True)
        data_frame.to_excel(EXCEL_FILE, index=False, sheet_name='Sheet1')
        sg.popup('Data Berhasil disimpan')
        clear_input()

window.close()
