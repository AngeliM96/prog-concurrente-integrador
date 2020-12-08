import threading
import time
import logging
import random
import sys

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

cantidad_candidatos = 10
cantidad_maestros_jedi = 3
# Los niños que llegan para ser entrenados van a ser una lista
candidatos = []
# Y los que son aceptados se ponen en otra
padawans = []
# El monitor para sincronizar quien está enseñando
monitor_evaluacion = threading.Condition()
semaforo_entrenamiento = threading.Semaphore(1)

class Candidato(threading.Thread):
    def __init__(self, numero):
        super().__init__()
        self.name = f'Candidato {numero + 1}'
        self.midiclorianos = random.randint(2500, 25000)
        self.sentimientos_negativos = random.randint(1, 10)

    def interrumpirMeditacion(self):
        if(self.soyPrimero()):
            with monitor_evaluacion:
                logging.info('Interrumpo la meditación del Gran Maestro para ser evaluado')
                monitor_evaluacion.notify()
    def soyPrimero(self): 
        return candidatos.index(self) == 0
    def entrarAlTemplo(self):
        candidatos.append(self)
        logging.info('Llegué al templo')
        time.sleep(2)
        self.interrumpirMeditacion()

    # Condiciones
    def esNegativo(self):
        return self.sentimientos_negativos >= 6
    def esPotente(self):
        return self.midiclorianos >= 18000
    def esSensible(self):
        return self.midiclorianos >= 8000
    def puedeSerPadawan(self):
        return (self.esSensible() and not self.esNegativo()) or self.esPotente()  
    
    def run(self):
        self.entrarAlTemplo()


class GranMaestroJedi(threading.Thread):
    def __init__(self):
        super().__init__()
        self.name = 'Gran Maestro Jedi'
        self.candidatos_evaluados = 0
    
    def evaluarCandidatos(self):
        with monitor_evaluacion:
            while(self.noHayNadieParaEvaluar() and not self.todosFueronEvaluados()):
                logging.info('Voy a meditar')
                monitor_evaluacion.wait()
            self.juzgarCandidato(candidatos[0])
            self.candidatos_evaluados += 1

    def juzgarCandidato(self, candidato):
        if candidato.puedeSerPadawan():
            padawans.append(candidato)  
            candidatos.pop(0)
            time.sleep(2)
            logging.info(f'{candidato.name} fue aceptado como padawan.')
        elif candidato.esNegativo():
            candidatos.pop(0)
            time.sleep(2)
            logging.info(f'{candidato.name} fue rechazado por ser peligroso.')
        else:
            candidatos.pop(0)
            time.sleep(2)
            logging.info(f'{candidato.name} fue rechazado por no ser lo suficientemente sensible a la fuerza.')

    def noHayNadieParaEvaluar(self):
        return len(candidatos) == 0
    def todosFueronEvaluados(self):
        return self.candidatos_evaluados == cantidad_candidatos
    def run(self):
        while(not self.todosFueronEvaluados()):
            self.evaluarCandidatos()
        logging.info('Todos los candidatos fueron evaluados, me voy a retirar para que empiecen las clases.')
        for i in range(cantidad_maestros_jedi):
            MaestroJedi(i).start()


class MaestroJedi(threading.Thread):
    def __init__(self, numero):
        super().__init__()
        self.name = f'Maestro Jedi {numero + 1}'
        # Se elige aleatoriamente a cuantos padawans puede entrenar antes de retirarse
        self.cuantos_padawans = random.randint(1, 5)
        self.padawans_entrenados = 0
    
    def entrenarPadawan(self, padawan):
        padawans.pop(0)
        logging.info(f'Voy a entrenar al {padawan.name}.')
        time.sleep(2)
        logging.info(f'{padawan.name} ahora es un Caballero Jedi.')
        self.padawans_entrenados += 1

    def noHayNadieParaEntrenar(self):
        return len(padawans) == 0
    def llegueAMiCapacidad(self):
        return self.padawans_entrenados == self.cuantos_padawans

    def run(self):
        semaforo_entrenamiento.acquire()
        while True:
            if self.noHayNadieParaEntrenar():
                logging.info('Ya no hay nadie para entrenar.')
                time.sleep(2)
                sys.exit()
            else:
                self.entrenarPadawan(padawans[0])

GranMaestroJedi().start()

for i in range(cantidad_candidatos):
    Candidato(i).start()
