import numpy as np
import math
import matplotlib.pyplot as plt
import time
import numpy.fft as fft
import numpy.random as random
from matplotlib.widgets import Slider

xcoords = np.loadtxt("GEM_xcoords.txt", delimiter="\n")
ycoords = np.loadtxt("GEM_ycoords.txt", delimiter="\n")

ncoords = len(xcoords)


xscoords = xcoords[:1000]
yscoords = ycoords[:1000]

def hough(xcoords,ycoords):
  thetas = np.deg2rad(np.arange(-90.0, 90.0, 1))
  width = 200
  height = 200

  diag_len = int(np.sqrt(width**2 + height**2) + 1)

  rhos = int(round(np.sqrt(width**2 + height**2)))
  
  cos_t = np.cos(thetas)
  sin_t = np.sin(thetas)
  num_thetas = len(thetas)

  accumulator = np.zeros((2*diag_len, num_thetas), dtype=np.uint8)

  for ii in range(len(xcoords)):
    rx = random.normal(0,0.5)
    ry = random.normal(0,0.5)
    x = xcoords[ii] + rx
    y = ycoords[ii] + ry

    for tt in range(num_thetas):

      rho = diag_len  + int(round(x*cos_t[tt] + y*sin_t[tt]))
      accumulator[np.abs(min(rho, 2*diag_len-1)), np.abs(min(tt, num_thetas-1))] += 1
  
  return accumulator, thetas, rhos

accumulator = hough(xscoords[10:14], yscoords[10:14])[0]
thetas = hough(xscoords, yscoords)[1]
rhos = hough(xscoords, yscoords)[2]

def fourier(arr1, arr2):

  arr = [arr1, arr2]

  farr = np.real(fft.fft2(arr))

  return farr
  

def showHits():
  
  fig = plt.figure(figsize=(9,5))
  #Plot histogram of hits
  plt.subplot(121)
  plt.hist2d(xscoords, yscoords, bins=40)
  plt.xlim(0,200)
  plt.ylim(0,200)
  plt.title("GEM Hits")
  plt.xlabel("X (mm)")
  plt.ylabel("Y (mm)")

  #Plot fourier transform of hits
  plt.subplot(122)
  ft = fourier(xscoords, yscoords)
  plt.hist2d(ft[0],ft[1], bins=150)
  plt.title("Fourier Transform of GEM Hits")
  plt.xlim(-6000,6000)
  plt.xlabel("X")
  plt.ylabel("Y")

  plt.show()
  plt.clf()


def slide(accumulator):
  fig, ax = plt.subplots()
  plt.subplots_adjust(left=0.25, bottom=0.25)


  l = plt.imshow(accumulator, interpolation='nearest', aspect='auto')

  plt.title("Hough Transform of GEM Hits")
  plt.xlabel(r"$\theta$")
  plt.ylabel(r"$\rho$")

  plt.autoscale(False)

  axcolor = 'lightgoldenrodyellow'
  axnum = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)

  n0 = 10
  snum = Slider(axnum, "Number", 0, 100, valinit=n0, valfmt='%0.0f')

  def update(val):

    num = np.around(snum.val)
    p = int(num)
    l.set_data(hough(xscoords[(p):(p+4)], yscoords[(p):(p+4)])[0])

    fig.canvas.draw_idle()

  snum.on_changed(update)

  plt.show()

showHits()
slide(accumulator)
