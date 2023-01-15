from window_buy import *

def window():

    def findFLights():
        global indexes
        indexes = []

        box_select_Select_Destinations['state'] = 'normal'
        box_select_Select_Destinations.delete(0, END)

        flight_name = text_Select_Destination.get('1.0', 'end-1c')
        found_flights, indexes = find_Flights(flight_name)

        check_Flag = check_For_Value(found_flights)
        if check_Flag == False:
            text_Select_Destination.delete('1.0', 'end')
            btn_Buy['state'] = 'disabled'
            text_Select_Destination.insert('1.0', "Введите город для поиска рейсов")
        else:
            flight_sorted = []
            for item in found_flights:
                if item[1] == True:
                    flight_sorted.append(item)
            btn_Buy['state'] = 'normal'
            flight_sorted, indexes = sort(flight_sorted, indexes)
            for item in flight_sorted:
                box_select_Select_Destinations.insert('end', item[0],)

    def showAll():
        print(DataBase)
        global indexes
        indexes = []

        box_select_Select_Destinations['state'] = 'normal'
        box_select_Select_Destinations.delete(0, END)
        found_flights, indexes = find_Flights('')

        btn_Buy['state'] = 'normal'
        for item in found_flights:
            box_select_Select_Destinations.insert('end', item[0])

    def Buy():
        try:
            select_data_index = indexes[box_select_Select_Destinations.curselection()[0]]
            window_for_buy(select_data_index)
        except IndexError as err:
            mb.showerror(title="Ошибка", message="Сначала выберите рейс для оформления билетов")

    def on_Closing():
        data_Rewrite()
        root.destroy()

    root = Tk()

    root.title("Курсовая работа. Выполнил: Азиз")
    root.geometry('1400x800')
    root.configure(background='#D3D3D3')

    #Найти рейс (кнопка + поле)
    Label(root, text="Введите пункт назначения:", font='Inter 15 bold', bg='#A66BFF', ).place(x=20, y=30)

    text_Select_Destination = Text(root, fg='white', font='Inter 15', bg='#7B68EE', width=38, height=1,
                                  padx=10, pady=10, )
    text_Select_Destination.place(x = 250, y = 20)

    box_select_Select_Destinations = Listbox(root, width=110, height=15, bg='#7B68EE', borderwidth=0, font='Inter 15',
                                  fg='white', state = 'disabled')
    box_select_Select_Destinations.place(x=20, y=100)

    btn_Select_Destination = Button(root, text="Найти рейсы", fg='white', font='Inter 15', bg='#1E90FF', width=20,
                          height=2, command = findFLights)
    btn_Select_Destination.place(x=1150, y=20)

    #Кнопка показа всех рейсов
    btn_Show_All = Button(root, text="Показать все рейсы", fg='white', font='Inter 15', bg='#1E90FF', width=20,
                          height=2, command = showAll)
    btn_Show_All.place(x=1150, y=100)

    #Кнопка оформленика покупки билетов
    btn_Buy = Button(root, text="Оформить билеты", fg='white', font='Inter 15', bg='#1E90FF', width=20,
                          height=2, state = 'disabled', command = Buy)
    btn_Buy.place(x=1150, y=180)



    root.protocol("WM_DELETE_WINDOW", on_Closing)
    root.mainloop()