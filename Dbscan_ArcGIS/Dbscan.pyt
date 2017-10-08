import arcpy
import math

class Toolbox(object):
    def __init__(self):
        self.label =  "Dbscan toolbox"
        self.alias  = "Dbscan"
	self.cs = 0

        # List of tool classes associated with this toolbox
        self.tools = [DbscanAlgorithm]

class DbscanAlgorithm(object):
    def __init__(self):
        self.label       = "Dbscan Algorithm"
        self.description = ""

    def getParameterInfo(self):
        #Define parameter definitions

        # Input Features parameter
        in_file = arcpy.Parameter(
            displayName="Input File",
            name="in_features",
            datatype="DEFile",
            parameterType="Required",
            direction="Input")

        in_file.filter.list = ['etc']

        # Distance parameter
        distan = arcpy.Parameter(
            displayName="Distance",
            name="Distance",
            datatype="GPLong",
            parameterType="Required",
            direction="Input")

	# Set an acceptable range of 0 to 1000
    	distan.filter.type = "Range"
    	distan.filter.list = [0, 1000] #  Aqui se determina el rango de la distancia permitida entre puntos.

	distan.value = ""

	# Minimum Points parameter
        mpt= arcpy.Parameter(
            displayName="Minimum Points",
            name="minpt",
            datatype="GPLong",
            parameterType="Required",
            direction="Input")

	# Set an acceptable range of 0 to 100
    	mpt.filter.type = "Range"
    	mpt.filter.list = [0, 100] #  Aqui se determina el minimo de puntos que puede conformar un cluster.

	mpt.value = ""

	# Derived Output Features parameter
        out_features = arcpy.Parameter(
            displayName="Output Features",
            name="out_features",
            datatype="GPFeatureLayer",
            parameterType="Derived",
            direction="Output")
        
        out_features.parameterDependencies = [in_file.name]
        out_features.schema.clone = True


        parameters = [in_file, distan, mpt, out_features]

        return parameters  

    def updateMessages(self, parameters): #optional
        return

    def execute(self, parameters, message):
        inFeatures  = parameters[0].valueAsText
        d = parameters[1].valueAsText
	mp = parameters[2].valueAsText
	outFeatures = parameters[3].valueAsText
	
        arcpy.AddMessage(d)
	arcpy.AddMessage(mp)
	
	outFeat = ""
	v = []

	for arr in xrange(0, outFeatures.__len__()):
	    if outFeatures[arr] == "\\":		
		v = arr
	for j in xrange(0, v):
	    outFeat = outFeat + outFeatures[j]

	x = datetime.datetime.now()
	outFeatures = outFeat + "\\Dbscan_"+str(d)+"_"+str(mp)
	
	arcpy.AddMessage(outFeatures)

	path = inFeatures	
        e = int(d)
        minpt = int(mp)

        read = Archivo()
        read.coordinate(path)
        points = read.getCoordinate()
        id_p = read.id_point

        util = Utility()

        scan = Dbscan(points)
        cluster = scan.applyDbscan(e, minpt)
	
	shape = Shapefile()

    	pointShape = []
	clus = []
	id_points = []
	
	nume = 0
	
        for i in xrange(0, cluster.__len__()):
	    num = int(i+1)            
            for j in xrange(0, cluster[i].__len__()):
                for l in xrange(0, points.__len__()):
                    p = Point(cluster[i][j].getX(), cluster[i][j].getY())
                    if util.equalPoints(p,points[l]) == True:			
			pointShape.append(p)
			clus.append(num)			                  
			id_points.append(id_p[l])
			arcpy.AddMessage(str(id_points[nume])+", "+str(clus[nume])+", "+str(p.getX())+", "+str(p.getY()))		
			nume = nume + 1
	
	if os.name == "nt":
	    path = "C:\Windows\Temp\Point_Cluster.txt"
	elif os.name == "posix":
	    path = "\tmp\Point_Cluster.txt" 	
		   
	outfile = open(path, 'w')		

	for l in clus:
		outfile.write(str(l)+'\n')
	outfile.close()

	if os.name == "nt":
	    path = "C:\Windows\Temp\Point_Id.txt"
	elif os.name == "posix":
	    path = "\tmp\Point_Id.txt" 	
		   
	outfile = open(path, 'w')		

	for l in id_points:
		outfile.write(str(l)+'\n')
	outfile.close()
            
	shape.shape(pointShape, outFeatures)
#  _________________________________________________

from decimal import Decimal
import os
cs = 0

class Shapefile:
    
    def shape(self, ptList, outDbscan):
        pt = arcpy.Point()
        ptGeoms = []
	
        for p in ptList:
            pt.X = float(p.getX())
            pt.Y = float(p.getY())
		
            ptGeoms.append(arcpy.PointGeometry(pt))
	   	        
	nameShape = arcpy.CopyFeatures_management(ptGeoms, outDbscan)

	#  coordinateSystem = "GEOGCS['GCS_MAGNA',DATUM['D_MAGNA',SPHEROID['GRS_1980',6378137.0,298,257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]" 
	
	coordinateSystem = "PROJCS[MAGNA_Ciudad_Bogota,GEOGCS['GCS_MAGNA',DATUM['D_MAGNA',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',92334.879],PARAMETER['False_Northing',109320.965],PARAMETER['Central_Meridian',-74.14659166666668],PARAMETER['Scale_Factor',1.000399803265436],PARAMETER['Latitude_Of_Origin',4.680486111111112],UNIT['Meter',1.0]]"
		
	#  nameShape = r"C:\Users\Emmanuel\Desktop\Points.shp"

	arcpy.DefineProjection_management(nameShape, coordinateSystem)
	
	arcpy.AddXY_management(nameShape)
	
	arcpy.AddField_management(nameShape, 'cluster', 'TEXT')
    	
	expression1 = "getClass(!FID!, 1)"
	expression2 = "getClass(!FID!, 2)"
	codeblock = """	
cs = []
import os
def getClass(indice, file):	
    if indice == 0:
	if file == 1:
	    if os.name == "nt":
	        path = "C:\Windows\Temp\Point_Id.txt"
	    elif os.name == "posix":
	        path = "\tmp\Point_Id.txt" 	
	elif file == 2:
	    if os.name == "nt":
	        path = "C:\Windows\Temp\Point_Cluster.txt"
	    elif os.name == "posix":
	        path = "\tmp\Point_Cluster.txt" 

	infile = open(path, 'r')    
			        
	for line in infile:
	    global cs
            cs.append(line)

        infile.close()
	os.remove(path)	
	
    return cs[indice]
"""	
	arcpy.CalculateField_management(nameShape, 'id',expression1, 'PYTHON_9.3', codeblock)
	arcpy.CalculateField_management(nameShape, 'cluster',expression2, 'PYTHON_9.3', codeblock)

	
class Dbscan:

    def __init__(self, date):
        self.util = Utility()
        self.util.defDate(date)
        self.pointList = date
        self.resultList = []
        self.e = 0
        self.minpt = 0
        self.Neighbours = []

    def applyDbscan(self, dist, minpt):

        self.e = dist  #  Interfaz.dU;
        self.minpt = minpt #  Interfaz.mP;
        self.util.VisitList = []

        index2 = 0;
        while self.pointList.__len__() > index2:
            p = self.pointList[index2]
            if self.util.isVisited(p) == False:
                self.util.Visited(p)
                self.Neighbours = []
                self.Neighbours = self.util.getNeighbours(p,dist)

                if self.Neighbours.__len__() >= self.minpt:

                    ind = 0;
                    while self.Neighbours.__len__() > ind:
                        r = self.Neighbours[ind]
                        if self.util.isVisited(r) == False:
                            self.util.Visited(r)
                            Neighbours2 = self.util.getNeighbours(r,dist)
                            if Neighbours2.__len__() >= self.minpt:
                                self.Neighbours = self.util.merge(self.Neighbours, Neighbours2)
                        ind = ind + 1


                    print "N " , self.Neighbours.__len__()
                    self.resultList.append(self.Neighbours)


            index2 = index2 + 1

        return self.resultList



    def reset():
        self.resultList = []
        self.pointList = []
        self.Neighbours = []

class Point:

    def __init__(self,a,b):
        self.X = a
        self.Y = b

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

class Archivo:


    def coordinate(self, path):

        self.coordina = []
        self.id_point = []
        self.util = Utility()

        with open(path) as data_f:
            for l in data_f.readlines():

                line = ""
                cId = ""
                cX = ""
                cY = ""
                court1 = 0
                court2 = 0

                line = l.strip()

                for i in xrange(0, line.__len__()):
                    if line[i] == "," and court1 == 0:
                        court1 = i
                    elif line[i] == "," and court2 == 0:
                        court2 = i

                for i in xrange(0, line.__len__()):
                    if i < court1:
                        cId += line[i]
                    elif i > court1 and i < court2:
                        cX += line[i]
                    elif i > court2:
                        cY += line[i]

                X = float(cX)
                Y= float(cY)

                p = Point(cX,cY)

                val = False

                for l in self.coordina:

                    if self.util.equalPoints(l,p)==True:

                        val = True
                        break
                    else:
                        val = False

                if val == False:
                    self.id_point.append(cId)
                    self.coordina.append(p)

        data_f.close()

        #  cont = 0
        #  for i in self.coordina:
            #  print cont, "  ", i.getX(), "  ", i.getY()
            #  cont = cont + 1

        return self.coordina

    def getCoordinate(self):
        return self.coordina

    def reset(self):
        self.coordina = []
        self.id_point = []

class Utility:
    def __init__(self):
        self.VisitList = []

    def getDistance(self,p,q):
        dx = float(p.getX()) - float(q.getX())
        dy = float(p.getY()) - float(q.getY())
        distance = math.sqrt(math.pow(dx,2) + math.pow(dy,2))
        return distance

    def getNeighbours(self,p, e):
        neigh = []
        points = []
        points = self.getList()

        for i in points:
            q = i
            if self.getDistance(p,q) <= e:
                neigh.append(q)
        return neigh

    def Visited(self,d):
        self.VisitList.append(d)

    def isVisited(self,c):
        if c in self.VisitList:
            return True
        else:
            return False

    def merge(self,a,b):
        it5 = b
        for i in it5:
            t = i
            if t not in a:
			a.append(t)
        return a

    def getList(self):
        return self.newList

    def equalPoints(self,m,n):
        if m.getX()==n.getX() and m.getY()==n.getY():
            return True
        else:
            return False

    def reset(self):
        VisitList = []

    def defDate(self, date):
        self.newList = date
