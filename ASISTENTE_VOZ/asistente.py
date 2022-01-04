import speech_recognition as sr

def asistente_personal():

    sr.Microphone(device_index = 0)

    reconocimiento = sr.Recognizer()

    reconocimiento.energy_threshold=1000
    reconocimiento.dynamic_energy_threshold = False

    with sr.Microphone() as source:

        print('Mi nombre es Siri, ¿Cómo puedo ayudarte hoy?:')
        reconocimiento.adjust_for_ambient_noise(source)
        audio = reconocimiento.listen(source)
        try:
            texto = reconocimiento.recognize_google(audio, language='es-EC')#en-US
            print(f"Acabas de decir: {texto}")
            print(type(texto))
            dividir=texto.split()
            print(dividir)
            print(type(dividir))
        except sr.UnknownValueError as msg:
            print(msg)
        except LookupError:
            print("Lo siento mucho, no se pudo procesar tu solicitud.")
        else:
            encendido = ['enciende', 'television']
            apagado = ['apaga', 'television']
            if any (palabra in dividir for palabra in encendido):
                print("Encendiendo la television")
            else:
                if any (palabra in dividir for palabra in apagado):
                    print("Apagando la television")
                else:
                    print("No puedo aplicar esa configuracion a television ")
            
asistente_personal()
