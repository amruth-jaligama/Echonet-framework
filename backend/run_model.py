from Echocardiogram import *
A=Preprocessing('./Videos/')
B=EfSe(destinationFolder, videosFolder, DestinationForWeights)
if __name__ == '__main__':
	A.preprocess()
	B.main()
