import matplotlib.pyplot as plt

class Plotter:

    @staticmethod
    def plotAlpha(df, title, ylim=None):
        fig = plt.figure(figsize=(15,8))
        for c in df.columns:
            plt.plot(df[c], label=f"k = {c}")
        plt.legend()
        plt.title(title)
        plt.xlabel("r")
        plt.grid()
        plt.ylabel("Alpha(r)")
        if ylim is not None:
            plt.ylim(0,ylim)
        plt.savefig(f'./imgs/{title}')
        plt.show()


    @staticmethod
    def plotBeta(df, title, ylim1=None, ylim2 = None):
        fig = plt.figure(figsize=(15,8))
        plt.plot(df, label=f"m", marker='o')
        plt.title(title)
        plt.xlabel("m")
        plt.grid()
        if ylim1 is not None:
            plt.ylim(ylim1, ylim2)
        plt.ylabel("Beta(m,0)")
        plt.savefig(f'./imgs/{title}')
        plt.show()

    @staticmethod
    def subplotAlphaBeta(alpha, beta, title, alpha_ylim0=None, alpha_ylim1=None, beta_ylim0=None, beta_ylim1=None):
        fig, axs = plt.subplots(1,2, figsize=(18,7))
        for c in alpha.columns:
            axs[0].plot(alpha[c], label=f"k = {c}")
        
        axs[0].legend()
        axs[0].set_title('Alpha(r) vs r')
        axs[0].set_xlabel("r")
        axs[0].grid()
        axs[0].set_ylabel("Alpha(r)")
        if alpha_ylim0 is not None:
            axs[0].set_ylim(alpha_ylim0, alpha_ylim1)

        axs[1].plot(beta.index, beta.values, label=f"m", marker='^', linestyle='--')
        axs[1].set_title('Beta(m, 0) vs m')
        axs[1].set_xlabel("m")
        axs[1].grid()

        if beta_ylim0 is not None:
            axs[1].set_ylim(beta_ylim0, beta_ylim1)
        axs[1].set_ylabel("Beta(m,0)")

        plt.suptitle(title, fontsize=18)
        plt.tight_layout()
        plt.savefig(f'./imgs/{title}')
        plt.show()