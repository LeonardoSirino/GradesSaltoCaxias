import matplotlib.pyplot as plt
import plotly.plotly as py
import math as m

file = open("DadosSaltoCaxias.txt", "r")
dados = file.readlines()


class ChannelData:
    def __init__(self, canal):
        self.canal = canal
        self.velocs = []
        self.freqs = []
        self.amps = []
        self.AmpMultiplier = 30
        self.MaxAmp = 30.0
        self.MaxVeloc = 3.5

    def AddData(self, data):
        freq = float(data[0].replace(",", "."))
        veloc = float(data[1].replace(",", "."))
        amp = data[2].replace(",", ".")
        amp = float(amp.replace("\n", ""))
        amp = min(amp, self.MaxAmp)
        amp = self.AmpMultiplier * amp

        if veloc < self.MaxVeloc:        

            self.freqs.append(freq)
            self.velocs.append(veloc)
            self.amps.append(amp)

    def __str__(self):
        return str(self.canal)

    def ShowData(self):
        print(self.canal)
        print("\n Velocidades")
        print(self.velocs)
        print("\n\n Frequências")
        print(self.freqs)
        print("\n\n Amplitudes")
        print(self.amps)
        print("\n\n ------------------------------------------ \n\n")

    def PlotData(self):
        plt.scatter(self.velocs, self.freqs, s=self.amps, alpha=0.4)

    def PlotSingle(self):
        plt.clf()
        plt.scatter(self.velocs, self.freqs, s=self.amps, alpha=0.4)
        plt.title(self.canal)
        plt.xlabel("Velocidade [m/s]")
        plt.ylabel("Frequência [Hz]")
        limits = [0, 3.5, 0, 120]
        plt.axis(limits)
        plt.show()


    def PlotLegend(self):
        return self.canal


Channels = []
for line in dados:
    data = line.split("\t")
    if "Canal" in data[0]:
        NewChannel = ChannelData(data[0])
        Channels.append(NewChannel)
    elif data[0] == "\n":
        pass
    else:
        NewChannel.AddData(data)

for channel in Channels:
    channel.PlotSingle()

legend = []
plt.clf
Graf = plt.figure()
for channel in Channels:
    channel.PlotData()
    #channel.ShowData()
    legend.append(channel.PlotLegend())


plt.legend(legend, loc = 2)
plt.title("Influência da velocidade na frequência e amplitude de vibração")
plt.xlabel("Velocidade [m/s]")
plt.ylabel("Frequência [Hz]")
#plot_url = py.plot_mpl(Graf, filename='SaltoCaxiasGeral')
plt.show()