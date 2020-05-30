#encoding:utf-8

import matplotlib.pyplot as plt

import numpy as np

# x = [1, 2, 3, 4, 5]
# y=[2.3,3.4,1.2,6.6,7.0]
# plt.scatter(x,y,color='r',marker='+')
#
# plt.show()

# ----------------------------------------------------------------------------------------------------------------
#
# #这是分别设置数据的（起始值，终止值，元素个数）
# x=numpy.linspace(1,5,100)
# #分别设置数据量，还有数据名称
# plt.plot(x,x,label='linear')
# plt.plot(x,x**2,label='quadratic')
# plt.plot(x,x**3,label='cubic')
#
# #分别设置两个参考线
# plt.xlabel('x label')
# plt.ylabel('y label')
#
# #设置数据的标题
# plt.title('Simple Plot')
# plt.legend()
# plt.show()
# ----------------------------------------------------------------------------------------------------------------

# def my_plotter(ax,data1,data2,param_dict):
#     out=ax.plot(data1,data2,**param_dict)
#     return out
#
#
#
# data1,data2,data3,data4=np.random.rand(4,100)
# fig,ax=plt.subplots(1,1)
#
# a=my_plotter(ax,data1,data2,{'marker':'x'})
# # fig.show()
# ax.show()

def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    param_dict : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out

# which you would then use as:

data1, data2, data3, data4 = np.random.randn(4, 100)
fig, ax = plt.subplots(1, 1)
my_plotter(ax, data1, data2, {'marker': 'x'})

fig.show()








