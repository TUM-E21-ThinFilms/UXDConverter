import matplotlib.pyplot as plt

from typing import List
from uxdconverter.measurement import Measurement

class Plotting(object):
    def plot(self, measurement: List[Measurement], names=None):
        """
        Plots the measurement.

        If measurement is of type list, earch measurement in the list is plotted in the same graph.


        :param Measurement measurement: Single measurement or a list if measurements.
        :return: None
        """

        if not names is None and not len(names) == len(measurement):
            raise ValueError("Given names must have the same length as measurements")
        handles = []
        for ms in measurement:
            data = ms.get_data()
            x = [x[0] for x in data]
            y = [x[1] for x in data]
            y_err = [x[2] for x in data]

            handles.append(plt.errorbar(x, y, yerr=y_err, markeredgewidth=1, capsize=2))

        if not names is None:
            plt.legend(handles, names)

        plt.yscale('log')
        plt.show()


    def interactive_plot(self, measurement: Measurement, signal=None):
        data = measurement.get_data()

        x = [x[0] for x in data]
        y = [x[1] for x in data]
        global picked, norm
        picked = []
        norm = None

        plt.plot(x, y)
        plt.yscale('log')

        # plt.show()

        def on_click(event):
            global picked, norm
            if event.button == 1:
                if event.inaxes:
                    print('Picked coords %f %f' % (event.xdata, event.ydata))
                    picked.append((event.xdata, event.ydata))

            if event.dblclick:
                norm = [event.xdata, event.ydata]
                if not signal is None:
                    signal.sig.emit(norm)

        def on_keyboard(event):
            global picked, norm
            if event.key == 'x' and len(picked) > 0:
                norm = picked[-1]
                picked = []

        plt.gcf().canvas.mpl_connect('button_press_event', on_click)
        plt.gcf().canvas.mpl_connect('key_press_event', on_keyboard)
        plt.show()

        return norm
