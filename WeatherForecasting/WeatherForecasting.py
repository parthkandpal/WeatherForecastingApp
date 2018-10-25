import requests
import time
import json
#Weather Forecast


def day1(**text):
    # Unix_date = text['list'][0]['dt']  # fetching date from list
    # date = time.ctime(Unix_date)

    # print(date)

    def day1part1(**text):


        quarter = text['list'][0]['dt_txt']  # 3hours with date


        temprature = round((text['list'][0]['main']['temp']) - 273,2)  # fetching temprature for first 3 hours


        temp_min = round((text['list'][0]['main']['temp_min']) - 273,2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][0]['main']['temp_max']) - 273,2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][0]['main']['humidity'])  # fetching humidity for this 3 hours


        # Weather

        main_weather = text['list'][0]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][0]['weather'][0]['description'])  # weather description for 3 hours


        #wind

        wind_speed= text['list'][0]['wind']['speed']

        print('''       
                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

        '''.format(quarter,temprature,temp_min,temp_max,humidity,main_weather,weather_description,wind_speed))



    def day1part2(**text):

        quarter = text['list'][1]['dt_txt']  # 3hours with date


        temprature = round((text['list'][1]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours


        temp_min = round((text['list'][1]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][1]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][1]['main']['humidity'])  # fetching humidity for this 3 hours


        # Weather

        main_weather = text['list'][1]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][1]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][1]['wind']['speed']

        print('''       
                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

            '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather, weather_description,
                       wind_speed))

    def day1part3(**text):
        quarter = text['list'][2]['dt_txt']  # 3hours with date


        temprature = round((text['list'][2]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours


        temp_min = round((text['list'][2]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][2]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][2]['main']['humidity'])  # fetching humidity for this 3 hours


        # Weather

        main_weather = text['list'][2]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][2]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][2]['wind']['speed']

        print('''       
                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                    '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather, weather_description,
                               wind_speed))

    def day1part4(**text):
        quarter = text['list'][3]['dt_txt']  # 3hours with date


        temprature = round((text['list'][3]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours


        temp_min = round((text['list'][3]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][3]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][3]['main']['humidity'])  # fetching humidity for this 3 hours


        # Weather

        main_weather = text['list'][3]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][3]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][3]['wind']['speed']

        print('''       
                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                    '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather, weather_description,
                               wind_speed))

    def day1part5(**text):
        quarter = text['list'][4]['dt_txt']  # 3hours with date


        temprature = round((text['list'][4]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours


        temp_min = round((text['list'][4]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][4]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][4]['main']['humidity'])  # fetching humidity for this 3 hours


        # Weather

        main_weather = text['list'][4]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][4]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][4]['wind']['speed']

        print('''   
                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                            '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather,
                                       weather_description,
                                       wind_speed))

    def day1part6(**text):
        quarter = text['list'][5]['dt_txt']  # 3hours with date


        temprature = round((text['list'][5]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours


        temp_min = round((text['list'][5]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][5]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][5]['main']['humidity'])  # fetching humidity for this 3 hours


        # Weather

        main_weather = text['list'][5]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][5]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][5]['wind']['speed']

        print('''       
                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                            '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather,
                                       weather_description,
                                       wind_speed))

    def day1part7(**text):
        quarter = text['list'][6]['dt_txt']  # 3hours with date


        temprature = round((text['list'][6]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours


        temp_min = round((text['list'][6]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][6]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][6]['main']['humidity'])  # fetching humidity for this 3 hours


        # Weather

        main_weather = text['list'][6]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][6]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][6]['wind']['speed']

        print('''       
                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                            '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather,
                                       weather_description,
                                       wind_speed))

    def day1part8(**text):
        quarter = text['list'][7]['dt_txt']  # 3hours with date


        temprature = round((text['list'][7]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours


        temp_min = round((text['list'][7]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][7]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][7]['main']['humidity'])  # fetching humidity for this 3 hours


        # Weather

        main_weather = text['list'][7]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][7]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][7]['wind']['speed']

        print('''
                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                            '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather,
                                       weather_description,
                                       wind_speed))

    day1part1(**text)
    day1part2(**text)
    day1part3(**text)
    day1part4(**text)
    day1part5(**text)
    day1part6(**text)
    day1part7(**text)
    day1part8(**text)





def day2(**text):
    # Unix_date = text['list'][1]['dt']  # fetching date from list
    # date = time.ctime(Unix_date)

    # print(date)

    def day2part1(**text):
        quarter = text['list'][2]['dt_txt']  # 3hours with date

        temprature = round((text['list'][8]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][8]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][8]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][8]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][8]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][8]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][8]['wind']['speed']

        print('''       

                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

            '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather, weather_description,
                       wind_speed))

    def day2part2(**text):
        quarter = text['list'][9]['dt_txt']  # 3hours with date

        temprature = round((text['list'][9]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][9]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][9]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][9]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][9]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][9]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][9]['wind']['speed']

        print('''       

                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather, weather_description,
                           wind_speed))

    def day2part3(**text):
        quarter = text['list'][10]['dt_txt']  # 3hours with date

        temprature = round((text['list'][10]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][10]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][10]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][10]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][10]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][10]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][10]['wind']['speed']

        print('''       

                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                        '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather, weather_description,
                                   wind_speed))

    def day2part4(**text):
        quarter = text['list'][11]['dt_txt']  # 3hours with date

        temprature = round((text['list'][11]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][11]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][11]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][11]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][11]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][11]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][11]['wind']['speed']

        print('''       

                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                        '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather, weather_description,
                                   wind_speed))

    def day2part5(**text):
        
        quarter = text['list'][12]['dt_txt']  # 3hours with date

        temprature = round((text['list'][12]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][12]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][12]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][12]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][12]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][12]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][12]['wind']['speed']

        print('''       
                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                                '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather,
                                           weather_description,
                                           wind_speed))

    def day2part6(**text):
        quarter = text['list'][13]['dt_txt']  # 3hours with date

        temprature = round((text['list'][13]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][13]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][13]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][13]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][13]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][13]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][13]['wind']['speed']

        print('''       
                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                                '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather,
                                           weather_description,
                                           wind_speed))

    def day2part7(**text):
        quarter = text['list'][14]['dt_txt']  # 3hours with date

        temprature = round((text['list'][14]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][14]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][14]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][14]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][14]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][14]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][14]['wind']['speed']

        print('''       

                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                                '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather,
                                           weather_description,
                                           wind_speed))

    def day2part8(**text):
        quarter = text['list'][15]['dt_txt']  # 3hours with date


        temprature = round((text['list'][15]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours


        temp_min = round((text['list'][15]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][15]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][15]['main']['humidity'])  # fetching humidity for this 3 hours


        # Weather

        main_weather = text['list'][15]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][15]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][15]['wind']['speed']

        print('''       

                         ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                                '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather,
                                           weather_description,
                                           wind_speed))

    day2part1(**text)
    day2part2(**text)
    day2part3(**text)
    day2part4(**text)
    day2part5(**text)
    day2part6(**text)
    day2part7(**text)
    day2part8(**text)


def day3(**text):
    # Unix_date = text['list'][2]['dt']  # fetching date from list
    # date = time.ctime(Unix_date)
    #
    # print(date)

    def day3part1(**text):
        quarter = text['list'][3]['dt_txt']  # 3hours with date

        temprature = round((text['list'][16]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][16]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][16]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][16]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][16]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][16]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][16]['wind']['speed']

        print('''       

                                {}

            Temprature=  {}

            Minimum temprature =  {}

            Maximum temprature=    {}

            Humidity = {}

            Weather = {} , {} 


            Wind Speed = {}

            '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather, weather_description,
                       wind_speed))

    def day3part2(**text):
        quarter = text['list'][17]['dt_txt']  # 3hours with date

        temprature = round((text['list'][17]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][17]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][17]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][17]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][17]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][17]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][17]['wind']['speed']

        print('''       

                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather, weather_description,
                           wind_speed))

    def day3part3(**text):
        quarter = text['list'][18]['dt_txt']  # 3hours with date

        temprature = round((text['list'][18]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][18]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][18]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][18]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][18]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][18]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][18]['wind']['speed']

        print('''       

                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                        '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather, weather_description,
                                   wind_speed))

    def day3part4(**text):
        quarter = text['list'][19]['dt_txt']  # 3hours with date

        temprature = round((text['list'][19]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][19]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][19]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][19]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][19]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][19]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][19]['wind']['speed']

        print('''       
                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                        '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather, weather_description,
                                   wind_speed))

    def day3part5(**text):
        quarter = text['list'][20]['dt_txt']  # 3hours with date

        temprature = round((text['list'][20]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][20]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][20]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][20]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][20]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][20]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][20]['wind']['speed']

        print('''       

                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                                '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather,
                                           weather_description,
                                           wind_speed))

    def day3part6(**text):
        quarter = text['list'][21]['dt_txt']  # 3hours with date

        temprature = round((text['list'][21]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][21]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][21]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][21]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][21]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][21]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][21]['wind']['speed']

        print('''       

                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                                '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather,
                                           weather_description,
                                           wind_speed))

    def day3part7(**text):
        quarter = text['list'][22]['dt_txt']  # 3hours with date

        temprature = round((text['list'][22]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][22]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][22]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][22]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][22]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][22]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][22]['wind']['speed']

        print('''       

                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                                '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather,
                                           weather_description,
                                           wind_speed))

    def day3part8(**text):
        quarter = text['list'][23]['dt_txt']  # 3hours with date


        temprature = round((text['list'][23]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours


        temp_min = round((text['list'][23]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][23]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][23]['main']['humidity'])  # fetching humidity for this 3 hours


        # Weather

        main_weather = text['list'][23]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][23]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][23]['wind']['speed']

        print('''       

                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    
   

                                '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather,
                                           weather_description,
                                           wind_speed))

    day3part1(**text)
    day3part2(**text)
    day3part3(**text)
    day3part4(**text)
    day3part5(**text)
    day3part6(**text)
    day3part7(**text)
    day3part8(**text)




def day4(**text):
    # Unix_date = text['list'][2]['dt']  # fetching date from list
    # date = time.ctime(Unix_date)

    # print(date)

    def day4part1(**text):
        quarter = text['list'][4]['dt_txt']  # 3hours with date

        temprature = round((text['list'][24]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][24]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][24]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][24]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][24]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][24]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][24]['wind']['speed']

        print('''       

                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    


            '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather, weather_description,
                       wind_speed))

    def day4part2(**text):
        quarter = text['list'][25]['dt_txt']  # 3hours with date

        temprature = round((text['list'][25]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][25]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][25]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][25]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][25]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][25]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][25]['wind']['speed']

        print('''       

                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather, weather_description,
                           wind_speed))

    def day4part3(**text):
        quarter = text['list'][26]['dt_txt']  # 3hours with date

        temprature = round((text['list'][26]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][26]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][26]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][26]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][26]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][26]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][26]['wind']['speed']

        print('''       

                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                        '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather, weather_description,
                                   wind_speed))

    def day4part4(**text):
        quarter = text['list'][27]['dt_txt']  # 3hours with date

        temprature = round((text['list'][27]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][27]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][27]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][27]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][27]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][27]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][27]['wind']['speed']

        print('''       

                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                        '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather, weather_description,
                                   wind_speed))

    def day4part5(**text):
        quarter = text['list'][28]['dt_txt']  # 3hours with date

        temprature = round((text['list'][28]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][28]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][28]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][28]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][28]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][28]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][28]['wind']['speed']

        print('''       

                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                                '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather,
                                           weather_description,
                                           wind_speed))

    def day4part6(**text):
        quarter = text['list'][29]['dt_txt']  # 3hours with date

        temprature = round((text['list'][29]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][29]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][29]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][29]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][29]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][29]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][29]['wind']['speed']

        print('''       
                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    


                                '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather,
                                           weather_description,
                                           wind_speed))

    def day4part7(**text):
        quarter = text['list'][30]['dt_txt']  # 3hours with date

        temprature = round((text['list'][30]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][30]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][30]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][30]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][30]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][30]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][30]['wind']['speed']

        print('''       
                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                                '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather,
                                           weather_description,
                                           wind_speed))

    def day4part8(**text):
        quarter = text['list'][31]['dt_txt']  # 3hours with date


        temprature = round((text['list'][31]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours


        temp_min = round((text['list'][31]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][31]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][31]['main']['humidity'])  # fetching humidity for this 3 hours


        # Weather

        main_weather = text['list'][31]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][31]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][31]['wind']['speed']

        print('''       
                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                                '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather,
                                           weather_description,
                                           wind_speed))

    day4part1(**text)
    day4part2(**text)
    day4part3(**text)
    day4part4(**text)
    day4part5(**text)
    day4part6(**text)
    day4part7(**text)
    day4part8(**text)


def day5(**text):
    # Unix_date = text['list'][2]['dt']  # fetching date from list
    # date = time.ctime(Unix_date)
    #
    # print(date)

    def day5part1(**text):
        quarter = text['list'][4]['dt_txt']  # 3hours with date

        temprature = round((text['list'][32]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][32]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][32]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][32]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][32]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][32]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][32]['wind']['speed']

        print('''       
                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    


            '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather, weather_description,
                       wind_speed))

    def day5part2(**text):
        quarter = text['list'][33]['dt_txt']  # 3hours with date

        temprature = round((text['list'][33]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][33]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][33]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][33]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][33]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][33]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][33]['wind']['speed']

        print('''       
                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather, weather_description,
                           wind_speed))

    def day5part3(**text):
        quarter = text['list'][34]['dt_txt']  # 3hours with date

        temprature = round((text['list'][34]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][34]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][34]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][34]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][34]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][34]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][34]['wind']['speed']

        print('''       
                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                        '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather, weather_description,
                                   wind_speed))

    def day5part4(**text):
        quarter = text['list'][35]['dt_txt']  # 3hours with date

        temprature = round((text['list'][35]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][35]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][35]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][35]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][35]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][35]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][35]['wind']['speed']

        print('''       
                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                        '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather, weather_description,
                                   wind_speed))

    def day5part5(**text):
        quarter = text['list'][36]['dt_txt']  # 3hours with date

        temprature = round((text['list'][36]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][36]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][36]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][36]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][36]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][36]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][36]['wind']['speed']

        print('''       
                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                                '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather,
                                           weather_description,
                                           wind_speed))

    def day5part6(**text):
        quarter = text['list'][37]['dt_txt']  # 3hours with date

        temprature = round((text['list'][37]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][37]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][37]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][37]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][37]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][37]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][37]['wind']['speed']

        print('''       
                    
                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                                '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather,
                                           weather_description,
                                           wind_speed))

    def day5part7(**text):
        quarter = text['list'][38]['dt_txt']  # 3hours with date

        temprature = round((text['list'][38]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours

        temp_min = round((text['list'][38]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][38]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][38]['main']['humidity'])  # fetching humidity for this 3 hours

        # Weather

        main_weather = text['list'][38]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][38]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][38]['wind']['speed']

        print('''
                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    
                                                    
                                '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather,
                                           weather_description,
                                           wind_speed))


    def day5part8(**text):
        quarter = text['list'][39]['dt_txt']  # 3hours with date
        

        temprature = round((text['list'][39]['main']['temp']) - 273, 2)  # fetching temprature for first 3 hours
        

        temp_min = round((text['list'][39]['main']['temp_min']) - 273, 2)  # fetching min temprature for this 3 hours

        temp_max = round((text['list'][39]['main']['temp_max']) - 273, 2)  # fetching max temprature for this 3 hours

        humidity = (text['list'][39]['main']['humidity'])  # fetching humidity for this 3 hours
        

        # Weather

        main_weather = text['list'][39]['weather'][0]['main']  # main weather for these three hours

        weather_description = (text['list'][39]['weather'][0]['description'])  # weather description for 3 hours

        # wind

        wind_speed = text['list'][39]['wind']['speed']

        print('''       
                        ----------------------------------{}----------------------------------

                                Temprature=  {} degree celsius

                                Minimum temprature =  {}    degree celsius

                                Maximum temprature=    {}   degree celsius

                                Humidity = {}

                                Weather = {} , {} 


                                Wind Speed = {}    

                                '''.format(quarter, temprature, temp_min, temp_max, humidity, main_weather,
                                           weather_description,
                                           wind_speed))


    day5part1(**text)
    day5part2(**text)
    day5part3(**text)
    day5part4(**text)
    day5part5(**text)
    day5part6(**text)
    day5part7(**text)
    day5part8(**text)


