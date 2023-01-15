from tkinter import *
from tkinter import messagebox as mb
from models import *

def window_for_buy(index):

    def make_Order():
        client_Name = text_Client_Name.get('1.0', 'end-1c')
        client_Phone = text_Client_Phone.get('1.0', 'end-1c')
        client_Email = text_Client_Email.get('1.0', 'end-1c')
        client_Quantity = text_Client_Quantity.get('1.0', 'end-1c')

        try:
            client_Phone = int(client_Phone)
            client_Quantity = int(client_Quantity)
        except ValueError as err:
            text_Client_Phone.delete('1.0', 'end')
            text_Client_Quantity.delete('1.0', 'end')
            mb.showerror(title="Ошибка", message="Поля номера телефона и количества билетов заполните цифрами")

        client_Data = {"name": client_Name, "phone": client_Phone, "email": client_Email,
                       "flight_number": DataBase['flights'][index]['number'],
                       "destination": DataBase['flights'][index]['destination'],
                       "quantity": client_Quantity,
                       "departure_time": DataBase['flights'][index]['departure_time'],
                       "flight_days": DataBase['flights'][index]['flight_days'],
                       "stopover_points": DataBase['flights'][index]['stopover_points'],
                       }

        for value in client_Data.values():
            if value == '':
                tkinter.messagebox.showerror(title=None, message='Заполните все поля',)
                break

        if client_Quantity > int(DataBase['flights'][index]['free_seats']):
            mb.showerror(title="Ошибка", message="Количество билетов в заказе не может превышать общее"
                                                 "количество доступных билетов")

        else:
            DataBase['flights'][index]['free_seats'] -= client_Quantity

            ticket_Text = 'Чек от заказа билетов на рейс № {0} на имя {1}(номер телефона: {2}, e-mail: {3})' \
                         ' в количестве {4}. Пункт назначения - {5}. Время отправления - {6}. Дни полета: ' \
                          '{7}. Полет с пересадками: {8}.'.format(client_Data['flight_number'],
                                                                       client_Data['name'],
                                                                       client_Data['phone'],
                                                                       client_Data['email'],
                                                                       client_Data['quantity'],
                                                                       client_Data['destination'],
                                                                       client_Data['departure_time'],
                                                                       client_Data['flight_days'],
                                                                       client_Data['stopover_points'],
                                                                  )
            check = open("Ticket.txt", "w")
            check.write(ticket_Text)
            check.close()
            window_buy.destroy()



    window_buy = Tk()
    window_buy.title("Оформление заказа")
    window_buy.geometry('750x350')
    window_buy.configure(background='#D3D3D3')

    Label(window_buy, text='Заказ на "' + DataBase['flights'][index]['number'] + '"',
          font='Inter 19 bold', bg='#A66BFF', ).place(x=270, y=20)

    Label(window_buy, text="ФИО заказчика", font='Inter 15 bold', bg='#A66BFF', ).place(x=20, y=100)
    Label(window_buy, text="Номер телефона", font='Inter 15 bold', bg='#A66BFF', ).place(x=380, y=100)

    text_Client_Name = Text(window_buy, fg='white', font='Inter 15', bg='#7B68EE', width=33, height=1, padx=10, pady=10, )
    text_Client_Name.place(x=20, y=130)

    text_Client_Phone = Text(window_buy, fg='white', font='Inter 15', bg='#7B68EE', width=33, height=1, padx=10,
                              pady=10, )
    text_Client_Phone.place(x=380, y=130)

    Label(window_buy, text="E-mail", font='Inter 15 bold', bg='#A66BFF', ).place(x=20, y=180)
    Label(window_buy, text="Количество билетов", font='Inter 15 bold', bg='#A66BFF', ).place(x=380, y=180)

    text_Client_Email = Text(window_buy, fg='white', font='Inter 15', bg='#7B68EE', width=33, height=1, padx=10,
                               pady=10, )
    text_Client_Email.place(x=20, y=210)

    text_Client_Quantity = Text(window_buy, fg='white', font='Inter 15', bg='#7B68EE', width=33, height=1, padx=10, pady=10, )
    text_Client_Quantity.place(x=380, y=210)

    btn_Place_Order = Button(window_buy, text="Оформить заказ", fg='white', font='Inter 15', bg='#1E90FF', width=20,
                                 height=2, command=make_Order)
    btn_Place_Order.place(x=260, y=270)

    window_buy.mainloop()