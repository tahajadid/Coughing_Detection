############################################################################
#                            By : JADID Taha                               #
#  Link to the project : https://github.com/tahajadid/Coughing_Detection/  #
#                     Contact : tahajadid98@gmail.com                      #
############################################################################

import argparse
import time
import cv2

from processing import extract_parts, draw
from math import *
from config_reader import config_reader
from model.cmu_model import get_testing_model

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', type=str, required=True, help='input image') # Input Images
    parser.add_argument('--output', type=str, default='result.png', help='output image') # The output Traget
    parser.add_argument('--model', type=str, default='model/keras/model.h5', help='path to the weights file') 

    args = parser.parse_args() # Read arg
    image_path = args.image # The Path of the input Image
    output = args.output # The Pathe of output Image
    keras_weights_file = args.model

    max_people = 0 # Initialize the Numbe of existing people
    tic = time.time() # Initialize The Time Counter 
    print('start processing...')

    # load model

    # authors of original model don't use
    # vgg normalization (subtracting mean) on input images
    model = get_testing_model()
    model.load_weights(keras_weights_file)  

    # load config
    params, model_params = config_reader()
    
    input_image = cv2.imread(image_path)  # B,G,R order
    height, width, channels = input_image.shape # image size
    body_parts, all_peaks, subset, candidate = extract_parts(input_image, params, model, model_params)
    canvas = draw(input_image, all_peaks, subset, candidate) # Drawing the body parts
    #The result are stocked in the list by Y-cordinates
    
    # print(all_peaks) -- if you want to see the coordinates of detected points --
    # to get acces you need to acces to the first element of the tuple in the first element of the list
    # in each element in the global list (all_peaks)

    ind = 0

    for x in all_peaks :
        b=len(x)
        if b > max_people:
            max_people=b 
    # to know how many ppl exist in the frame

    while ind<max_people :
        pass
        #Distance P0 P1
        try :
            X0=all_peaks[0][ind][0]
            Y0=all_peaks[0][ind][1]
            X1=all_peaks[1][ind][0]
            Y1=all_peaks[1][ind][1]
            dist_0_1 = sqrt(abs(X0-X1)**2+abs(Y0-Y1)**2)
            print("la distande de P0 à P1 est : ",dist_0_1)
        except:
            print("Les pts P0 ou P1 non-Exist")

        #Distance P2 P3
        try:
            X2=all_peaks[2][ind][0]
            Y2=all_peaks[2][ind][1]
            X3=all_peaks[3][ind][0]
            Y3=all_peaks[3][ind][1]
            dist_2_3 = sqrt(abs(X2-X3)**2+abs(Y2-Y3)**2)
            print("la distande de P2 à P3 est : ",dist_2_3) 
        except:
            print("P2 Or P3 non-Exist") 

        #Distance P3 P4
        try:
            X4=all_peaks[4][ind][0]
            Y4=all_peaks[4][ind][1]
            dist_3_4 = sqrt(abs(X4-X3)**2+abs(Y4-Y3)**2)
            print("la distande de P3 à P4 est : ",dist_3_4) 
        except:
            print("P4 non-Exist") 

        #Distance P5 P6
        try:
            X5=all_peaks[5][ind][0]
            Y5=all_peaks[5][ind][1]
            X6=all_peaks[6][ind][0]
            Y6=all_peaks[6][ind][1]
            dist_5_6 = sqrt(abs(X5-X6)**2+abs(Y5-Y6)**2)
            print("la distande de P5 à P6 est : ",dist_5_6) 
        except:
            print("P5 Or P6 non-Exist") 

        #Distance P6 P7
        try:
            X7=all_peaks[7][ind][0]
            Y7=all_peaks[7][ind][1]
            dist_6_7 = sqrt(abs(X6-X7)**2+abs(Y6-Y7)**2)
            print("la distande de P6 à P7 est : ",dist_6_7) 
        except:
            print("P7 non-Exist") 

        #Distance P0 P4
        try:
            dist_0_4 = sqrt(abs(X0-X4)**2+abs(Y0-Y4)**2)
            print("la distande de P0 à P4 est : ",dist_0_4) 
        except:
            print("P4 non-Exist") 

        #Distance P0 P7
        try:
            dist_0_7 = sqrt(abs(X0-X7)**2+abs(Y0-Y7)**2)
            print("la distande de P0 à P7 est : ",dist_0_7) 
        except:
            print("P7 non-Exist") 

        
        #Valeur absolue dans python est abs()
        #Puissance dans python est **
        #Racine avec python est sqrt()

        r1=0
        try:
            indexR = (dist_5_6+dist_6_7)/(2*dist_0_7)
            print("index Right is : ",indexR)
            if indexR > 1.3 :
                #Coughing
                r1=1
            else :
                #good State
                r1=0
            #print("r1 is ",r1)
            #print("First Result is : ",result1)
        except:
            print("No distance btwn 0 and 7")
        r2=0
        try:
            indexL = (dist_2_3+dist_3_4)/(2*dist_0_4)
            print("index Left is :",indexL)
            if indexL > 1.3 :
                #Coughing
                r2=1
            else :
                #good State
                r2=0
            #print("r2 is : ",r2)
            #print("Second Result is : ",result2)
        except:
            print("No distance btwn 0 and 4")
        ind = ind +1
        toc = time.time()
        print('processing time is %.5f' % (toc - tic))
        try : 
            r=(r1)+(r2)
        except :
            print("r1 Or r2 non-Exist")
        print(r) # The final Result

        # Now we gonna Draw the state of each one on the frame
        try :
            X_toReduce = int(X0/5)
            Y_toReduce = int(Y0/5) 
        except :
            X_toReduce = 40
            Y_toReduce = 30

        if r==0:
            to_put = "Normal"
            cv2.putText(canvas,to_put,(X0-X_toReduce,Y0-Y_toReduce),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2) # Put the Text "State" on the frame
        else : 
            to_put = "Cough"
            cv2.putText(canvas,to_put,(X0-X_toReduce,Y0-Y_toReduce),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2) # Put the Text "State" on the frame
        print(to_put)

    cv2.imwrite(output, canvas) # Show the Frame in The Finale State

    cv2.destroyAllWindows()