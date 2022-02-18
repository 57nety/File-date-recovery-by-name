# импорт модулей
import os, re, time, datetime

# проверить ОС == Windows
from sys import platform
if platform == 'win32':
  from win32_setctime import setctime

def finder():
  # все файлы в текущей директории
  names = os.listdir(os.getcwd())
  # цикл по всем файлам
  for name in names:
    flag = 0
    date = 0
    # путь к текущему файлу
    fullname = os.path.join(os.getcwd(), name)
    if os.path.isfile(name):
      # если файл подходит под шаблон названия
      if (re.search('IMG|VID.\d{8}.*\.jpg|mp4', name)):
        if(name[0:6] == "InShot"):
          flag = 1
          if (name[7:15].isdigit()):
            m = int(name[11:13])
            if (1 <= m <= 12):
              # получить год, месяц и день из названия
              y = int(name[7:11])
              d = int(name[13:15])
              if (name[16:22].isdigit()):
                hour = int(name[16:18])
                minute = int(name[18:20])
                second = int(name[20:22])
                # создать дату и превратить ее в timestamp
                date = datetime.datetime(y, m, d, hour, minute, second).timestamp()
              else:
                date = datetime.datetime(y, m, d).timestamp()
        else:
          flag = 1
          if(name[4:12].isdigit()):
            m = int(name[8:10])
            if(1<=m<=12):
              # получить год, месяц и день из названия
              y = int(name[4:8])
              d = int(name[10:12])
              if(name[13:19].isdigit()):
                hour = int(name[13:15])
                minute = int(name[15:17])
                second = int(name[17:19])
                # создать дату и превратить ее в timestamp
                date = datetime.datetime(y, m, d, hour, minute, second).timestamp()
              else:
                date = datetime.datetime(y, m, d).timestamp()
      elif(re.search('PANO.\d{8}.*\.jpg', name)):
        flag = 1
        if (name[5:13].isdigit()):
          m = int(name[9:11])
          if (1 <= m <= 12):
            # получить год, месяц и день из названия
            y = int(name[5:9])
            d = int(name[11:13])
            if (name[14:20].isdigit()):
              hour = int(name[14:16])
              minute = int(name[16:18])
              second = int(name[18:20])
              # создать дату и превратить ее в timestamp
              date = datetime.datetime(y, m, d, hour, minute, second).timestamp()
            else:
              date = datetime.datetime(y, m, d).timestamp()
      elif(re.search('Screenshot.\d{4}.*\.home|whatsapp|jpg', name)):
        if(name[0:4] == "SAVE"):
          flag = 1
          if (name[5:13].isdigit()):
            m = int(name[9:11])
            if (1 <= m <= 12):
              # получить год, месяц и день из названия
              y = int(name[5:9])
              d = int(name[11:13])
              if (name[14:20].isdigit()):
                hour = int(name[14:16])
                minute = int(name[16:18])
                second = int(name[18:20])
                # создать дату и превратить ее в timestamp
                date = datetime.datetime(y, m, d, hour, minute, second).timestamp()
              else:
                date = datetime.datetime(y, m, d).timestamp()
        else:
          flag = 1
          y = int(name[11:15])
          m = int(name[16:18])
          d = int(name[19:21])
          hour = int(name[22:24])
          minute = int(name[25:27])
          second = int(name[28:30])
          # создать дату и превратить ее в timestamp
          date = datetime.datetime(y, m, d, hour, minute, second).timestamp()
      elif(re.search('Screenrecorder.\d{4}.*\.mp4', name)):
        flag = 1
        y = int(name[15:19])
        m = int(name[20:22])
        d = int(name[23:25])
        hour = int(name[26:28])
        minute = int(name[29:31])
        second = int(name[32:34])
        # создать дату и превратить ее в timestamp
        date = datetime.datetime(y, m, d, hour, minute, second).timestamp()
      elif(re.search('SAVE.\d{8}.*\.jpg', name)):
        flag = 1
        if (name[5:13].isdigit()):
          m = int(name[9:11])
          if (1 <= m <= 12):
            # получить год, месяц и день из названия
            y = int(name[5:9])
            d = int(name[11:13])
            if (name[14:20].isdigit()):
              hour = int(name[14:16])
              minute = int(name[16:18])
              second = int(name[18:20])
              # создать дату и превратить ее в timestamp
              date = datetime.datetime(y, m, d, hour, minute, second).timestamp()
            else:
              date = datetime.datetime(y, m, d).timestamp()
    print(flag)
    if(flag==1):
      # изменить дату изменения (но не создания)
      os.utime(fullname, times=(date, date))
      # если Windows
      if platform == 'win32':
        # изменить дату создания
        setctime(fullname, date)
        print(name)

# выполнить функцию
if __name__ == '__main__':
  finder()