from p5 import *


def setup():
  createCanvas(400, 400)
  global meteorX
  global meteorY
  meteorX = 50 # starting vlaue
  meteorY = 350  
  background(0,0,128)

def draw():
  global meteorX
  global meteorY
  background(0,0,128, 40)
 
  stroke(255)
  strokeWeight(4)
  point(100,250)
  point(150,300)
  point(200,350)

  # draw meteor
  strokeWeight(6)
  point(meteorX, meteorY)
  meteorX = meteorX + 1
  meteorY = meteorY - 1
  strokeWeight(0)
  fill("white")
  circle(300,300,100)
  fill("navy")
  circle(250,300,100)
  fill("darkgreen")
  triangle(0,50,50,150,150,50)
  triangle(100,50,200,150,250,50)
  fill("chocolate")
  rect(250,50,150,25) 
  fill("darkgreen")
  rect(250,75,150,17)
