import pandas as pd
import os
import matplotlib.pyplot as plt

class PLOT():
    def __init__(self):

        self.FILE_PATH = "E:/VRF/DATA"
        self.TIME = "updated_time"

        #
        # self.FILE_NAME = "교육용 전기요금_봄가을_0301_0531_0901_1031"
        # self.SAVE_NAME = "Education-Spring, Autumn"

        # self.FILE_NAME = "교육용 전기요금_여름철_0601_0831"
        # self.SAVE_NAME = "Education-Summer"

        # self.FILE_NAME = "교육용_전기요금_겨울철_1101_0228"
        # self.SAVE_NAME = "Education-Winter"

        # self.FILE_NAME = "산업용 전기요금_봄가을_0301_0531_0901_1031"
        # self.SAVE_NAME = "General, Industry-Spring, Autumn"

        # self.FILE_NAME = "산업용 전기요금_여름철_0601_0831"
        # self.SAVE_NAME = "General, Industry-Summer"

        self.FILE_NAME = "산업용 전기요금_겨울철_1101_0228"
        self.SAVE_NAME = "General, Industry-Winter"

        df = pd.read_csv("{}/{}.csv".format(self.FILE_PATH, self.FILE_NAME), encoding='cp949', index_col=self.TIME)
        df.dropna(inplace=True)
        self.LinePlot(df=df)


    def LinePlot(self, df):
        plt.rcParams['font.family'] = 'Malgun Gothic'
        plt.rcParams['axes.unicode_minus'] = False

        fig = plt.figure(figsize=(20, 10))
        ax1 = fig.add_subplot(1, 1, 1)

        tt0 = df.index.tolist()
        tt = []
        for i in range(len(tt0)):
            k = str(tt0[i])[10:16]
            tt.append(k)

        plt.title("{}".format(self.SAVE_NAME), fontsize=50)

        for i in range(1, len(df.columns)):
            print(i)
            ax1.plot(tt, df[df.columns[i]].tolist(), linewidth='5', alpha=0.7, drawstyle='steps-post')

        # ax1.legend(fontsize=50, ncol=1, loc='upper left')

        self.gap = int(df.shape[0] * 0.25)

        ax1.set_xticks([tt[i] for i in range(len(tt)) if i % self.gap == 0 or tt[i] == tt[-1]])
        ax1.tick_params(axis="x", labelsize=50)
        ax1.tick_params(axis="y", labelsize=50)

        ax1.set_ylabel("Electricity \nprice (Won/kWh)".format(), fontsize=50)

        ax1.set_ylim([0, 250])

        ax1.autoscale(enable=True, axis='x', tight=True)

        ax1.grid(linewidth=4)
        plt.tight_layout()

        plt.savefig("{}/{}.png".format(self.FILE_PATH, self.SAVE_NAME))




    def creat_folder(self, directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print("Error : creating directory."+ directory)
if __name__ == '__main__':
    DMR = PLOT()