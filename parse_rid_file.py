import csv
import folium
import numpy as np
import time as tmp
import plotly.graph_objects as go
import sys
import webbrowser


def string_to_float_array_method2(input_string):
     return list(map(float, input_string.split()))
temp_coords=[0,0]
count=0
coords=[]
speed=[]
time=[]
height=[]
rssi=[]
bt_transport=[]

hor_acc=[]
ver_acc=[]
baro_acc=[]
spd_acc=[]
status_drone=[]
distance_from_drone=[]
mac_address=[] 
count_mac_address=[]
operator_id=[]
count_operator_id=[]
category=[] 
count_category=[]
class_value=[]
count_class_value=[]
log_file=sys.argv[1]
mac_address_arg=sys.argv[2]
marker_number=sys.argv[3]
show_graph=sys.argv[4]

tileurl = 'http://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}'


m = folium.Map(location=[0,0],tiles=tileurl,attr='Mapbox')

with open(str(log_file), newline="", encoding="ISO-8859-1") as filecsv:
     lettore = csv.reader(filecsv,delimiter=",")
     for line in lettore:
         
         #check if number is the id of the drone
         
         if(mac_address_arg in line[3]):
           try:
               if(str(line[20])!="" and str(line[21])!=""):
                    temp_coords[0]=(float(line[20])*1e-7) #lat 
                    temp_coords[1]=(float(line[21])*1e-7) #lgn
               if(str(line[29])!=""):
                    time_real=round((float(line[29])/10),2)
                    time.append(time_real)
               if(str(line[18])!=""):
                    speed.append(float(line[18])/4)
               if(str(line[24])!=""):
                    height.append(float((line[24]))/1000)
               if(str(line[5])!=""):
                        rssi.append(float(line[5]))
               if(str(line[2])!=""):
                    bt_transport.append(line[2])
               if(str(line[25])!=""):
                    hor_acc.append(int(line[25]))
               if(str(line[26])!=""):
                    ver_acc.append(int(line[26]))
               if(str(line[27])!=""):
                    baro_acc.append(int(line[27]))
               if(str(line[28])!=""):
                    spd_acc.append(int(line[28]))
               if(str(line[13])!=""):
                    status_drone.append(int(line[13]))
               if(str(line[3])!=""):
                    mac_address.append(str(line[3]))
               if(str(line[31])!=""):
                    distance_from_drone.append(float(line[31]))
               if(str(line[47])!=""):
                    operator_id.append(str(line[47]))
               if(str(line[42])!=""):
                    category.append(str(int(line[42])))
               if(str(line[43])!=""):
                    class_value.append(str(int(line[43])))

               #print("ok")


           except:
           
               continue
           if(str(line[20])!="" and str(line[21])!=""):
                test=(str(temp_coords[0]))+' '+(str(temp_coords[1]))
                result=string_to_float_array_method2(test)
                #print(test)
                coords.append(result)




     # add marker one by one on the map
     if(len(coords)!=0):
          m = folium.Map(location=coords[0],zoom_start=18,max_zoom = 100,tiles=tileurl,attr='Mapbox')

          for i in range(1,len(coords)-2,int(marker_number)):
                    if(speed[i]<0.10):
                        continue
                    else:
                         if(status_drone[i]==1):
                              folium.Circle(radius=0.5,fill_color="green", fill_opacity=0.8,
                              location=coords[i],
                              popup='Height: '+ str(height[i]) + '(m) ' +'Speed: '+str(speed[i])+ '(m/s) '+'Status: '+ str(status_drone[i])+' Time:'+str(time[i]) + " (s)",
                              ).add_to(m)
                         if(status_drone[i]==2):
                              folium.Circle(radius=0.5,fill_color="blue", fill_opacity=0.8,
                              location=coords[i],
                              popup='Height: '+ str(height[i]) + '(m) ' +'Speed: '+str(speed[i])+ '(m/s) '+'Status: '+ str(status_drone[i])+' Time:'+str(time[i]) + " (s)",
                              ).add_to(m)
                         if(status_drone[i]==3):
                              folium.Circle(radius=0.5,fill_color="red", fill_opacity=0.8,
                              location=coords[i],
                              popup='Height: '+ str(height[i]) + '(m) ' +'Speed: '+str(speed[i])+ '(m/s) '+'Status: '+ str(status_drone[i])+' Time:'+str(time[i]) + " (s)",
                              ).add_to(m)



          folium.Marker(
                   location=coords[0], icon=folium.Icon(color="green",icon="location-dot", prefix='fa'),
                   popup=' START / Height: '+ str(height[0]) + '(m) ' +'Speed: '+str(speed[0])+ '(m/s) '+'Status: '+ str(status_drone[0])+' Time:'+str(time[0]) + " (s)",
                   ).add_to(m)
          folium.Marker(
                   location=coords[len(coords)-1], icon=folium.Icon(color="red",icon="location-dot", prefix='fa'),
                   popup=' END / Height: '+ str(height[1]) + '(m) ' +'Speed: '+str(speed[1])+ '(m/s) '+'Status: '+ str(status_drone[1])+' Time:'+str(len(coords)-1) + " (s)",
                   ).add_to(m)
          folium.PolyLine(coords, color='red', weight=2).add_to(m)
          #AntPath(coords, delay=400, dash_array=[30,15], color="red", weight=3).add_to(m)

          print("####TELEMETRY INFORMATION####")
          print("Average speed: "+str(round(np.mean(speed),2))+" m/s" + " |Min Speed: "+str(round(min(speed),2))+ " m/s "+" |Max Speed: "+str(round(max(speed),2))+ " m/s")
          print("Average height: "+str(round(np.mean(height),2))+" m"+ " |Min height: "+str(round(min(height),2))+ " m "+" |Max height: "+str(round(max(height),2))+ " m")
          print("Average hor_acc: "+str(round(np.mean(hor_acc),2))+" m"+ " |Min hor_acc: "+str(round(min(hor_acc),2))+ " m "+" |Max hor_acc: "+str(round(max(hor_acc),2))+ " m")
          print("Average ver_acc: "+str(round(np.mean(ver_acc),2))+" m"+ " |Min ver_acc: "+str(round(min(ver_acc),2))+ " m "+" |Max ver_acc: "+str(round(max(ver_acc),2))+ " m")
          print("Average baro_acc: "+str(round(np.mean(baro_acc),2))+" m"+ " |Min baro_acc: "+str(round(min(baro_acc),2))+ " m "+" |Max baro_acc: "+str(round(max(baro_acc),2))+ " m")
          print("Average spd_acc: "+str(round(np.mean(spd_acc),2))+" m/s" + " |Min spd_acc: "+str(round(min(spd_acc),2))+ " m/s "+" |Max spd_acc: "+str(round(max(spd_acc),2))+ " m/s")
          print("Average rssi: "+str(round(np.mean(rssi),2))+" db"+ " |Min db: "+ str(round(min(rssi),2))+ " db "+" |Max db: "+str(round(max(rssi),2))+ " db")
          print("Average distance from uav: "+str(round(np.mean(distance_from_drone),2))+" m" + " |Min dist: "+str(round(min(distance_from_drone),2))+ " m"+" |Max dist: "+str(round(max(distance_from_drone),2))+ " m")
          #print average mac address
          print("####INFORMATION ON UAV AND REMOTE ID####")
          for a in range(0,len(mac_address)):
              count_mac_address.append(mac_address.count(a))
          most_frequent_mac = mac_address[count_mac_address.index(max(count_mac_address))]
          print("Most Frequent Mac Address: " + str(most_frequent_mac))
          #print average operator id
          for b in range(0,len(operator_id)):
              count_operator_id.append(operator_id.count(b))
          most_frequent_operator_id = operator_id[count_operator_id.index(max(count_operator_id))]
          print("Most Frequent Operator Id: " + str(most_frequent_operator_id))

          #print type of drone
          for c in range(0,len(category)):
              count_category.append(category.count(c))
          most_frequent_category = category[count_category.index(max(count_category))]
          print("Most Frequent Vehicle Category: " + str(most_frequent_category))

          #print class of drone
          for d in range(0,len(class_value)):
              count_class_value.append(class_value.count(d))
          most_frequent_class_value = class_value[count_class_value.index(max(count_class_value))]
          print("Most Frequent Vehicle Class Value: " + str(most_frequent_class_value))

          count_BT5=0
          count_BT4=0
          count_wifi=0
          for i in range(len(bt_transport)):
              if("BT5"in bt_transport[i]):
                  count_BT5+=1
              if("BT4"in bt_transport[i]):
                  count_BT4+=1
              if("Beacon"in bt_transport[i]):
                  count_wifi+=1
          print("On "+str(count_BT5+count_BT4+count_wifi)+ " packets in total "+ str(count_BT5) + " BT5 message were found and "+ str(count_BT4) + " BT4 message were found and " + str(count_wifi) + " Wifi message were found")


          m.save(str(str(mac_address_arg.replace(":","_")))+'.html')

          fig = go.Figure()
          # Create and style traces
          fig.add_trace(go.Scatter(x=time, y=speed, name='Speed',
                         line=dict(color='firebrick', width=4)))
          fig.add_trace(go.Scatter(x=time, y=status_drone, name = 'Status',
                         line=dict(color='royalblue', width=4)))
          fig.add_trace(go.Scatter(x=time, y=height, name='Height',
                         line=dict(color='pink', width=4)))
          fig.update_layout(title='Log of uav '+str(mac_address_arg),
                   xaxis_title='Data',
                   yaxis_title='Time(s)')
          if(show_graph=="1"):
               fig.show()
               webbrowser.open_new_tab(str(mac_address_arg.replace(":","_"))+'.html')
          
     else:
         print("Error , no data found on this drone")
