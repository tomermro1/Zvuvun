import math

initialvelocity= float(input("Enter your velocity: "))
initialangle= float(input("Enter your angle: "))
initialheight= float(input("Enter your height: "))

def calculateheight(v,a,h):
    time=2*v*math.sin(math.radians(a))

    finalheight=v*time*math.cos(math.radians(a))

    return finalheight
def calculatevelocity(v,a):
    g=10
    time=2*v*math.sin(math.radians(a))
    velocityfinalx=v*math.cos(math.radians(a))
    velocityfinaly=g*time+ v*math.sin(math.radians(a))

    velocityfinal=math.sqrt(velocityfinalx**2+velocityfinaly**2)
    return (velocityfinal)
def calculateangle(v,a,h):
    g=10
    time=v*math.sin(math.radians(a))
    x= v*time*math.cos(math.radians(a))

    vfinalx=v*math.cos(math.radians(a))
    vfinaly=v*math.sin(math.radians(a))-g*time
    vfinal=math.sqrt(vfinalx**2+vfinaly**2)

    finalrad=math.atan(vfinaly/vfinalx)
    finaldeg=math.degrees(finalrad)
    return finaldeg

finalheight=calculateheight(initialvelocity,initialangle,initialheight)
finalvelocity=calculatevelocity(initialvelocity,initialangle)
finalangle = calculateangle(initialvelocity, initialangle, initialheight)
print("Final height:", finalheight, " m")
print("Final velocity:", finalvelocity, " m/s")
print("Final angle:", finalangle, "degrees")
