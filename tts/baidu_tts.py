from aip import AipSpeech
import os



def text2audio(textlist):
    """ 你的 APPID AK SK """
    APP_ID = '17522858'
    API_KEY = "DRDzSY7HEcGXG3KKccb05sIA"
    SECRET_KEY = "mounL0borhSLGVjMqFoYdxCUlETyo5zQ"

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


    for i in range(len(textlist)):
        filename = textlist[i]
        print(filename)
        result = client.synthesis(textlist[i])

        if not isinstance(result, dict):
            with open('./audio/'+filename+".mp3", 'wb') as f:
                f.write(result)
    return True

if __name__ == "__main__":
    text2audio('北京')