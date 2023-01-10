import pandas as pd #импорт библиотеки Пандас
bookings_df=pd.read_csv("bookings.csv", encoding="windows-1251",sep=";")# чтение csv файла, указание кодировки файла, разделитель.
print(bookings_df.head(7))# вывод первых 7-ми строк
print((bookings_df.shape))# вывод кол-во строк и столбцов в файле

bookings_df=bookings_df.rename(columns={'Hotel':"hotel",'Is Canceled':"is_canceled", 'Lead Time':"lead_time",
'arrival full date':"arrival_full_date", 'Arrival Date Year':"arrival_date_year",
'Arrival Date Month':"arrival_date_month", 'Arrival Date Week Number':"arrival_date_week_number",
'Arrival Date Day of Month':"arrival_date_day_of_month", 'Stays in Weekend nights':"stays_in_weekend_nights",
'Stays in week nights':"stays_in_week_nights", 'stays total nights':"stays_total_nights",
'Adults':"adults", 'Children':"children", 'Babies':"babies", 'Meal':"meal", 'Country':"country",
'Reserved Room Type':"reserved_room_type", 'Assigned room type':"assigned_room_type", 'customer type':"customer_type",
'Reservation Status':"reservation_status", 'Reservation status_date':"reservation_status_date"})# переименование заголовков столбцов.

country_top=bookings_df.query("is_canceled==0")\
    .groupby(["country"])\
    .aggregate({"is_canceled":"count"})\
    .sort_values("is_canceled",ascending=False)# вывод стран с наибольшим кол-во успешных боринований ("0")# query-условие, комбинация groupby и aggregate для обощения данных.
print(country_top.head())# вывод топ 5 стран

night_res=bookings_df.groupby(["hotel"],as_index=False).aggregate({"stays_total_nights":"mean"}).sort_values("hotel")# вывод среднего кол-во ночей, на которые бронируют отели разных типов

true_number=bookings_df\
    .query("assigned_room_type!=reserved_room_type")\
    .groupby(["reserved_room_type"],as_index=False)\
    .aggregate({"assigned_room_type":"count"})\
    .sort_values("reserved_room_type",ascending=False)\
    .sum() #вывод кол-ва несовпадений номеров в столбцах assigned_room_type и reserved_room_type

month_top=bookings_df\
    .groupby(["arrival_date_year", "arrival_date_month"])\
    .aggregate({"is_canceled":"sum"})\
    .sort_values("arrival_date_year", ascending=False)# вывод кол-ва бронирований на каждый месяц за 3 года.

month_top=bookings_df\
    .query("is_canceled==1")\
    .groupby(["arrival_date_year", "arrival_date_month", "hotel"])\
    .aggregate({"is_canceled":"count"})\
    .sort_values("hotel", ascending=False)# вывод кол-ва бронирований на каждый месяц и кажды вид отеля за 3 года.

bookings_df["total_kids"]=bookings_df.children+bookings_df.babies #добавление нового столбца с объединением уже существующих
kids_m=bookings_df.groupby(["hotel"],as_index=False)\
    .aggregate({"total_kids":"mean"})\
    .sort_values("hotel")# среднее значение по столбцу total_kids для видов отелей

churn_rate_no_kids=round(bookings_df.query("is_canceled==1 and has_kids==False").shape[0]/bookings_df\
    .query("has_kids==False").shape[0]*100,2)# % отменивших поездку без детей
churn_rate_has_kids=round(bookings_df.query("is_canceled==1 and has_kids==True").shape[0]/bookings_df\
    .query("has_kids==True").shape[0]*100,2)# % отменивших поездку с детьми



















































